volume = float(input("Введите нужный объём раствора (мл): "))

mass_salt = volume * 0.009

round(volume,2)
round(mass_salt,2)


report = f"""ОТЧЕТ ПО ПРИГОТОВЛЕНИЮ:
--------------------------

Общий объём:     {volume} мл
Масса соли:      {mass_salt} г
Объём воды:      {volume} мл
"""

with open("recipe.txt", "w", encoding="utf-8") as file:
    file.write(report)