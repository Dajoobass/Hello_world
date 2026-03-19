phenotype_d = input("Введите фенотип группы крови донора (I, II, III, IV): ").strip().upper()
phenotype_r = input("Введите фенотип группы крови реципиента (I, II, III, IV): ").strip().upper()

if phenotype_d == phenotype_r or phenotype_d == "I" or phenotype_r == "IV":
    print(f"\nПереливаем!")
else:
    print(f"\nНе переливаем!")
