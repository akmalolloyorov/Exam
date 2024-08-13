import hashlib
import random

from Exam_4.admin.admin import Admin, int_input


class Main(Admin):
    def __init__(self):
        super().__init__()

    def show_menu(self) -> None:
        text = """
        choice number
        1. Login
        2. Register
        3. Exit
        """
        print(text)
        num = int_input("number: ")
        if num == 1:
            self.login()
        elif num == 2:
            self.register()
        else:
            print("The end...")

    def login(self) -> None:
        user_file: dict = self.read_to_file(self.users_file)
        username: str = input("Username: ").lower().strip()
        password: str = input("Password: ")
        p = hashlib.sha256(password.encode("utf-8")).hexdigest()
        for i, j in user_file.items():
            for phone, k in j.values:
                if k["username"] == username and k['password'] == p:
                    if i == "student":
                        self.show_menu_user(phone=phone, file=user_file)
                        if self.exit:
                            self.exit = False
                            return self.show_menu()

                    elif i == "teacher":
                        self.show_menu_teacher(phone=phone)
                        if self.exit:
                            self.exit = False
                            return self.show_menu()
                    elif i == "admin":
                        self.show_menu_admin(phone=phone)
                        if self.exit:
                            self.exit = False
                            return self.show_menu()
        print("incorrect password or username. try again later.")
        self.show_menu()

    def register(self) -> None:
        users_file: dict = self.read_to_file(self.users_file)
        phone = self.phone_input("Enter your phone number: ")
        full_name = input("Enter full name: ").title()
        username_list: list = []
        for i in users_file.values():
            for j in i.values():
                username_list.append(j['username'])

        num = random.randint(100000, 999999)
        while num in username_list:
            num = random.randint(100000, 999999)

        password = input("Enter password: ")
        birthday = self.birth_input("Enter birth")
        gmail = input("Enter gmail: ")
        while "@gmail.com" not in gmail:
            gmail = input("Enter gmail: ")
        p = hashlib.sha256(password.encode("utf-8")).hexdigest()
        gender_list = ['male', 'female']
        gender = self.list_choice(gender_list)

        user = {
            f"+998{phone}": {
                "full_name": full_name,
                "username": num,
                "password": p,
                "birthday": birthday,
                "gmail": gmail,
                "gender": gender,
                "balance": 0,
                "my_payments": [],
                "my_result": {
                    "xp": 0,
                    "silver": 0,
                    "be_lesson": [0, 0],
                    "be_homework": [0, 0],
                    "exam": 0
                },
                "sms": [],
                "massage": [],
                "groups": {}

            }
        }
        users_file['student'].update(user)
        self.add_to_file(self.users_file, users_file)
        print("Registration successful")
        self.show_menu_user(phone=f"+998{phone}", file=users_file)
        if self.exit:
            self.exit = False
            return self.show_menu()


main = Main()
main.show_menu()
