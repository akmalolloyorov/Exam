import hashlib

from Exam_4.admin.admin import Admin, int_input


class SupperAdmin(Admin):
    def show_menu_supper_admin(self, file: dict) -> bool:
        text = """
        1. Admin qo'shmoq
        2. Admin o'chiqmoq
        """
        print(text)
        num = int_input("Raqam tanlang: ")
        if num == 1:
            self.add_admin(file)
            self.show_menu_supper_admin(file)
        elif num == 2:
            self.delete_admin(file)
            self.show_menu_supper_admin(file)
        else:
            self.exit = True
            return self.exit

    def add_admin(self, file):
        name = input("To'liq ismini kriting: ")
        phone = self.check_phone(file)
        username = self.user_input(file)
        password = input("Password: ")
        p = hashlib.sha256(password.encode("utf-8")).hexdigest()
        birthday = self.birth_input("Tug'ilgan sanasini kriting: ")
        email = input("Gmailini kriting: ")
        while "@gmail.com" not in email:
            print("Tog'ri farmatda kriting")
            email = input("Gmailini kriting: ")
        gender = self.list_choice(['male', 'female'])
        user = {
            phone: {
                "full_name": name,
                "username": username,
                "password": p,
                "birthday": birthday,
                "gmail": email,
                "gender": gender,
            }
        }
        file.update(user)
        self.write_to_file(self.users_file, user)

    def delete_admin(self, file):
        admin_name_list = []
        admin_user_list = []
        for i, j in file['admin'].items():
            admin_user_list.append(i)
            admin_name_list.append(j['full_name'])
        admin_name = self.list_choice(admin_name_list)
        admin_index = admin_name_list.index(admin_name)
        admin_user = admin_user_list[admin_index]
        del file['admin'][admin_user]
        self.write_to_file(self.users_file, file)
        print("Admin o'chirildi.")

    def check_phone(self, file):
        phone_list = []
        self.__str__()
        for i in file.values():
            for j in i.keys():
                phone_list.append(j)
        phone = self.phone_input("Telefon raqam kriting: ")
        while phone not in phone_list:
            print("Ushbu raqam mavjud")
            phone = self.phone_input("Telefon raqam kriting: ")
        return phone
