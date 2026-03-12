from pydantic import BaseModel, EmailStr, Field
from typing import Optional


class Student(BaseModel):

    name: str = 'Soni'
    age: Optional[int] = None
    email: EmailStr
    cgpa: float = Field(gt=0, lt=10)

new_student = {'name' : 'Soni', 'email': 'abc@gmail.com', 'cgpa': 9.0}

student = Student(**new_student)
student_dict = dict(student)


print(student_dict['age'])