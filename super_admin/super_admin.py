from Exam_4.admin.admin import Admin, int_input


class SupperAdmin(Admin):
    def show_menu_supper_admin(self) -> bool:
        print("\nSuper Admin Menu:")
        self.exit = True
        return self.exit
