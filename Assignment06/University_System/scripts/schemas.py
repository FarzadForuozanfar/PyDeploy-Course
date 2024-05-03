from pydantic import BaseModel
from typing import Optional

class CourseBase(BaseModel):
    name: str
    unit: int


class CourseCreate(CourseBase):
    pass


class Course(CourseBase):
    id: int

    class Config:
        orm_mode = True


class CourseUpdate(BaseModel):
    name: Optional[str] = None
    unit: Optional[int] = None



class StudentBase(BaseModel):
    firstname: str
    lastname: str


class StudentCreate(StudentBase):
    pass

class StudentUpdate(BaseModel):
    firstname: Optional[str] = None
    lastname: Optional[str] = None
    average: Optional[float] = None
    graduated: Optional[bool] = None

class Student(StudentBase):
    id: int
    average: float
    graduated: bool
    
    class Config:
        orm_mode = True

