from Exam_4.teacher.personal_teacher import PersonalTeacher, int_input


class Teacher(PersonalTeacher):
    def show_menu_teacher(self, phone: str, file: dict) -> bool:
        text = """
        1. Dars o'tish
        2. Studentlarni baholash
        3. Student bahosin o'zgartirish
        4. Dars vaqtini ko'rish
        5. Sozlamalar
        6. Chiqish
        """
        print(text)
        num = int_input("Raqamni tanlang: ")
        if num == 1:
            self.lesson_for(phone, file)
            self.show_menu_teacher(phone, file)
        elif num == 2:
            self.rating_ball(phone, file)
            self.show_menu_teacher(phone, file)
        elif num == 3:
            self.change_rating(phone, file)
            self.show_menu_teacher(phone, file)
        elif num == 4:
            self.view_lesson_time(phone, file)
            self.show_menu_teacher(phone, file)
        elif num == 5:
            print("tez kunlarda.")
            self.show_menu_teacher(phone, file)
        else:
            self.exit = True
            return self.exit

    def lesson_for(self, phone: str, file: dict) -> None:
        group_file: dict = self.read_to_file(self.groups_file)
        group_list: list = []
        if len(file['teacher'][phone]['groups']) > 0:
            for group, value in file['teacher'][phone]['groups'].items():
                group_list.append(group)
            group: str = self.list_choice(group_list)

            students: list = self.choice_student(group, group_file)
            lesson_name = input('Dars nomini kriting: ')
            l_date = input("Dars sanasini kriting exp(10.08.2024): ")
            l_s = input("Dars boshlanish vaqtini kriting: exp(16:00): ")
            l_e = input("Dars tegash vaqtini kriting: exp(18:00): ")
            month = self.choice_month(phone, group, file)
            if month == "no":
                file['teacher'][phone]['groups'][group]['status'] = False
                for i in students:
                    file['student'][i]['groups'][group]['status'] = False
                self.write_to_file(self.users_file, file)
                print("Kurs tugatilgan")
            else:
                lesson_dict = {
                    lesson_name: {
                        "lesson_date": l_date,
                        "start_time": l_s,
                        "end_time": l_e,
                        "student": {},
                        "month": month
                    }
                }
                file['teacher'][phone]['groups'][group]['lessons'].update(lesson_dict)
                for i in students:
                    file['student'][i]['groups'][group]['lessons'].update({lesson_name: {}})
                    print(f"{file['student'][i]['full_name']} kelganmi:")
                    choice = self.list_choice(['ha', "yo'q"])
                    xp = file['student'][i]['my_results']['xp']
                    if choice == "ha":
                        group_file[group]['students'][i] += 2
                        active = True
                        ball = 'ball'
                        sms = "darsga qatnashganingiz uchun 2 xp berildi"
                        file['student'][i]['sms'].append(sms)
                        file['student'][i]['my_results']['xp'] += 2
                        file['student'][i]['my_results']['silver'] += self.xp_l(self.find_level(xp), 1)
                        file['student'][i]['my_results']['be_lesson'][0] += 2
                        file['student'][i]['my_results']['be_lesson'][1] += self.xp_l(self.find_level(xp), 1)
                    else:
                        ball = 0
                        active = False
                    user = {i: {
                        "lesson_date": l_date,
                        "start_time": l_s,
                        "end_time": l_e,
                        "grade": ball,
                        "attendees": active,
                        'month': month
                    }}
                    file['student'][i]['groups'][group]['lessons'][lesson_name].update(user)
                    file['teacher'][phone]['groups'][group]['lessons'][lesson_name]['student'].update(user)
                    self.write_to_file(self.users_file, file)
                    self.write_to_file(self.groups_file, group_file)
                print("Dars qo'shildi")
        else:
            print("Sizning baholash uchun guruhingiz yo'q adminga murojat qiling")
            return

    def choice_month(self, phone: str, group: str, file: dict) -> str:
        lesson_count = len(file['teacher'][phone]['groups'][group]['lessons'])
        self.__str__()
        month = None
        if 0 < lesson_count <= 12:
            month = 1
        elif 12 < lesson_count <= 24:
            month = 2
        elif 24 < lesson_count <= 36:
            month = 3
        elif 36 < lesson_count <= 48:
            month = 4
        elif 48 < lesson_count <= 60:
            month = 5
        elif 60 < lesson_count <= 72:
            month = 6
        elif 72 < lesson_count <= 84:
            month = 7
        elif 84 < lesson_count <= 96:
            month = 8
        elif lesson_count < 0 or lesson_count > 96:
            month = "no"
        return month

    def choice_student(self, group: str, file: dict) -> list:
        self.__str__()
        students: list = []
        for student_phone in file[group]['students'].keys():
            students.append(student_phone)
        return students

    def rating_ball(self, phone: str, file: dict) -> None:
        group_file: dict = self.read_to_file(self.groups_file)
        group_list: list = []
        lessons: list = []
        student_list: list = []
        if len(file['teacher'][phone]['groups']) > 0:
            for group in file['teacher'][phone]['groups'].keys():
                group_list.append(group)
            group: str = self.list_choice(group_list)
            if len(file['teacher'][phone]['groups'][group]['lessons']) > 0:
                for lesson in file['teacher'][phone]['groups'][group]['lessons'].keys():
                    lessons.append(lesson)
                lesson: str = self.list_choice(lessons)
                for student, value in file['teacher'][phone]['groups'][group]['lessons'][lesson]['student'].items():
                    try:
                        if value['attendees']:
                            if value['grade'] == "ball":
                                student_list.append(student)
                                print(f"{file['student'][student]['full_name']} - O'quvchini baholang")
                                g = int_input("ball: ")
                                while 0 > g or g > 100:
                                    print("0 dan 100 gacha baholang.")
                                    g = int_input("ball: ")
                                value['grade'] = g
                                xp = file['student'][student]['my_results']['xp']
                                xp, silver = self.xp_for(g, self.find_level(xp))
                                sms = f"uyga vasifa bajarganingiz uchun {xp} xp berild"
                                file['student'][student]['sms'].append(sms)
                                try:
                                    file['student'][student]['groups'][group]['lessons'][lesson][student]['grade'] = g
                                except TypeError:
                                    pass
                                except KeyError:
                                    pass
                                file['student'][student]['my_results']['xp'] += xp
                                file['student'][student]['my_results']['silver'] += silver
                                file['student'][student]['my_results']['be_homework'][0] += xp
                                file['student'][student]['my_results']['be_homework'][1] += silver
                                group_file[group]['students'][student] += xp
                        else:
                            print(f"{file['student'][student]['full_name']} - bu o'quvchi darsga kelmagan.")
                    except KeyError:
                        pass
                    self.write_to_file(self.users_file, file)
                    self.write_to_file(self.groups_file, group_file)
                if len(student_list) <= 0:
                    print("Oldin baholangan")
        else:
            print("Sizning baholash uchun guruhingiz yo'q adminga murojat qiling")
            return

    def change_rating(self, phone: str, file: dict) -> None:
        group_file: dict = self.read_to_file(self.groups_file)
        group_list: list = []
        lessons: list = []
        if len(file['teacher'][phone]['groups']) > 0:
            for group in file['teacher'][phone]['groups'].keys():
                group_list.append(group)
            group: str = self.list_choice(group_list)
            if len(file['teacher'][phone]['groups'][group]['lessons']) > 0:
                for lesson in file['teacher'][phone]['groups'][group]['lessons'].keys():
                    lessons.append(lesson)
                lesson: str = self.list_choice(lessons)
                for student, value in file['teacher'][phone]['groups'][group]['lessons'][lesson]['student'].items():
                    try:
                        if value['attendees']:
                            xp = file['student'][student]['my_results']['xp']
                            old_grade = file['student'][student]['groups'][group]['lessons'][lesson][student]['grade']
                            print(f"{file['student'][student]['full_name']} : {old_grade}-ball")
                            grade = int_input("Yangi ball: ")
                            while 0 > grade or grade > 100:
                                print("0 dan 100 gacha baholang.")
                                grade = int_input("ball: ")
                            value['grade'] = grade
                            old_xp, old_silver = self.xp_for(old_grade, self.find_level(xp))
                            xp, silver = self.xp_for(grade, self.find_level(xp))
                            sms = f"Sizning balingiz o'zgartirildi {old_xp} dan {xp} ga o'zgartirildi"
                            file['student'][student]['sms'].append(sms)
                            file['student'][student]['groups'][group]['lessons'][lesson][student]['grade'] = grade
                            file['student'][student]['my_results']['xp'] += xp - old_xp
                            file['student'][student]['my_results']['silver'] += silver - old_silver
                            file['student'][student]['my_results']['be_homework'][0] += xp - old_xp
                            file['student'][student]['my_results']['be_homework'][1] += silver - old_silver
                            group_file[group]['students'][student] += xp - old_xp
                        else:
                            print(f"{file['student'][student]['full_name']} - bu o'quvchi darsga kelmagan.")
                    except KeyError:
                        pass
                    self.write_to_file(self.users_file, file)
                    self.write_to_file(self.groups_file, group_file)

    def view_lesson_time(self, phone: str, file: dict) -> None:
        group_lies: list = []
        lesson_list = []
        if len(file['teacher'][phone]['groups']) > 0:
            for group in file['teacher'][phone]['groups'].keys():
                group_lies.append(group)
            group: str = self.list_choice(group_lies)
            if len(file['teacher'][phone]['groups'][group]['lessons']) > 0:
                for lesson in file['teacher'][phone]['groups'][group]['lessons'].keys():
                    lesson_list.append(lesson)
                lesson: str = self.list_choice(lesson_list)
                text = f"""
        Dars sanasi: {file['teacher'][phone]['groups'][group]['lessons'][lesson]['lesson_date']}
        Boshlash vaqti: {file['teacher'][phone]['groups'][group]['lessons'][lesson]['start_time']} 
        Tugash vaqti: {file['teacher'][phone]['groups'][group]['lessons'][lesson]['end_time']}
"""
                print(text)
            else:
                print("Sizda hali dsars qo'shilmagan.")
                return
        else:
            print("Sizning baholash uchun guruhingiz yo'q adminga murojat qiling")
            return
