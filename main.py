import hashlib
import random
from Exam_4.check_payment import check_time, stop_thread
from Exam_4.super_admin.super_admin import SupperAdmin, int_input


class Main(SupperAdmin):
    def __init__(self):
        super().__init__()
        self.true = False

    def show_menu(self) -> None:
        text = """
        Raqam tanlang
        1. Kirish
        2. Ro'yhatdan o'tish
        3. Chiqish
        """
        print(text)
        num = int_input("Raqam kriting: ")
        if num == 1:
            self.login()
        elif num == 2:
            self.register()
        elif num == 0000:
            file: dict = self.read_to_file(self.users_file)
            self.show_menu_supper_admin(file)
            if self.exit:
                self.exit = False
                return self.show_menu()
        else:
            print("Dastur tugadi...")

    def login(self) -> None:
        user_file: dict = self.read_to_file(self.users_file)
        username: str = input("Foydalanuvchi nomi: ").lower().strip()
        password: str = input("parol: ")
        p = hashlib.sha256(password.encode("utf-8")).hexdigest()
        for i, j in user_file.items():
            for phone, km in j.items():
                if km["username"] == username and km['password'] == p:
                    if i == "student":
                        self.show_menu_user(phone=phone, file=user_file)
                        if self.exit:
                            self.exit = False
                            return self.show_menu()

                    elif i == "teacher":
                        self.show_menu_teacher(phone=phone, file=user_file)
                        if self.exit:
                            self.exit = False
                            return self.show_menu()
                    elif i == "admin":
                        self.show_menu_admin(phone=phone, file=user_file)
                        if self.exit:
                            self.exit = False
                            return self.show_menu()
                    else:
                        print("Parol yoki foydalanuvchi nomi xato qaytadan urunib ko'ring.")
                        return self.show_menu()
                else:
                    self.true = True
        if self.true:
            print("Parol yoki foydalanuvchi nomi xato qaytadan urunib ko'ring.")
            self.true = False
            return self.show_menu()

    def register(self) -> None:
        users_file: dict = self.read_to_file(self.users_file)
        phone = self.phone_input("Telefon raqam kriting: ")
        full_name = input("To'liq ismingizni kriting: ").title()
        username_list: list = []
        for i in users_file.values():
            for j in i.values():
                username_list.append(j['username'])

        num = random.randint(100000, 999999)
        while num in username_list:
            num = random.randint(100000, 999999)

        password = input("Parol kriting: ")
        birthday = self.birth_input("tug'ilgan kuninglizni kriting: ")
        gmail = input("Gmailingizni kriting: ")
        while "@gmail.com" not in gmail:
            print("exp(proaktiv64@gmail.com)")
            gmail = input("Qaytadan kriting: ")
        p = hashlib.sha256(password.encode("utf-8")).hexdigest()
        gender_list = ['male', 'female']
        gender = self.list_choice(gender_list)

        user = {
            phone: {
                "full_name": full_name,
                "username": str(num),
                "password": p,
                "birthday": birthday,
                "gmail": gmail,
                "gender": gender,
                "balance": 0,
                "my_payments": [],
                "my_results": {
                    "xp": 0,
                    "silver": 0,
                    "be_lesson": [0, 0],
                    "be_homework": [0, 0],
                    "exam": [0, 0]
                },
                "sms": [],
                "massage": [],
                "groups": {}

            }
        }
        users_file['student'].update(user)
        self.add_to_file(self.users_file, users_file)
        print(f"Ro'yhatdan o'tdingiz sizning usernamegiz: {num}")
        self.show_menu_user(phone=phone, file=users_file)
        if self.exit:
            self.exit = False
            return self.show_menu()

    def file(self) -> dict:
        return self.read_to_file(self.users_file)


main = Main()
if __name__ == '__main__':
    file_ = main.file()
    check_time(file_)
    try:
        main.show_menu()
    finally:
        stop_thread()
