products = [
    {"sku": "A1", "category": "flour", "expected": 100, "actual": 95},
    {"sku": "B2", "category": "sugar", "expected": 50, "actual": 50},
    {"sku": "C3", "category": "enzyme", "expected": 10, "actual": 12},
]

# Создаем пустой список с именем discrepancies
discrepancies = []
for item in products:
    if item["actual"] != item["expected"]:
        diff = item["actual"] - item["expected"] 
        discrepancies.append((item["sku"], diff))

# Создание словаря by_category
by_category = {}
for item in products:
    category = item["category"]
    sku = item["sku"]
    
    # Если категории еще нет в словаре, создаем пустой список
    if category not in by_category:
        by_category[category] = []
        
    # Добавляем sku в список соответствующей категории
    by_category[category].append(sku)

print("Расхождения (discrepancies):")
print(discrepancies)
print("\nКатегории (by_category):")
print(by_category)