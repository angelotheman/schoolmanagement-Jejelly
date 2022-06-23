from abc import abstractmethod 

# This is supported only in python: > 3.6
from __future__ import annotations

from typing import List , TYPE_CHECKING
from domain.schoolManagement.studentSchema import \StudentCreateSchema, StudentupdateSchema

if TYPE_CHECKING:
    from infrastructure.database.student.models import StudentModel

class IStudentQueriesInterface:
    @abstractmethod
    async def  create_student( self, user: StudentCreateSchema) -> UserModel:
        raise NotImplementedError

    @abstractmethod
    async def update(self, old_student_detail: USerModel, new_student: StudentupdateSchema)-> StudentModel:
        raise NotImplementedError

    @abstractmethod
    async def delete_student( self, student_id:int ) -> StudentModel:
    raise NotImplementedError

   @abstractmethod
   async def get_student_by_id(self , student_id:int) -> StudentModel:
       raise NotImplementedError


    @abstractmethod
    async def get_all_student(self) -> List[StudentModel]:
        raise NotImplementedError   
