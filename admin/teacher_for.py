from Exam_4.teacher.teacher import Teacher, int_input


class TeacherFor(Teacher):
    def teacher_for(self, file: dict) -> bool:
        phone = self.choice_teacher_admin_for(file=file)
        if phone == "none":
            print("Hali teacher qo'shilmagan")
        else:
            text = """
            1. Teacher haqida malumot
            2. Teacher sozlamalari 
            3. Chiqish
            """
            print(text)
            num = int_input("Raqam tanlang: ")
            if num == 1:
                self.teacher_about(phone=phone, file=file)
                self.teacher_for(file)
            elif num == 2:
                self.teacher_settings(phone=self.phone, file=file)
                self.teacher_for(file)
            else:
                self.exit = True
                return self.exit

    def teacher_about(self, phone: str, file: dict) -> None:
        text = """
        1. To'liq ismini ko'rish
        2. Usernamesin ko'rish
        3. Tug'ilgan sanasin ko'rish
        4. Gmailini ko'rish
        5. Jinsini ko'rish
        6. Guruhlarin ko'rish
        7. O'quvchilarin ko'rish
        8. Chiqish
        """
        print(text)
        num = int_input("Raqam tanlang: ")
        if num == 1:
            self.view_teacher_name(phone=phone, file=file)
            self.teacher_about(phone=phone, file=file)
        elif num == 2:
            self.view_teacher_user_name(phone=phone, file=file)
            self.teacher_about(phone=phone, file=file)
        elif num == 3:
            self.view_teacher_birthday(phone=phone, file=file)
            self.teacher_about(phone=phone, file=file)
        elif num == 4:
            self.view_teacher_gmail(phone=phone, file=file)
            self.teacher_about(phone=phone, file=file)
        elif num == 5:
            self.view_teacher_gender(phone=phone, file=file)
            self.teacher_about(phone=phone, file=file)
        elif num == 6:
            self.view_teacher_groups(phone=phone, file=file)
            self.teacher_about(phone=phone, file=file)
        elif num == 7:
            self.view_teacher_students(phone=phone, file=file)
            self.teacher_about(phone=phone, file=file)
        else:
            self.teacher_for(file)

    def view_teacher_students(self, phone: str, file: dict) -> None:
        pass

    def view_teacher_groups(self, phone: str, file: dict) -> None:
        pass

    def view_teacher_name(self, phone: str, file: dict) -> None:
        pass

    def view_teacher_gmail(self, phone: str, file: dict) -> None:
        pass

    def view_teacher_birthday(self, phone: str, file: dict) -> None:
        pass

    def view_teacher_gender(self, phone: str, file: dict) -> None:
        pass

    def view_teacher_user_name(self, phone, file: dict) -> None:
        name: str = file['teacher'][phone]['full_name']
        print(f"Ustoz to'liq simi: {name}")
        self.__str__()

    def choice_teacher_admin_for(self, file: dict) -> str:
        teacher_phone: list = []
        teacher_name_list: list = []
        if len(file['teacher']) > 0:
            for phone in file['teacher'].keys():
                teacher_name_list.append(file['teacher'][phone]['full_name'])
                teacher_phone.append(phone)
            teacher_name = self.list_choice(teacher_name_list)
            teacher_index = teacher_name_list.index(teacher_name)
            phone = teacher_phone[teacher_index]
            return phone
        else:
            return "none"

    def teacher_settings(self, phone: str, file: dict) -> None:
        self.phone = phone
        text = """
        1. Telefon raqamini o'zgartirish
        2. Parolini o'zgartirish
        3. Usernamesin o'zgartirish
        4. tug'ilgan kunini o'zgartirish
        5. Gmailni o'zgartirish
        6. Chiqish
        """
        print(text)
        num = int_input("Raqam tanlang: ")
        if num == 1:
            self.change_phone_admin('teacher', phone, file)
            self.teacher_settings(phone=self.phone, file=file)
        elif num == 2:
            self.change_password_admin('teacher', phone, file)
            self.teacher_settings(phone=phone, file=file)
        elif num == 3:
            self.change_user_admin('teacher', phone, file)
            self.teacher_settings(phone=phone, file=file)
        elif num == 4:
            self.change_birth_date_admin('teacher', phone, file)
            self.teacher_settings(phone=phone, file=file)
        elif num == 5:
            self.change_gmail_admin('teacher', phone, file)
            self.teacher_settings(phone=phone, file=file)
        else:
            self.teacher_settings(self.phone, file)
