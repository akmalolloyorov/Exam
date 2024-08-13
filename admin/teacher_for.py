from Exam_4.teacher.teacher import Teacher, int_input


class TeacherFor(Teacher):
    def teacher_for(self) -> bool:
        text = """
        1. Dars o'tish
        2. Guruhni ko'rish
        3. 
        """
        print(text)
        self.exit = True
        return self.exit

    def add_teacher(self, file: dict) -> None:
        pass
