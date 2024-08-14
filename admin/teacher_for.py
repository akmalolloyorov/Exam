import json

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
            3. Teacher qo'shish
            4. Teacher o'chirish
            5. Chiqish
            """
            print(text)
            num = int_input("Raqam tanlang: ")
            if num == 1:
                self.teacher_about(phone=phone, file=file)
                self.teacher_for(file)
            elif num == 2:
                self.teacher_settings(phone=self.phone, file=file)
                self.teacher_for(file)
            elif num == 3:
                self.add_teacher(file)
                self.teacher_for(file)
            elif num == 4:
                self.delete_teacher(phone=phone, file=file)
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
        group_name_list: list = []
        group_user_list: list = []
        group_file: dict = self.read_to_file(self.groups_file)
        if len(file['teacher'][phone]['groups']) > 0:
            for group, value in file['teacher'][phone]['groups'].items():
                group_name_list.append(value['direction'])
                group_user_list.append(group)
            group_name: str = self.list_choice(group_name_list)
            group_index: int = group_name_list.index(group_name)
            group_user: str = group_user_list[group_index]
            print("Studentlar:")
            for user in group_file[group_user]['students'].keys():
                print(file['student'][user]['full_name'])
        else:
            print("Guruhlar yo'q")

    def view_teacher_groups(self, phone: str, file: dict) -> None:
        group_name_list: list = []
        self.__str__()
        if len(file['teacher'][phone]['groups']) > 0:
            for group, value in file['teacher'][phone]['groups'].items():
                group_name_list.append(value['direction'])
            print(f"Guruhlar:, {json.dumps(group_name_list, indent=4)}")
        else:
            print("Guruhlar yo'q")

    def view_teacher_name(self, phone: str, file: dict) -> None:
        name: str = file['teacher'][phone]['full_name']
        print(f"To'liq ismi: {name}")
        self.__str__()

    def view_teacher_gmail(self, phone: str, file: dict) -> None:
        gmail: str = file['teacher'][phone]['gmail']
        print(f"Gmail: {gmail}")
        self.__str__()

    def view_teacher_birthday(self, phone: str, file: dict) -> None:
        birth = file['teacher'][phone]['birthday']
        print(f"Tug'ilgan sanasi: {birth}")
        self.__str__()

    def view_teacher_gender(self, phone: str, file: dict) -> None:
        gender: str = file['teacher'][phone]['gender']
        print(f"Jins: {gender}")
        self.__str__()

    def view_teacher_user_name(self, phone, file: dict) -> None:
        name: str = file['teacher'][phone]['username']
        print(f"username: {name}")
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

    def add_teacher(self, file: dict) -> None:
        pass

    def delete_teacher(self, phone: str, file: dict) -> None:
        pass
