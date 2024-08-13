from Exam_4.user.payments import Payments, int_input


class User(Payments):
    def show_menu_user(self, phone: str, file: dict) -> bool:
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
            if self.exit:
                self.exit = False
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
            print("Tez orada qo'shiladi")
            self.show_menu_user(phone=phone, file=file)
        elif num == 7:
            self.personal_info(phone=phone, file=file)
            if self.exit:
                self.exit = False
                self.show_menu_user(phone=self.phone, file=file)
        else:
            self.exit = True
            return self.exit

    def my_groups(self, phone: str, file: dict) -> None:
        group_a_list: list = []
        group_b_list: list = []
        active = self.list_choice(["Faol", "Tugagan"])

        if len(file['student'][phone]['groups']):
            try:
                for group, ac in file['student'][phone]['groups'].items():
                    if ac['status']:
                        group_a_list.append(group)
                    else:
                        group_b_list.append(group)
                if active == "Faol":
                    if len(group_a_list) < 1:
                        return print("Sizda faol guruh yo'q")
                    group = self.list_choice(group_a_list)
                else:
                    if len(group_b_list) < 1:
                        return print("Sizda tugagan guruh yo'q")
                    group = self.list_choice(group_b_list)
                print(group)
                lesson_list = []
                for lesson in file['student'][phone]['groups'][group]['lessons'].keys():
                    lesson_list.append(lesson)
                lesson = self.list_choice(lesson_list)
                if file['student'][phone]['groups'][group]['lessons'][lesson]['grade'] == "None":
                    grade = "ball qo'yilmagan"
                else:
                    grade = file['student'][phone]['groups'][group]['lessons'][lesson]['grade']
                text = f"""
        Dars sanasi: {file['student'][phone]['groups'][group]['lessons'][lesson]['lesson_date']}
        boshlash vaqti: {file['student'][phone]['groups'][group]['lessons'][lesson]['start_time']}
        Tugash vaqti: {file['student'][phone]['groups'][group]['lessons'][lesson]['end_time']},
        ball: {grade}
                """
                print(text)
            except KeyError:
                print(f"Sizda {active} guruh yo'q")
        else:
            print("Sizda guruh yo'q")

    def my_pointers(self, phone: str, file: dict) -> None:
        self.__str__()
        xp = file["student"][phone]['my_results']['xp']
        silver = file["student"][phone]['my_results']['silver']
        be_lesson_xp = file["student"][phone]['my_results']['be_lesson'][0]
        be_lesson_silver = file["student"][phone]['my_results']['be_lesson'][1]
        be_homework_xp = file['student'][phone]['my_results']['be_homework'][0]
        be_homework_silver = file['student'][phone]['my_results']['be_homework'][1]
        exam_xp = file["student"][phone]['my_results']['exam'][0]
        exam_silver = file["student"][phone]['my_results']['exam'][1]
        text = f"""
        Darsga ishtirok bo'yicha jami XP {be_lesson_xp}, Jami Kumush {be_lesson_silver}
        Uyga vazifa bo'yicha jami XP {be_homework_xp}, Jami Kumush {be_homework_silver}
        imtihon o'tish bo'yicha jami XP {exam_xp}, Jami Kumush {exam_silver}
        
            Jami yig'ilgan XP: {xp}
            Jami yig'ilgan Kumush: {silver}'
"""
        print(text)

    def my_rating(self, phone: str, file: dict) -> None:
        pass

    # def shop(self, phone: str, file: dict) -> None:
    #     print("Tez orada qo'shiladi")
