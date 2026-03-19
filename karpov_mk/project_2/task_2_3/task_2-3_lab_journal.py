filename = "journal.txt"

WIDTH = 50

separator = "+" + "-" * 52 + "+"

with open(filename, mode="w", encoding="utf-8") as file:

    name = input("Введите ФИО исследователя: ")
    date = input("Введите дату: ")
    experiment = input("Введите название эксперимента: ")
    conclusion = input("Введите вывод: ")

    line_name = f"ФИО исследователя : {name}"
    line_date = f"Дата              : {date}"
    line_exp  = f"Эксперимент       : {experiment}"

    text = f"{separator}\n"
    text += f"| {'Электронный лабораторный журнал':<{WIDTH}} |\n"
    text += f"{separator}\n"
    text += f"| {line_name:<{WIDTH}} |\n"
    text += f"| {line_date:<{WIDTH}} |\n"
    text += f"| {line_exp:<{WIDTH}} |\n"
    text += f"{separator}\n"
    text += f"| {'Вывод:':<{WIDTH}} |\n"
    text += f"| {conclusion:<{WIDTH}} |\n"
    text += f"{separator}\n"

    file.write (text)

      
