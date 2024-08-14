from Exam_4.user.user import User, int_input
import hashlib
import random


class StudentFor(User):
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

    def choice_group(self, group_file: dict, phone: str) -> str:
        group_list: list = []
        for group, value in group_file.items():
            for num in value['students'].keys():
                if num == phone:
                    pass
                else:
                    group_list.append(group)
        group_set = set(group_list)
        group_list = list(group_set)
        if len(group_list) > 0:
            group: str = self.list_choice(group_list)
            return group
        else:
            return "none"

    def add_student_in_group(self, phone: str, file: dict) -> None:
        groups: dict = self.read_to_file(self.groups_file)
        group = self.choice_group(groups, phone)
        if group == "none":
            print("Guruh topilmadi")
            return
        else:
            groups[group]['students'].update({phone: 0})
            user = {
                group: {
                    "direction": groups[group]['direction'],
                    "status": True,
                    "lessons": {}
                }
            }
            file['student'][phone]['groups'].update(user)
            self.write_to_file(self.groups_file, groups)
            self.write_to_file(self.users_file, file)
            print(f"{group}-guruhiga qo'shildi.")

    def choice_teacher(self, group: str, teacher_file: dict) -> str:
        self.__str__()
        for phone_teacher, value in teacher_file['teacher'].items():
            for i in value['groups'].keys():
                if i == group:
                    return phone_teacher

    def change_student_ball(self, phone: str, file: dict) -> None:
        group_list = []
        lesson_list = []
        if len(file['student'][phone]['groups']) > 0:
            for group in file['student'][phone]['groups'].keys():
                group_list.append(group)
            group: str = self.list_choice(group_list)
            if len(file['student'][phone]['groups'][group]['lessons'].keys()) > 0:
                for lesson in file['student'][phone]['groups'][group]['lessons'].keys():
                    lesson_list.append(lesson)
                lesson: str = self.list_choice(lesson_list)
                print(f"oldingi ball: {file['student'][phone]['groups'][group]['lessons'][lesson]['grade']}")
                old_ball = file['student'][phone]['groups'][group]['lessons'][lesson]['grade']
                xp = file['student'][phone]['my_results']['xp']
                old_xp, old_silver = self.xp_for(old_ball, self.find_level(xp))
                ball = int_input("Ball kriting: ")
                while ball < 0 or ball > 100:
                    print("ball 0 dan 100 gacha bo'lishi kerak qaytadan kriting: ")
                    ball = int_input("Ball kriting: ")
                file['student'][phone]['groups'][group]['lessons'][lesson]['grade'] = ball
                e_xp, e_silver = self.xp_for(ball, self.find_level(xp))
                print(e_silver)
                file['student'][phone]['my_results']['xp'] += e_xp - old_xp
                file['student'][phone]['my_results']['silver'] += e_silver - old_silver
                file['student'][phone]['my_results']['be_homework'][0] += e_xp - old_xp
                file['student'][phone]['my_results']['be_homework'][1] += e_silver - old_silver
                teacher = self.choice_teacher(group, file)
                file['teacher'][teacher]['groups'][group]['lessons'][lesson]['student'][phone]['grade'] = ball

                self.write_to_file(self.users_file, file)
                print(f"Ball o'zgartirildi.")
            else:
                print("Siz hali dars bo'lmagan")
        else:
            print("Sizda guruh yo'q.")

    def find_level(self, xp: int) -> int:

        self.__str__()
        level = 0
        if 0 <= xp < 200:
            level = 0
        elif 200 <= xp < 450:
            level = 1
        elif 450 <= xp < 750:
            level = 2
        elif 700 <= xp < 950:
            level = 3
        elif 950 <= xp <= 1250:
            level = 4
        elif 1250 <= xp <= 20000:
            level = 5
        return level

    def xp_l(self, level: int, xp: int) -> int:
        self.__str__()
        silver = 0
        if level == 0:
            silver = xp * 4
        elif level == 1:
            silver = xp * 5
        elif level == 2:
            silver = xp * 6
        elif level == 3:
            silver = xp * 7
        elif level == 4:
            silver = xp * 8
        elif level == 5:
            silver = xp * 9
        return silver

    def xp_for(self, ball: int, level: int):
        self.__str__()
        xp = 0
        silver = 0
        if 0 < ball <= 50:
            xp = 0
        elif 50 < ball <= 74:
            xp = 4
        elif 74 < ball <= 84:
            xp = 6
        elif 84 < ball <= 94:
            xp = 8
        elif 94 < ball <= 100:
            xp = 10
        if level == 0:
            silver = xp * 4
        elif level == 1:
            silver = xp * 5
        elif level == 2:
            silver = xp * 6
        elif level == 3:
            silver = xp * 7
        elif level == 4:
            silver = xp * 8
        elif level == 5:
            silver = xp * 9
        return xp, silver
