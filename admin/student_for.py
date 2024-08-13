from Exam_4.admin.personal_admin import PersonalAdmin, int_input
import hashlib
import random


class StudentFor(PersonalAdmin):
    def choice_user(self, file: dict):
        full_name_list: list = []
        phone_list: list = []
        for phone, p_value in file['student'].items():
            full_name_list.append(p_value["full_name"])
            phone_list.append(phone)
        full_name = self.list_choice(full_name_list)
        name_index = full_name_list.index(full_name)
        return phone_list[name_index]

    def student_for(self, file: dict) -> bool:
        phone = self.choice_user(file)
        text = """
        1. Teleforn raqamini o'zgartirish
        2. To'liq ismini o'zgartirish
        3. Usernameni o'zgartirish
        4. Parolini o'agartirish
        5. Tug'ilgan kunini o'zgartirish
        6. Gmailni o'zgartirish
        7. hisobini to'ldirish
        8. To'lovlarini ko'rish
        9. Natijalarini ko'rish
        10. Guruhlarin ko'rish
        11. Studentni o'chirish
        12. Studentni guruhga qo'shish
        13. Studentni ballini o'zgartirish
        14. Exit
        """
        print(text)
        num = int_input("Raqam tanlang: ")
        if num == 1:
            self.change_phone(phone, file)
            self.student_for(file)
        elif num == 2:
            self.change_full_name(phone, file)
            self.student_for(file)
        elif num == 3:
            self.change_username(phone, file)
            self.student_for(file)
        elif num == 4:
            self.change_password(phone, file)
            self.student_for(file)
        elif num == 5:
            self.change_birth_date(phone, file)
            self.student_for(file)
        elif num == 6:
            self.change_gmail(phone, file)
            self.student_for(file)
        elif num == 7:
            self.paid(phone, file)
            self.student_for(file)
        elif num == 8:
            self.my_payments(phone, file)
            self.student_for(file)
        elif num == 9:
            self.my_pointers(phone, file)
            self.student_for(file)
        elif num == 10:
            self.my_groups(phone, file)
            self.student_for(file)
        elif num == 11:
            self.delete_student(phone, file)
            self.student_for(file)
        elif num == 12:
            self.add_student_in_group(phone, file)
            self.student_for(file)
        elif num == 13:
            self.change_student_ball(phone, file)
            self.student_for(file)
        else:
            self.exit = True
            return self.exit

    def add_student(self, file: dict) -> None:
        phone = self.phone_input("Telefon raqam kriting: ")
        full_name = input("To'liq ismingizni kriting: ").title()
        username_list: list = []
        for i in file.values():
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
        file['student'].update(user)
        self.add_to_file(self.users_file, file)
        print(f"Ro'yhatdan qo'shildi, student username: {num}")

    def delete_student(self, phone: str, file: dict) -> None:
        del file['student'][phone]
        self.write_to_file(self.users_file, file)
        print("Student o'chirildi")

    def add_student_in_group(self, phone: str, file: dict) -> None:
        pass

    def change_student_ball(self, phone: str, file: dict) -> None:
        pass
