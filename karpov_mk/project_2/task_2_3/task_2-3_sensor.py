filename = "sensor_log.txt"

with open(filename, mode="a", encoding="utf-8") as file:

    name = input("Введите имя оператора: ")
    pressure = input("Введите текущее значение давления (Па): ")
    file.write (f"{name}:\t{pressure}Па\n")
    print ("Данные сохранены в sensor_log.txt")
      
