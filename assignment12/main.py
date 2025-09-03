from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import aiosqlite

DATABSE = "database.db"
app = FastAPI(title = "Student API (Async)")

# ------------- 
# Models 
# -------------
class Student(BaseModel):
    student_id: str
    name: str
    enrolled_year: int
    group_no : int

# ------------
#  Routes 
# -------------

# Get all students
@app.get("/Students")
async def get_students():
    async with aiosqlite.connect(DATABSE) as db:
        db.row_factory = aiosqlite.Row
        cursor = await db.execute("SELECT * FROM students")
        rows = await cursor.fetchall()
        return [dict(row) for row in rows]

# Get student by ID
@app.get("/Students/{student_id}")
async def get_student(student_id: str):
    async with aiosqlite.connect(DATABSE) as db:
        db.row_factory = aiosqlite.Row
        cursor = await db.execute(
            "SELECT * FROM students WHERE student_id = ?", (student_id,)
            )
        row = await cursor.fetchone()
        if row is None:
            raise HTTPException(status_code=404, detail="Student not found")
        return dict(row)
    
# Add a new student
@app.post("/Students")
async def add_student(student: Student):
    try:
        async with aiosqlite.connect(DATABSE) as db:
            await db.execute(
                "INSERT INTO students (student_id, name, enrolled_year, group_no) VALUES (?, ?, ?, ?)",
                (student.student_id, student.name, student.enrolled_year, student.group_no)
            )
            await db.commit()
        return {"message": "Student added successfully"}
    except aiosqlite.IntegrityError:
        raise HTTPException(status_code=400, detail="Student ID already exists")
    
# Update student
@app.put("/Students/{student_id}")
async def update_student(student_id: str, student: Student):
    async with aiosqlite.connect(DATABSE) as db:
        cursor = await db.execute(
            "UPDATE students SET name = ?, enrolled_year = ?, group_no = ? WHERE student_id = ?",
            (student.name, student.enrolled_year, student.group_no, student_id)
        )
        await db.commit()
        if cursor.rowcount == 0:
            raise HTTPException(status_code=404, detail="Student not found")
    return {"message": "Student updated successfully"}

# Delete student
@app.delete("/Students/{student_id}")
async def delete_student(student_id: str):
    async with aiosqlite.connect(DATABSE) as db:
        cursor = await db.execute(
            "DELETE FROM students WHERE student_id = ?", (student_id,)
        )
        await db.commit()
        if cursor.rowcount == 0:
            raise HTTPException(status_code=404, detail="Student not found")
    return {"message": "Student deleted successfully"}

# Analytics : Number of students per group
@app.get("/analytics/group")
async def analytics_group():
    async with aiosqlite.connect(DATABSE) as db:
        cursor = await db.execute(
            "SELECT group_no, COUNT(*) as student_count FROM students GROUP BY group_no"
        )
        rows = await cursor.fetchall()
        return [{"group_no": row[0], "student_count": row[1]} for row in rows]
    
# Analytics : Number of students per enrolled year
@app.get("/analytics/year")
async def analytics_year():
    async with aiosqlite.connect(DATABSE) as db:
        cursor = await db.execute(
            "SELECT enrolled_year, COUNT(*) as student_count FROM students GROUP BY enrolled_year"
        )
        rows = await cursor.fetchall()
        return [{"enrolled_year": row[0], "student_count": row[1]} for row in rows]