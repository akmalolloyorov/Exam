from Exam_4.admin.personal_admin import PersonalAdmin, int_input


class StudentFor(PersonalAdmin):
    def student_for(self) -> bool:
        self.exit = True
        return self.exit
