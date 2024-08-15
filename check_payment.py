import json
from datetime import datetime
import threading
import time


def check_payment(file: dict) -> None:
    students_list: list = []
    for student_phone in file['student'].keys():
        students_list.append(student_phone)
    if len(students_list) > 0:
        check_balance(student_list=students_list, file=file)
    else:
        pass


def check_balance(student_list: list, file: dict) -> None:
    for student_phone in student_list:
        group_list: list = [x for x in file['student'][student_phone]['groups'].keys()]
        if len(group_list) > 1:
            for group in group_list:
                if check_month(student_phone, file, group):
                    pass
                else:
                    file['student'][student_phone]['groups'][group]['status'] = False

        elif len(group_list) < 1:
            pass
        else:
            if check_month(student_phone, file, group_list[0]):
                pass
            else:
                file['student'][student_phone]['groups'][group_list[0]]['status'] = False
    with open('users.json', 'w') as f:
        json.dump(file, f, indent=4)


def check_month(student_phone: str, file: dict, group: str) -> bool:
    paid_month: int = paid(student_phone, file)
    course_balance, month = check_course_balance(group)
    student_balance: int = user_balance(student_phone, file)

    lessons: int = check_lesson(student_phone, file, group)
    for m in range(1, month + 1):
        if m <= paid_month:
            pass
        else:
            if lessons >= paid_month * 12 + 12:
                if student_balance >= course_balance:
                    file['student'][student_phone]['balance'] = student_balance - course_balance
                    payment = {
                        paid_month + 1: {
                            "money": course_balance,
                            "date": current_time(),
                            "type": "card",
                            "month": paid_month + 1
                        }
                    }
                    file['student'][student_phone]['my_payments'].update(payment)
                    with open(file="users.json", mode='w', encoding='UTF-8') as fi:
                        json.dump(file, fi, indent=4)
                else:
                    print("Student balance yetmaydi")
                    return False
            else:
                return True


def check_course_balance(group: str) -> tuple:
    with open(file='files/groups.json', mode='r', encoding='UTF-8') as f:
        groups_file = json.load(f)
    course_balance = groups_file[group]['course_price']
    month: int = groups_file[group]['term']
    return course_balance, month


def paid(student_phone: str, file: dict) -> int:
    month = 0
    for i in file['student'][student_phone]['my_payments'].values():
        try:
            for j in i['month']:
                month = j
        except TypeError:
            pass

    return month


def check_lesson(student_phone: str, file: dict, group: str) -> int:
    return len([x for x in file['student'][student_phone]['groups'][group]['lessons'].keys()])


def user_balance(student_phone: str, file: dict) -> int:
    balance: int = file['student'][student_phone]['balance']
    return balance


def current_time() -> str:
    return datetime.now().strftime("%Y-%m-%d %H:%M:%S")


def check_time(file: dict):
    with open(file="files/sleep.txt", mode='r', encoding="UTF-8") as f:
        time_for: int = int(f.read().strip())
    stop_event = threading.Event()
    t = threading.Thread(target=thread_worker, args=(stop_event, file, time_for))
    t.start()
    return stop_event


def thread_worker(stop_event, file: dict, time_for):
    while not stop_event.is_set():
        check_payment(file)
        time.sleep(time_for)
