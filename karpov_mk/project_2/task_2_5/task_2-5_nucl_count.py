print(f"\n=== Анализ последовательности ДНК ===\n")

seq = input("Введите последовательность ДНК: ")
seq_upper = seq.upper()

print(f"\nПоследовательность в верхнем регистре: {seq_upper}\n")

count_A = seq_upper.count('A')
count_T = seq_upper.count('T')
count_G = seq_upper.count('G')
count_C = seq_upper.count('C')

total = len(seq_upper)

print("Подсчёт нуклеотидов:")
print(f"A: {count_A}")
print(f"T: {count_T}")
print(f"G: {count_G}")
print(f"C: {count_C}")
print("\nПроцентное содержание:")
print(f"A: {count_A / total * 100:.1f}%")
print(f"T: {count_T / total * 100:.1f}%")
print(f"G: {count_G / total * 100:.1f}%")
print(f"C: {count_C / total * 100:.1f}%")

print(f"\nОбщая длина: {total} нуклеотидов\n")