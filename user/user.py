from Exam_4.context_manager import JsonManager, int_input


class User(JsonManager):
    def show_menu_user(self, phone: str) -> bool:
        print(phone)
        text = """
        choice number
        1. 
        """
        print(text)
        num = int_input("number: ")
        print(num)
        self.exit = True
        return self.exit
