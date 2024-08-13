from Exam_4.admin.teacher_for import TeacherFor, int_input


class Admin(TeacherFor):
    def show_menu_admin(self, phone: str, file: dict) -> bool:
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
            if self.exit:
                self.exit = False
                self.show_menu_admin(phone, file)
        elif num == 3:
            self.teacher_for()
            if self.exit:
                self.exit = False
                self.show_menu_admin(phone, file)
        elif num == 1:
            self.personal_admin(phone, file)
            if self.exit:
                self.exit = False
                self.show_menu_admin(self.phone, file)
        else:
            self.exit = True
            return self.exit
