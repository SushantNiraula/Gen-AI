from pydantic import BaseModel
from pydantic import Field
from typing import Optional

class Student(BaseModel):
    name:str
    age: int=1 ## default value
    roll_no: Optional[int]=None ## optional field
    cgpa: float = Field(gt=0, lt=10, default=5,description="CGPA of the student") ## field with constraints and description
    

new_student={'name':"Sushant",'email':'sushantniraula1'}
student=Student(**new_student)
print(student)