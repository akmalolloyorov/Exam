from Exam_4.context_manager import JsonManager, int_input


class PersonalInfo(JsonManager):
    def personal_info(self, phone: str, file: dict) -> bool:
        text = """
        1. Raqamni o'zgartirish
        2. To'liq ismni o'zgartirish
        3. usernameni o'zgartirish
        4. parolni o'zgartirish
        5. tug'ilgan sanani o'zgartirish
        6. gmailni o'zgartirish
        7. genderni o'zgartirish
        8. Chiqish
        """
        print(text)
        num = int_input("Raqamni tanlang: ")
        if num == 1:
            self.change_phone(phone=phone, file=file)
            self.personal_info(phone, file)
        elif num == 2:
            self.change_full_name(phone=phone, file=file)
            self.personal_info(phone, file)
        elif num == 3:
            self.change_username(phone=phone, file=file)
            self.personal_info(phone, file)
        elif num == 4:
            self.change_password(phone=phone, file=file)
            self.personal_info(phone, file)
        elif num == 5:
            self.change_birth_date(phone=phone, file=file)
            self.personal_info(phone, file)
        elif num == 6:
            self.change_gmail(phone=phone, file=file)
            self.personal_info(phone, file)
        elif num == 6:
            self.change_gender(phone=phone, file=file)
            self.personal_info(phone, file)
        else:
            self.exit = True
            return self.exit

    def change_phone(self, phone: str, file: dict) -> None:
        pass

    def change_full_name(self, phone: str, file: dict) -> None:
        pass

    def change_username(self, phone: str, file: dict) -> None:
        pass

    def change_password(self, phone: str, file: dict) -> None:
        pass

    def change_birth_date(self, phone: str, file: dict) -> None:
        pass

    def change_gmail(self, phone: str, file: dict) -> None:
        pass

    def change_gender(self, phone: str, file: dict) -> None:
        pass
