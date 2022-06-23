import pydantic from BaseModel, EmailStr
from typing import Optional

class BaseStudent(BaseModel):
    first_name : Optional[str ] = None
    last_name :Optional[str]   = None
    course: Optional[str] = None 
    is_active : optional[bool] = False
    is_superuser: Optional[bool] = False
    email: Optional[EmailStr] = None 


class StudentCreateSchema(BaseStudent):
    email: EmailStr
    password: str

class StudentupdateSchema(BaseStudent):
    password: Optional[str]= None

class StudentDB(BaseStudent):
    student_id: int

    class Config:
        orm_mode = True
