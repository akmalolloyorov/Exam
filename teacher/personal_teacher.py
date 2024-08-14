from Exam_4.admin.student_for import StudentFor, int_input


class PersonalTeacher(StudentFor):
    def personal_teacher(self, phone: str, file: dict) -> bool:
        self.exit = True
        return self.exit
