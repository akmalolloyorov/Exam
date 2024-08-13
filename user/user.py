from Exam_4.user.payments import Payments, int_input


class User(Payments):
    def show_menu_user(self, phone: str, file: dict) -> bool:
        print("Hush kelibsiz...")
        self.home_page(phone=phone, file=file)
        text = """
        1. ⌂ Bosh sahifa
        2. To'lovlarim
        3. Guruhlarim
        4. Ko'rsatgichlarim
        5. Reyting
        6. Do'kon
        7. Sozlamalar
        8. Chiqish
        """
        print(text)
        num = int_input("Raqamni tanglang: ")
        if num == 1:
            self.show_menu_user(phone=phone, file=file)
        elif num == 2:
            self.payment(phone=phone, file=file)
            self.show_menu_user(phone=phone, file=file)
        elif num == 3:
            self.my_groups(phone=phone, file=file)
            self.show_menu_user(phone=phone, file=file)
        elif num == 4:
            self.my_pointers(phone=phone, file=file)
            self.show_menu_user(phone=phone, file=file)
        elif num == 5:
            self.my_rating(phone=phone, file=file)
            self.show_menu_user(phone=phone, file=file)
        elif num == 6:
            self.shop(phone=phone, file=file)
            self.show_menu_user(phone=phone, file=file)
        elif num == 7:
            self.personal_info(phone=phone, file=file)
            if self.exit:
                self.exit = False
                self.show_menu_user(phone=phone, file=file)
        else:
            self.exit = True
            return self.exit

    def my_groups(self, phone: str, file: dict) -> None:
        pass

    def my_pointers(self, phone: str, file: dict) -> None:
        pass

    def my_rating(self, phone: str, file: dict) -> None:
        pass

    def shop(self, phone: str, file: dict) -> None:
        pass
