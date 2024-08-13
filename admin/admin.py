from Exam_4.admin.personal_admin import PersonalAdmin, int_input


class Admin(PersonalAdmin):
    def show_menu_admin(self, phone: str, file: dict) -> bool:
        text = """
        1. Sozlamalar
        2. Student uchun
        3. Ustoz uchun
        4. Student qo'shish
        5. Ustoz qo'shish
        6. Chiqish
        """
        print(text)
        num = int_input("Raqam tanlang: ")
        if num == 2:
            self.student_for(file=file)
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
        elif num == 4:
            self.add_student(file)
            self.show_menu_admin(phone, file)
        elif num == 5:
            self.add_teacher(file)
            self.show_menu_admin(phone, file)
        else:
            self.exit = True
            return self.exit
