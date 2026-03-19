filename = "recipe.txt"

with open(filename, mode="a", encoding="utf-8") as file:

    name = input("Введите название питательной среды: ")
    quantity = input("Введите концентрацию агара(%): ")
    temp = input("Введите температуру стерилизации(°C): ")
    file.write (f"{name}:\n Концентрация: {quantity}%, температура: {temp}°C\n")
    print ("Данные записаны в recipe.txt")

      
