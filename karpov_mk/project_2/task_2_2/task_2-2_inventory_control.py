filename = "reagents_list.txt"

print ("Для конца работы с программмой, введите 'stop' вместо названия реактива")

with open(filename, mode="a", encoding="utf-8") as file:
    while True:

        name = input("Введите название реактива: ")

        if name.lower() == "stop":
            print ("Завершение работы.")
            break
    
        quantity = input(f"Введите количество для {name}: ")
    
        file.write (f"{name} -- {quantity}\n")

      
