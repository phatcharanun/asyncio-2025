import httpx
import folium
from fastapi import FastAPI, HTTPException
from fastapi.responses import HTMLResponse
from pydantic import BaseModel
from typing import Dict

app = FastAPI(title="Service Registry")

# เก็บ service ที่ลงทะเบียน (in-memory)
services: Dict[str, dict] = {}

# ข้อมูลที่ต้องส่งมาเวลา register
class Service(BaseModel):
    name: str
    url: str
    city: str

@app.get("/services")
async def list_services():
    """ดู service ทั้งหมดที่ลงทะเบียนไว้"""
    return services

@app.post("/register")
async def register_service(service: Service):
    """ลงทะเบียน service ใหม่"""
    if service.name in services:
        raise HTTPException(status_code=400, detail="Service already exists")
    services[service.name] = service.dict()
    return {"message": f"Service {service.name} registered", "data": service.dict()}

@app.delete("/unregister/{name}")
async def unregister_service(name: str):
    """ลบ service ออก"""
    if name not in services:
        raise HTTPException(status_code=404, detail="Service not found")
    del services[name]
    return {"message": f"Service {name} removed"}

@app.put("/update")
async def update_service(service: Service):
    """อัปเดต service"""
    if service.name not in services:
        raise HTTPException(status_code=404, detail="Service not found")
    services[service.name] = service.dict()
    return {"message": f"Service {service.name} updated", "data": service.dict()}

# ---------------- Aggregate Map ----------------
@app.get("/aggregate", response_class=HTMLResponse)
async def aggregate():
    """รวมข้อมูลจากทุก student service และแสดง Folium Map"""
    if not services:
        return HTMLResponse("<h3>ยังไม่มี student service ถูก register</h3>")

    m = folium.Map(location=[14.994,103.104], zoom_start=6)  # default Bangkok

    async with httpx.AsyncClient() as client:
        for svc in services.values():
            try:
                r = await client.get(svc["url"])
                w = r.json()
                popup = f"""
                <b>{w['city']}</b><br>
                {w['name']}<br>
                Temp: {w['temperature']} °C<br>
                Humidity: {w['humidity']}%<br>
                {w['weather']}
                """
                folium.Marker(
                    location=[float(w["lat"]), float(w["lon"])],
                    popup=popup,
                    tooltip=w["city"]
                ).add_to(m)
            except Exception as e:
                print("Error fetching:", svc, e)

    return HTMLResponse(content=m.get_root().render())