from Exam_4.admin.student_for import StudentFor, int_input


class Teacher(StudentFor):
    def show_menu_teacher(self, phone: str, file: dict) -> bool:
        text = """
        1. Dars o'tish
        2. Studentlarni baholash
        3. Student bahosin o'zgartirish
        4. Dars vaqtini ko'rish
        5. Sozlamalar
        """
        print(text)
        num = int_input("Raqamni tanlang: ")
        if num == 1:
            self.lesson_for(phone, file)
            self.show_menu_teacher(phone, file)
        elif num == 2:
            self.rating_ball(phone, file)
            self.show_menu_teacher(phone, file)
        elif num == 3:
            self.change_rating(phone, file)
            self.show_menu_teacher(phone, file)
        elif num == 4:
            self.view_lesson_time(phone, file)
            self.show_menu_teacher(phone, file)
        elif num == 5:
            print("tez kunlarda.")
            self.show_menu_user(phone, file)
        else:
            self.exit = True
            return self.exit

    def lesson_for(self, phone: str, file: dict) -> None:
        pass

    def rating_ball(self, phone: str, file: dict) -> None:
        pass

    def change_rating(self, phone: str, file: dict) -> None:
        pass

    def view_lesson_time(self, phone: str, file: dict) -> None:
        pass
