from fastapi import FastAPI, Path, HTTPException
from typing import Optional

app = FastAPI()

students = {
    1: {
        "name": "john",
        "age": 17, 
        "class": "year 12"
    }
}

@app.get("/")
def index():
    return {"name": "First Data"}

@app.get("/get-student/{student_id}")
def get_student(student_id: int = Path(..., description="The ID of the student you want to view")):
    if student_id not in students:
        raise HTTPException(status_code=404, detail="Student not found")
    return students[student_id]

@app.get("/get-by-name")
def get_student_by_name(name: str):
    for student_id in students:
        if students[student_id]["name"].lower() == name.lower():
            return students[student_id]
    raise HTTPException(status_code=404, detail="Student not found")