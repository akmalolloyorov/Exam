from Exam_4.admin.student_for import StudentFor, int_input


class TeacherFor(StudentFor):
    def teacher_for(self) -> bool:
        self.exit = True
        return self.exit

    def add_teacher(self, file: dict) -> None:
        pass
