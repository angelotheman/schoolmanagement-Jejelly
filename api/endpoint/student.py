from fastapi import fastAPI  
from typing import List, Optional
from fastapi import Depends, HTTPException, APIRouter
from api.utils import get_student_services 
from domain.schoolManagement.studentService import StudentService
from domain.schoolManagement.studentSchema import StudentDB, StudentCreateSchema, StudentupdateSchema

router =  APIRouter 

@router.post("/" , response_model=StudentDB)
async def create_student( student: StudentCreateSchema, student_services: StudentService = Depends(get_student_services)) -> StudentModel:
    return await student.create_student(student)


@router.get("/{student_id}", response_model= StudentDB )
async def get_student_by_id(student_id: int, student_services: StudentService = Depends(get_student_services)) -> StudentDB:
    return student_services.get_student_by_id(student_id)


