from Exam_4.teacher.teacher import Teacher, int_input


class PersonalAdmin(Teacher):
    def personal_admin(self, phone: str) -> bool:
        self.phone = phone
        self.exit = True
        return self.exit
