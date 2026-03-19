protein = int(input("Введите массу белков в продукте(г): "))
fats = int(input("Введите массу жиров в продукте(г): "))
carbs = int(input("Введите массу углеводов в продукте(г): "))

nutrition = protein*4 + fats*9 + carbs*4 
print (f"Энергетическая ценность:\t{nutrition}")