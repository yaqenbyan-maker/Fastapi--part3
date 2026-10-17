from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import sqlite3

app = FastAPI()

# نموذج البيانات (Pydantic Model) لاستقبال وتصديق بيانات الطالب
class Student(BaseModel):
    name: str
    age: int
    grade: int

# الخطوة 2 و 3: تهيئة قاعدة البيانات وإنشاء الجدول إذا لم يكن موجوداً
def setup_database():
    try:
        conn = sqlite3.connect("school.db")
        cursor = conn.cursor()
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS students (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT,
                age INTEGER,
                grade INTEGER
            )
        """)
        conn.commit()
        conn.close()
    except Exception as e:
        print(f"Error setting up database: {e}")

# استدعاء دالة التهيئة في بداية تشغيل التطبيق
setup_database()


# 1. وظيفة القراءة (Read - GET): جلب جميع الطلاب المسجلين
@app.get("/students")
async def read_students():
    try:
        conn = sqlite3.connect("school.db")
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM students")
        students = cursor.fetchall()
        conn.close()
        return {"students": students}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


# 2. وظيفة الإضافة (Create - POST): إضافة طالب جديد
@app.post("/students")
async def create_student(student: Student):
    try:
        conn = sqlite3.connect("school.db")
        cursor = conn.cursor()
        cursor.execute(
            "INSERT INTO students (name, age, grade) VALUES (?, ?, ?)",
            (student.name, student.age, student.grade)
        )
        conn.commit()
        conn.close()
        return {"message": "Student added successfully", "student": student}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


# 3. وظيفة التحديث (Update - PUT): تحديث بيانات طالب بناءً على الـ ID
@app.put("/students/{student_id}")
async def update_student(student_id: int, student: Student):
    try:
        conn = sqlite3.connect("school.db")
        cursor = conn.cursor()
        cursor.execute(
            "UPDATE students SET name = ?, age = ?, grade = ? WHERE id = ?",
            (student.name, student.age, student.grade, student_id)
        )
        conn.commit()
        conn.close()
        return {"message": "Student updated successfully", "id": student_id}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


# 4. وظيفة الحذف (Delete - DELETE): حذف طالب بناءً على الـ ID
@app.delete("/students/{student_id}")
async def delete_student(student_id: int):
    try:
        conn = sqlite3.connect("school.db")
        cursor = conn.cursor()
        cursor.execute("DELETE FROM students WHERE id = ?", (student_id,))
        conn.commit()
        conn.close()
        return {"message": "Student deleted successfully", "id": student_id}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))