from Exam_4.teacher.teacher import Teacher, int_input


class Admin(Teacher):
    def show_menu_admin(self, phone: str) -> bool:
        self.exit = True
        return self.exit
