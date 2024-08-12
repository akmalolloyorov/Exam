import hashlib

from context_manager import JsonManager, int_input


class Main(JsonManager):
    def __init__(self):
        super().__init__()

    def show_menu(self):
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

    def login(self):
        pass

    def register(self):
        full_name = input("Enter full name: ").title()
        phone = self.phone_input("Enter your phone number: ")
        username = input("Enter username: ")
        password = input("Enter password: ")
        p = hashlib.sha256(password.encode("utf-8")).hexdigest()
        gender_list = ['male', 'female']
        gender = self.list_choice(gender_list)

        u = {
            f"+998{phone}": {
                "full_name": full_name,
                "username": username,
                "password": p,
                "gender": gender,
                "balance": 0,

            }
        }


main = Main()
user = {
    f"+998{952203465}": {
        "full_name": "Yo'ldashev Temur",
        "username": "tima",
        "password": "f",
        "birthday": "08.10.2024",
        "gmail": "tima@gmail.com",
        "gender": 'male',
        "balance": 1000000,
        "my_result": {
            "xp": 30,
            "silver": 120,
            "be_lesson": [6, 24],
            "be_homework": [24, 96],
            "Exam": 0
        },
        "sms": [
            "darsga qatnashganingiz uchun 2 xp berildi",
            "uyga vasifa bajarganingiz uchun 8 xp berild",
            "darsga qatnashganingiz uchun 2 xp berildi",
            "uyga vasifa bajarganingiz uchun 8 xp berild",
            "darsga qatnashganingiz uchun 2 xp berildi",
            "uyga vasifa bajarganingiz uchun 8 xp berild",
        ],
        "massages": [],
        "groups": {
            "n50": {
                "direction": "python django, (backend)",
                "status": True,
                "lessons": {
                    "if, else, elif": {
                        "lesson_date": "10.08.2024",
                        "start_time": "16:00",
                        "end_time": "18:00",
                        "grade": 94,
                        "attendance": True,
                        "month": 1
                    },
                    "for, while": {
                        "lesson_date": "12.08.2024",
                        "start_time": "16:00",
                        "end_time": "18:00",
                        "grade": 94,
                        "attendance": True,
                        "month": 1
                    }
                }
            }
        }
    }
}
users = {
    "student": {},
    "teacher": {},
    "admin": {}
}
users['student'].update(user)
group = {
    "n50": {
        "direction": "python django, (backend)",
        "teachers": ["+998931113565"],
        "students": ["+998952203465"],
        "course_price": 1350000,
        "term": 8
    }
}
teacher = {
    f"+998{931113565}": {
        "full_name": "Masharipov Nodirbek",
        "username": "nodirbek",
        "password": "5",
        "birthday": "11.10.2003",
        "gmail": "masharipov@gmail.com",
        "gender": "male",
        "groups": ['n50'],
        "students": ['+998952203465'],
        "sms": [],
        "massages": {},

    }
}
admin = {
    "+998972203565": {
        "full_name": "Akmal Olloyorov",
        "username": "akmalbek",
        "password": "5",
        "birthday": "16.12.2004",
        "gmail": "proaktiv64@gamil.com",
        "gender": "male",
    }
}

users['teacher'].update(teacher)
users['admin'].update(admin)

main.add_to_file(main.users_file, users)
main.add_to_file(main.groups_file, group)
