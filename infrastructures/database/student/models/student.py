from typing import  List 
from domain.schoolManagement.IStudentQueries import IStudentQueriesInterface
from domain.schoolManagement.studentSchema import StudentCreateSchema, StudentupdateSchema
from core.db import db 

class StudentModel(db.Model):
    __tablename__ = "user base"

    student_id = db.Column("id",db.Integer, autoincreamen=Ture, primary_key=True,)
    emial = db.Column("email",db.String,nullable=False, unique= True)
    password= db.Column("password",db.String, nullalble=False)
    first_name = db.Column("first_name", db.String, nullable=False)
    last_name = db.Column("last_name", db.String, nullable=False)
    is_active = db.Column("is_active", db.Boolean, nullable=False)
    is_superuser = db.Column("is_superuser", db.Boolean, nullable=False)
    created_date = db.Column("created_date", db.DateTime,default=db.func.now(),nullable=False, )
    



class StudentQueries(IStudentQueriesInterface):

    async def create_student(self,user: User: StudentCreateSchema ) -> StudentModel:
        return await StudentModel.create(**user.__dict__)

    async def update_student(self, old_student_detail: StudentModel, new_student:StudentupdateSchema ) -> StudentModel:
        updated_student_details = await old_student_detail.update(**new_student.__dict__).apply()
        return update_student_details._instance

    async def delete_user(self, student_id:int)-> StudentModel:
        return await StudentModel.get(student_id).delete()

    async def  get_student_by_id(self, student_id: int )-> StudentModel:
        return await StudentModel.get(student_id) 


    # async def get_all_student(self)-> List[StudentModel]:
    #     return await StudentModel.get          