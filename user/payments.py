from Exam_4.user.Home import HomePage, int_input


class Payments(HomePage):
    def payment(self, phone: str, file: dict) -> bool:
        text = """
        1. To'lovlarim
        2. To'lov qilish card
        3. Chiqish
        """
        print(text)
        num = int_input("Raqam tanlang: ")
        if num == 2:
            self.paid(phone, file)
            self.payment(phone, file)
        elif num == 1:
            self.my_payments(phone, file)
            self.payment(phone, file)
        else:
            self.exit = True
            return self.exit

    def paid(self, phone: str, file: dict) -> None:
        money = file["student"][phone]['balance']
        print(f"Hisobingizda {money}-sum bor")
        new_money = int_input("Pul miqdorini kriting: ")
        while new_money < 0:
            print("Xato kritdingiz qaytadan kriting.")
            new_money = int_input("Pul miqdorini kriting: ")
        file["student"][phone]['balance'] += new_money
        self.write_to_file(self.users_file, file)
        print("To'lov qilindi!")

    def my_payments(self, phone: str, file: dict) -> None:
        for j, i in file["student"][phone]["my_payments"].items():
            print(f"{j}.Money: {i['money']}, Date: {i['date']}, Type: {i['type']}")
        self.__str__()

