import hashlib
from Exam_4.user.user import User, int_input


class PersonalAdmin(User):
    def personal_admin(self, phone: str, file: dict) -> bool:
        self.phone = phone
        text = """
        1. Telefon raqamni o'zgartirish
        2. username ni o'zgartirish
        3. Parolni o'zgartirish
        4. Tug'ilgan sanani o'zgartirish
        5. Gmailni o'zgartirish
        6. Chiqish
        """
        print(text)
        num = int_input("Raqamni tanlang: ")
        if num == 1:
            self.change_phone_admin('admin', phone, file)
            self.personal_admin(self.phone, file)
        elif num == 2:
            self.change_user_admin("admin", phone, file)
            self.personal_admin(phone, file)
        elif num == 3:
            self.change_password_admin("admin", phone, file)
            self.personal_admin(phone, file)
        elif num == 4:
            self.change_birth_date_admin("admin", phone, file)
            self.personal_admin(phone, file)
        elif num == 5:
            self.change_gmail_admin("admin", phone, file)
            self.personal_admin(phone, file)
        else:
            self.exit = True
            return self.exit

    def change_phone_admin(self, type_: str, phone: str, file: dict) -> None:
        print(f"Amaldagi telefon raqamingiz: {phone}")
        new_phone = self.phone_input("Yangi teleforn raqam kriting: ")
        while new_phone in file['admin'] or new_phone in file['student'] or new_phone in file['teacher']:
            print("Bu raqam allaqachon mavjud. Iltimos yangi raqam kriting!")
            new_phone = self.phone_input("Yangi telefonn raqam kriting: ")
        user = {new_phone: file[type_][phone]}
        del file[type_][phone]
        file[type_].update(user)
        print("Teleforn raqamingiz o'zgartirildi.")
        self.write_to_file(self.users_file, file)
        self.phone = new_phone

    def change_user_admin(self, type_: str, phone: str, file: dict) -> None:
        user_list: list = []
        for i, j in file.items():
            for k in j.values():
                user_list.append(k['username'])
        print(f"Sizning usernamegiz: {file[type_][phone]['username']}")
        new_user = input("Yangi username kriting: ")
        while new_user in user_list:
            print("Bu username allaqachon mavjud. Iltimos yangi username kriting!")
            new_user = input("Yangi username kriting: ")
        file[type_][phone]['username'] = new_user
        self.write_to_file(self.users_file, file)
        print("Usernameingiz o'zgartirildi.")

    def change_password_admin(self, type_: str, phone: str, file: dict) -> None:
        password = input('Parolni kriting: ')
        p = hashlib.sha256(password.encode("utf-8")).hexdigest()
        if file[type_][phone]['password'] == p:
            new_password = input("Yangi parol kriting: ")
            new_p = hashlib.sha256(new_password.encode("utf-8")).hexdigest()
            file[type_][phone]['password'] = new_p
            self.write_to_file(self.users_file, file)
            print("Parolingiz o'zgartirildi.")
        else:
            print("Natog'ri kritdingiz: ")

    def change_birth_date_admin(self, type_: str, phone: str, file: dict) -> None:
        print(f"Sizning tug'ilgan kunigiz: {file[type_][phone]['birthday']}")
        new_birthday = self.birth_input("Tug'ilgan kunigizni yangilang: ")
        file[type_][phone]['birthday'] = new_birthday
        self.write_to_file(self.users_file, file)
        print("Tug'ilgan kuningiz o'zgartirildi.")

    def change_gmail_admin(self, type_: str, phone: str, file: dict) -> None:
        print(f"Sizning gmail: {file[type_][phone]['gmail']}")
        new_gmail = input("Yangi gmail kriting: ")
        while "@gmail.com" not in new_gmail:
            print("Bu gmail formatida emas. Iltimos @gmail.com formatiga ko'rsatgan gmail kriting!")
            new_gmail = input("Yangi gmail kriting: ")
        file[type_][phone]['gmail'] = new_gmail
        self.write_to_file(self.users_file, file)
        print("Gmailingiz o'zgartirildi.")
