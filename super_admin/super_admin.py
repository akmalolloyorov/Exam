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
        pass

    def delete_admin(self, file):
        pass

    def check_phone(self, file):
        pass
