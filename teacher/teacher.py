from Exam_4.user.user import User, int_input


class Teacher(User):
    def show_menu_teacher(self, phone: str) -> bool:
        print(phone)
        self.exit = True
        return self.exit
