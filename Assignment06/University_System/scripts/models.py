from sqlalchemy import Table, Column, Integer, String, Float, Boolean, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

# Define the association table for the many-to-many relationship
student_course_association = Table(
    'student_course_association',
    Base.metadata,
    Column('student_id', Integer, ForeignKey('students.id')),
    Column('course_id', Integer, ForeignKey('courses.id'))
)

class Student(Base):
    __tablename__ = "students"

    id = Column(Integer, primary_key=True)
    firstname = Column(String)
    lastname = Column(String)
    average = Column(Float)
    graduated = Column(Boolean, default=False)

    # Define the relationship with Course
    courses = relationship("Course", secondary=student_course_association, back_populates="students")


class Course(Base):
    __tablename__ = "courses"

    id = Column(Integer, primary_key=True)
    name = Column(String)
    unit = Column(Integer)

    # Define the relationship with Student
    students = relationship("Student", secondary=student_course_association, back_populates="courses")
