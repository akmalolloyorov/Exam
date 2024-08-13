import hashlib

from Exam_4.context_manager import JsonManager, int_input


class PersonalInfo(JsonManager):
    def __init__(self):
        super().__init__()
        self.phone = None

    def personal_info(self, phone: str, file: dict) -> bool:
        self.phone = phone
        text = """
        1. Raqamni o'zgartirish
        2. To'liq ismni o'zgartirish
        3. usernameni o'zgartirish
        4. parolni o'zgartirish
        5. tug'ilgan sanani o'zgartirish
        6. gmailni o'zgartirish
        7. Chiqish
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
        else:
            self.exit = True
            return self.exit

    def change_phone(self, phone: str, file: dict) -> None:
        print(f"Sizning telefon raqamingiz: {phone}")
        new_phone = self.phone_input("Yangi telefon no'mer kriting: ")
        user = {new_phone: file['student'][phone]}
        file['student'].update(user)
        del file['student'][phone]
        self.write_to_file(self.users_file, file)
        self.phone = new_phone

    def change_full_name(self, phone: str, file: dict) -> None:
        new_full_name = input("Yangi to'liq ismingizni kriting: ").title()
        file['student'][phone]['full_name'] = new_full_name
        self.write_to_file(self.users_file, file)

    def change_username(self, phone: str, file: dict) -> None:
        print(f"Sizning usenamegiz :{file['student'][phone]['username']}")
        new_username = input("Yangi usernameni kriting: ").lower().strip()
        for i in file['student'].values():
            if new_username in i['username']:
                new_username = input('Bu username allaqadagi. Ushbu usernameni qayta kiriting: ')
        file['student'][phone]['username'] = new_username
        self.write_to_file(self.users_file, file)

    def change_password(self, phone: str, file: dict) -> None:
        password = input('Parolni kriting: ')
        p = hashlib.sha256(password.encode('utf8')).hexdigest()
        if file['student'][phone]['password'] == p:
            new_password = input("Yangi parol kriting: ")
            new_p = hashlib.sha256(new_password.encode('utf8')).hexdigest()
            file['student'][phone]['password'] = new_p
            self.write_to_file(self.users_file, file)
        else:
            print("Parolni nato'g'ri kritdingiz.")

    def change_birth_date(self, phone: str, file: dict) -> None:
        print(f"Hozirgil tug'ilgan sana: {file['student'][phone]['birthday']}")
        new_birthday = self.birth_input("Yangi tug'ilgan sana kriting: ")
        file['student'][phone]['birthday'] = new_birthday
        self.write_to_file(self.users_file, file)

    def change_gmail(self, phone: str, file: dict) -> None:
        print(f"Sizning gmailingiz {file['student'][phone]['gmail']}")
        new_gmail = input("Yangi gmail kriting: ").lower().strip()
        while "@gmail.com" not in new_gmail:
            new_gmail = input("Gmailning formati notog'ri. Ushbu gmailni qayta kiriting: ").lower().strip()
        file['student'][phone]['gmail'] = new_gmail
        self.write_to_file(self.users_file, file)
