from Exam_4.admin.teacher_for import TeacherFor, int_input


class Admin(TeacherFor):
    def show_menu_admin(self, phone: str, file: dict) -> bool:
        text = """
        1. Sozlamalar
        2. Student uchun
        3. Ustoz uchun
        4. Student qo'shish
        5. Guruh qo'shish
        6. Guruh o'chirish
        7. Chiqish
        """
        print(text)
        num = int_input("Raqam tanlang: ")
        if num == 2:
            self.student_for(file=file)
            if self.exit:
                self.exit = False
                self.show_menu_admin(phone, file)
        elif num == 3:
            self.teacher_for(file)
            if self.exit:
                self.exit = False
                self.show_menu_admin(phone, file)
        elif num == 1:
            self.personal_admin(phone, file)
            if self.exit:
                self.exit = False
                self.show_menu_admin(self.phone, file)
        elif num == 4:
            self.add_student(file)
            self.show_menu_admin(phone, file)
        elif num == 5:
            self.add_group()
            self.show_menu_admin(phone, file)
        elif num == 6:
            self.delete_group(file)
            self.show_menu_admin(phone, file)
        else:
            self.exit = True
            return self.exit

    def add_group(self) -> None:
        groups: dict = self.read_to_file(self.groups_file)
        group_name_list = [x for x in groups.keys()]
        group_name = input("Guruh nomi: ").lower().strip()
        while group_name in group_name_list:
            group_name = input("Bu nomli guruh mavjud. boshqa nom bering: ").lower().strip()
        group_d = input("Guruh nima o'tiladi: ")
        term = int_input("Kurs necha oy bo'ladi: ")
        group = {
            group_name: {
                "direction": group_d,
                "teachers": "none",
                "students": {},
                "course_price": {},
                "term": term
            }
        }
        groups.update(group)
        self.write_to_file(self.groups_file, groups)
        print("Guruh qo'shildi")

    def delete_group(self, file: dict) -> None:
        groups: dict = self.read_to_file(self.groups_file)
        group = self.find_group(groups)
        if group != "none":
            for teacher, value in file['teacher'].items():
                try:
                    for gr in value['groups'].keys():
                        if gr == group:
                            del file['teacher'][teacher]['groups'][gr]

                except KeyError:
                    pass
            for student, value in file['student'].items():
                try:
                    for gr in value['groups'].keys():
                        if gr == group:
                            del file['student'][student]['groups'][gr]

                except KeyError:
                    pass
            del groups[group]
            self.write_to_file(self.groups_file, groups)
            self.write_to_file(self.users_file, file)
        else:
            print("guruhlar yo'q.")
