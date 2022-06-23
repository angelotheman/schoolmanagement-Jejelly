from typing import List, Any, Optional
from domain.schoolManagement.studentSchema import UserCreateSchema, StudentDB, UserupdateSchema

class StudentService:
    
    def __init__(self, student_queries: Any ):
        self._student_queries = student_queries

    async def create_student(self,student: UserCreateSchema)-> StudentDB:
        new_student =  await self._student_queries.create_student(student)
        return new_student



    async def update_student_details(self,student_id: int, new_student: UserupdateSchema)-> StudentDB:
        old_student_detail = self._student_queries.get_student_by_id(student_id)
        updated_details = self._student_queries.update_student(old_student_detail,new_student)
        return updated_details

    async def get_student_by_id(student_id : int) -> Optional[StudentDB]:
        user = self._student_queries.get_student_by_id()
        if user :
            return user 
        else:
            None    

    async def get_user_list(self)-> List[StudentDB]:
        users = await self._student_queries.get-all_users()
        return users


    async def remove_student (self,student_id:int) -> StudentDB:
        deleted_user = self._student_queries.delete_user(student_id)  
        reuturn deleted_user 

