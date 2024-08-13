from Exam_4.user.personal_information import PersonalInfo, int_input


class HomePage(PersonalInfo):
    def __init__(self):
        super().__init__()

    def home_page(self, phone: str, file: dict) -> None:
        silver = file['student'][phone]['my_results']['silver']
        xp = file['student'][phone]['my_results']['xp']

        text = f"""
    Kumoshlar: {silver} 🩶
    {self.stage(phone=phone, file=file)}
    XP: {xp}
    Reyting
    Umumiy: {self.all_rating(phone=phone, file=file)}
    {self.group_rating(phone=phone, file=file)}
        """
        print(text)

    def stage(self, phone: str, file: dict) -> str:
        self.__str__()
        xp = file['student'][phone]['my_results']['xp']
        if 0 <= xp < 200:
            text = f"""
    Bosqich: 0
    {xp}/200
            """
        elif 200 <= xp < 450:
            text = f"""
    Bosqich: 1
    {xp}/450
            """
        elif 450 <= xp < 750:
            text = f"""
    Bosqich: 2
    {xp}/700
            """
        elif 700 <= xp < 950:
            text = f"""
    Bosqich: 3
    {xp}/950
            """
        elif 950 <= xp <= 1250:
            text = f"""
    Bosqich: 4
    {xp}/1200
            """
        else:
            text = f"""
    Bosqich: 5
    {xp}/20000
            """
        return text

    def all_rating(self, phone: str, file: dict) -> str:
        self.__str__()
        user_phone_list: list = []
        user_index: list = []
        xp_list = []
        for phone_num, phone_value in file['student'].items():
            xp_list.append(phone_value['my_results']['xp'])
            user_phone_list.append(phone_num)
        while len(xp_list) > 0:
            max_xp = max(xp_list)
            xp_index = xp_list.index(max_xp)
            user_phone = user_phone_list[xp_index]
            user_index.append(user_phone)
            xp_list.remove(max_xp)
            user_phone_list.remove(user_phone)
        return f"{user_index.index(phone) + 1}"

    def group_rating(self, phone: str, file: dict) -> str:
        group_file: dict = self.read_to_file(self.groups_file)
        if len(file['student'][phone]["groups"]) > 0:
            for group in file['student'][phone]["groups"]:
                count = 1
                xp = group_file[group]['students'][phone]
                for phone_number, xp_for in group_file[group]['students'].items():
                    if phone_number == phone:
                        pass
                    else:
                        if xp < xp_for:
                            count += 1
                return f"Guruh: {group}: {count}-o'rin"
        else:
            return "Sizning guruhingiz yoq."
