SIGNS = ["Козирог", "Водолей", "Риби", "Овен", "Телец", "Близнаци",
         "Рак", "Лъв", "Дева", "Везни", "Скорпион", "Стрелец"]
LIMITS_FOR_MONTHS = [19, 18, 20, 20, 20, 20, 21, 22, 22, 22, 21, 21]


def what_is_my_sign(day, month):
    if day > LIMITS_FOR_MONTHS[month - 1]:
        month = (month + 1) % 12
    return SIGNS[month - 1]
