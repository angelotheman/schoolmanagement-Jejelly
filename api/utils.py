from domain.schoolManagement.StudentService import StudentService
from infrastructure.database.student.models.student import StudentQueries

def get_student_services()-> StudentService:
    return StudentService(StudentQueries)