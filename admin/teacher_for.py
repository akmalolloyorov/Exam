import hashlib
import json

from Exam_4.teacher.teacher import Teacher, int_input


class TeacherFor(Teacher):
    def teacher_for(self, file: dict) -> bool:
        text = """
        1. Teacher haqida malumot
        2. Teacher sozlamalari 
        3. Teacher qo'shish
        5. Chiqish
        """
        print(text)
        num = int_input("Raqam tanlang: ")
        if num == 1:
            phone = self.choice_teacher_admin_for(file=file)
            if phone == "none":
                print("Hali teacher qo'shilmagan")
            else:
                self.teacher_about(phone=phone, file=file)
                self.teacher_for(file)
        elif num == 2:
            phone = self.choice_teacher_admin_for(file=file)
            if phone == "none":
                print("Hali teacher qo'shilmagan")
            else:
                self.teacher_settings(phone=self.phone, file=file)
                self.teacher_for(file)
        elif num == 3:
            self.add_teacher(file)
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
        6. Teacherni o'chirish
        7. Chiqish
        """
        print(text)
        num = int_input("Raqam tanlang: ")
        if num == 1:
            self.change_phone_admin('teacher', phone, file)
            groups: dict = self.read_to_file(self.groups_file)
            for group, value in groups.items():
                if value['teachers'] == phone:
                    try:
                        value['teachers'].remove(phone)
                        value['teachers'].append(self.phone)
                    except ValueError:
                        pass
                    except KeyError:
                        pass
                    except IndexError:
                        pass
            self.write_to_file(self.groups_file, groups)
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
        elif num == 6:
            self.delete_teacher(phone, file)
            self.teacher_settings(self.phone, file)
        else:
            self.teacher_for(file)

    def check_group(self, group: str, file: dict) -> bool:
        self.__str__()
        count = len(file[group]['teachers'])
        if count == 0:
            c = True
        else:
            c = False
        return c

    def add_teacher(self, file: dict) -> None:
        groups: dict = self.read_to_file(self.groups_file)
        group = self.find_group(groups)
        if group != "none":
            if self.check_group(group, file):
                direction = groups[group]['direction']
                name = input("To'liq ismini kriting: ").title()
                phone = self.phone_input("Telefon raqamini kriting: ")
                username = self.user_input(file)
                password = input("Password: ").title().strip()
                p = hashlib.sha256(password.encode("utf-8")).hexdigest()
                birthday = self.birth_input("Birthday: ")
                gmail = input("Gmail: ").lower().strip()
                while "@gmail.com" not in gmail:
                    gmail = input("Gmailni kerakli formatda kiriting: ").lower().strip()
                gender = self.list_choice(['male', 'female'])
                user = {
                    phone: {
                        "full_name": name,
                        "username": username,
                        "password": p,
                        "birthday": birthday,
                        "gmail": gmail,
                        "gender": gender,
                        "groups": {
                            group: {
                                "direction": direction,
                                "status": True,
                                "lessons": {}
                            }
                        }
                    }
                }
                file['teacher'].update(user)
                groups[group]['students'].append(phone)
                self.write_to_file(self.users_file, file)
                self.write_to_file(self.groups_file, groups)
            else:
                print('guruh band')
        else:
            print("Gruh yo'q.")

    def delete_teacher(self, phone: str, file: dict) -> None:
        group_file: dict = self.read_to_file(self.groups_file)
        group: str = self.choice_group('teachers', group_file, phone)
        group_file[group]['teachers'].remove(phone)
        del file['teacher'][phone]
        self.write_to_file(self.groups_file, group_file)
        self.write_to_file(self.users_file, file)
        print("O'chirildi")

    def find_group(self, file: dict) -> str:
        group_list: list = []
        if len(file) > 0:
            for group in file.keys():
                group_list.append(group)
            group: str = self.list_choice(group_list)
            return group
        else:
            return "none"

    def user_input(self, file: dict) -> str:
        self.__str__()
        user_list: list = []
        for i, j in file.items():
            for n, m in j.items():
                user_list.append(m['username'])
        username = input("Enter username: ").lower().strip()
        while username in user_list:
            username = input("Bu username band boshqasin kriting: ").lower().strip()
        return username
