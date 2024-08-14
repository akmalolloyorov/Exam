from Exam_4.admin.student_for import StudentFor, int_input


class PersonalTeacher(StudentFor):
    def personal_teacher(self, phone: str, file: dict) -> bool:
        self.phone = phone
        text = """
        1. Telefon raqamni o'zgartirish
        2. Usernameni o'zgartirish
        3. Parolni o'zgaritish
        4. Tug'ilgan sanani o'zgartirish
        5. Gmailni o'zgaritish
        6. Chiqish
        """
        print(text)
        num = int_input("Raqam tanlang: ")
        if num == 1:
            self.change_phone_admin('teacher', phone, file)
            self.personal_teacher(self.phone, file)
        elif num == 2:
            self.change_user_admin('teacher', phone, file)
            self.personal_teacher(phone, file)
        elif num == 3:
            self.change_password_admin('teacher', phone, file)
            self.personal_teacher(phone, file)
        elif num == 4:
            self.change_birth_date_admin('teacher', phone, file)
            self.personal_teacher(phone, file)
        elif num == 5:
            self.change_gmail_admin('teacher', phone, file)
            self.personal_teacher(phone, file)
        else:
            self.exit = True
            return self.exit
