from context_manager import CustomOpen, int_input


class Main:
    def __init__(self):
        pass

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
        pass
