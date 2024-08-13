from Exam_4.admin.teacher_for import TeacherFor, int_input


class Admin(TeacherFor):
    def show_menu_admin(self, phone: str) -> bool:
        text = """
        1. Sozlamalar
        2. Student uchun
        3. Ustoz uchun
        4. Chiqish
        """
        print(text)
        num = int_input("Raqam tanlang: ")
        if num == 2:
            self.student_for()
        elif num == 3:
            self.teacher_for()
        elif num == 1:
            self.personal_admin(phone)
        else:
            self.exit = True
            return self.exit

    def personal_admin(self, phone: str) -> None:
        pass

    def student_for(self) -> bool:
        pass

    def teacher_for(self) -> bool:
        pass
