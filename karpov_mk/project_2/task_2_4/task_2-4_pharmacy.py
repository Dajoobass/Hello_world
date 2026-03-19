total_capsules = int(input("Введите общее количество произведенных капсул: "))
size = int(input("Введите количество капсул в одной упаковке: "))

full = total_capsules // size
remainder = total_capsules % size


print("\n--- Отчет фасовочного цеха ---")
print(f"Полных упаковок:\t{full}")
print(f"Остаток капсул:\t{remainder}")