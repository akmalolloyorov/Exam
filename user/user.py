from Exam_4.user.personal_information import PersonalInfo, int_input


class User(PersonalInfo):
    def show_menu_user(self, phone: str) -> bool:
        text = """
        1. Bosh sahifa
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
            self.home_page(phone=phone)
            self.show_menu_user(phone=phone)
        elif num == 2:
            self.my_payments(phone=phone)
            self.show_menu_user(phone=phone)
        elif num == 3:
            self.my_groups(phone=phone)
            self.show_menu_user(phone=phone)
        elif num == 4:
            self.my_pointers(phone=phone)
            self.show_menu_user(phone=phone)
        elif num == 5:
            self.my_rating(phone=phone)
            self.show_menu_user(phone=phone)
        elif num == 6:
            self.shop(phone=phone)
            self.show_menu_user(phone=phone)
        elif num == 7:
            self.personal_info(phone=phone)
            if self.exit:
                self.exit = False
                self.show_menu_user(phone=phone)
        else:
            self.exit = True
            return self.exit

    def home_page(self, phone: str) -> None:
        pass

    def my_payments(self, phone: str) -> None:
        pass

    def my_groups(self, phone: str) -> None:
        pass

    def my_pointers(self, phone: str) -> None:
        pass

    def my_rating(self, phone: str) -> None:
        pass

    def shop(self, phone: str) -> None:
        pass
