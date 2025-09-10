import httpx
import folium
from fastapi import FastAPI
from fastapi.responses import HTMLResponse
from dotenv import dotenv_values

app = FastAPI(title="Student Service")

# ฟังก์ชันอ่าน config ทุกครั้งจาก .env-sample
def load_config():
    return dotenv_values(".env-sample")

# -------------------- Weather --------------------
@app.get("/weather")
async def get_weather():
    cfg = load_config()
    url = (
        f"https://api.openweathermap.org/data/2.5/weather?"
        f"lat={cfg['LAT']}&lon={cfg['LON']}&appid={cfg['OWM_API_KEY']}&units=metric"
    )
    async with httpx.AsyncClient() as client:
        resp = await client.get(url)
        data = resp.json()

    return {
        "name": cfg["STUDENT_NAME"],
        "city": cfg["CITY"],
        "lat": cfg["LAT"],
        "lon": cfg["LON"],
        "temperature": data["main"]["temp"],
        "humidity": data["main"]["humidity"],
        "weather": data["weather"][0]["description"],
    }

# -------------------- Register Self --------------------
@app.post("/register_self")
async def register_self():
    cfg = load_config()
    payload = {"name": cfg["STUDENT_NAME"], "url": cfg["SELF_URL"], "city": cfg["CITY"]}
    async with httpx.AsyncClient() as client:
        resp = await client.post(f"{cfg['SERVICE_REGISTRY_URL']}/register", json=payload)
        return resp.json()

# -------------------- Update Self --------------------
@app.put("/update_self")
async def update_self():
    cfg = load_config()
    payload = {"name": cfg["STUDENT_NAME"], "url": cfg["SELF_URL"], "city": cfg["CITY"]}
    async with httpx.AsyncClient() as client:
        resp = await client.put(f"{cfg['SERVICE_REGISTRY_URL']}/update", json=payload)
        return resp.json()

# -------------------- Unregister Self --------------------
@app.delete("/unregister_self")
async def unregister_self():
    cfg = load_config()
    async with httpx.AsyncClient() as client:
        resp = await client.delete(f"{cfg['SERVICE_REGISTRY_URL']}/unregister/{cfg['STUDENT_NAME']}")
        return resp.json()

# -------------------- Aggregate --------------------
@app.get("/aggregate", response_class=HTMLResponse)
async def aggregate():
    cfg = load_config()
    async with httpx.AsyncClient() as client:
        resp = await client.get(f"{cfg['SERVICE_REGISTRY_URL']}/services")
        registry = resp.json()

        # ใช้จุดกลางจากไฟล์ .env
        m = folium.Map(location=[float(cfg["LAT"]), float(cfg["LON"])], zoom_start=6)
        for svc in registry.values():
            try:
                r = await client.get(svc["url"])
                w = r.json()

                popup = f"""
                <b>{w['city']}</b><br>
                Temp: {w['temperature']} °C<br>
                Humidity: {w['humidity']}%<br>
                {w['weather']}
                """

                # --- ปักหมุดตาม lat/lon ที่ service รายงาน ---
                folium.Marker(
                    location=[float(w["lat"]), float(w["lon"])],
                    popup=popup,
                    tooltip=w["city"]
                ).add_to(m)

                # --- ปักหมุดบังคับตาม lat/lon จาก .env ของ aggregator ---
                folium.Marker(
                    location=[float(cfg["LAT"]), float(cfg["LON"])],
                    popup=f"Fixed marker for {w['city']}",
                    icon=folium.Icon(color="red", icon="info-sign"),
                    tooltip=f"{cfg['CITY']} (fixed)"
                ).add_to(m)

            except Exception as e:
                print("Error fetching:", svc, e)

        return HTMLResponse(content=m.get_root().render())
