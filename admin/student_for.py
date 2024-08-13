from Exam_4.admin.personal_admin import PersonalAdmin, int_input


class StudentFor(PersonalAdmin):
    def student_for(self, file: dict) -> bool:
        full_name_list: list = []
        phone_list: list = []
        for phone, p_value in file['student'].items():
            full_name_list.append(p_value["full_name"])
            phone_list.append(phone)
        full_name = self.list_choice(full_name_list)
        name_index = full_name_list.index(full_name)
        phone = phone_list[name_index]
        text = """
        1. Teleforn raqamini o'zgartirish
        2. To'liq ismini o'zgartirish
        3. Parolini o'agartirish
        4. Tug'ilgan kunini o'zgartirish
        5. Gmailni o'zgartirish
        6. hisobini to'ldirish
        7. To'lovlarini ko'rish
        8. Natijalarini ko'rish
        9. Exit
        """
        print(text)
        num = int_input("Raqam tanlang: ")
        if num == 1:
            pass
        elif num == 2:
            pass
        elif num == 3:
            pass
        elif num == 4:
            pass
        elif num == 5:
            pass
        elif num == 6:
            pass
        elif num == 7:
            pass
        elif num == 8:
            pass
        else:
            self.exit = True
            return self.exit
