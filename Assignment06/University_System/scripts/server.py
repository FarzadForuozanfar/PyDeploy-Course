from fastapi import Depends, FastAPI, HTTPException
from sqlalchemy.orm import Session
from typing import Optional

import crud, models, schemas
from database import SessionLocal, engine

models.Base.metadata.create_all(bind=engine)

app = FastAPI()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# **************** Students ************** #

@app.post("/students/", response_model=schemas.Student)
def create_student(student: schemas.StudentCreate, db: Session = Depends(get_db)):
    return crud.create_student(db=db, student=student)


@app.get("/students/", response_model=list[schemas.Student])
def read_students(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    students = crud.get_students(db, skip=skip, limit=limit)
    return students


@app.get('/students/{id}', response_model=schemas.Student)
def read_student(id: int, db: Session = Depends(get_db)):
    student = crud.get_student(db, id=id)
    if student is None:
        raise HTTPException(404, 'Student Not Found')
    return student


@app.put('/students/{id}', response_model=schemas.Student)
def update_student(id: int, student: schemas.StudentUpdate, db: Session = Depends(get_db)):
    student = crud.update_student(db, id=id, student=student)
    if student is None:
        raise HTTPException(404, 'Student Not Found')
    return student


@app.delete('/students/{id}')
def delete_student(id: int, db: Session = Depends(get_db)):
    result = crud.delete_student(db, id=id)
    if result:
        return "Student Deleted."
    raise HTTPException(404, 'Student Not Found')


# **************** Courses ************** #

@app.post("/courses/", response_model=schemas.Course)
def create_course(course: schemas.CourseCreate, db: Session = Depends(get_db)):
    return crud.create_course(db=db, course=course)


@app.get("/courses/", response_model=list[schemas.Course])
def read_courses(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    courses = crud.get_courses(db, skip=skip, limit=limit)
    return courses


@app.get('/courses/{id}', response_model=schemas.Course)
def read_course(id: int, db: Session = Depends(get_db)):
    course = crud.get_course(db, id=id)
    if course is None:
        raise HTTPException(404, 'Course Not Found')
    return course


@app.put('/courses/{id}', response_model=schemas.Course)
def update_course(id: int, course: schemas.CourseUpdate, db: Session = Depends(get_db)):
    course = crud.update_course(db, id=id, course=course)
    if course is None:
        raise HTTPException(404, 'Course Not Found')
    return course


@app.delete('/courses/{id}')
def delete_course(id: int, db: Session = Depends(get_db)):
    result = crud.delete_course(db, id=id)
    if result:
        return "Course Deleted."
    raise HTTPException(404, 'Course Not Found')

