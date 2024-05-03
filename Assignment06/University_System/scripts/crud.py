from typing import Optional
from sqlalchemy.orm import Session
import models, schemas

# **************** Students ************** #

def get_students(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Student).offset(skip).limit(limit).all()

def create_student(db: Session, student: schemas.StudentCreate):
    db_student = models.Student(firstname=student.firstname, lastname=student.lastname, average=student.average, graduated=student.graduated)
    db.add(db_student)
    db.commit()
    db.refresh(db_student)
    return db_student

def get_student(db: Session, id: int):
    return db.query(models.Student).filter(models.Student.id == id).first()


def update_student(db: Session, id: int, student: schemas.StudentUpdate):
    db_student = get_student(db, id=id)
    if db_student:
        db_student.average = student.average
        db_student.firstname = student.firstname
        db_student.lastname = student.lastname
        db_student.graduated = student.graduated
        
        db.commit()
        db.refresh(db_student)
        return db_student
    return None


def delete_student(db: Session, id: int):
    db_student = get_student(db, id=id)
    if db_student:
        db.delete(db_student)
        db.commit()
        return 'Ok'
    return None

# **************** Courses ************** #

def get_courses(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Course).offset(skip).limit(limit).all()

def create_course(db: Session, course: schemas.CourseCreate):
    db_course = models.Course(name=course.name, unit=course.unit)
    db.add(db_course)
    db.commit()
    db.refresh(db_course)
    return db_course

def get_course(db: Session, id: int):
    return db.query(models.Course).filter(models.Course.id == id).first()


def update_course(db: Session, id: int, course: schemas.CourseUpdate):
    db_course = get_course(db, id=id)
    if db_course:
        db_course.name = course.name
        db_course.unit = course.unit
        
        db.commit()
        db.refresh(db_course)
        return db_course
    return None


def delete_course(db: Session, id: int):
    db_course = get_course(db, id=id)
    if db_course:
        db.delete(db_course)
        db.commit()
        return 'Ok'
    return None
