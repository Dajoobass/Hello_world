# Функция принимает records — список словарей
# Возвращает кортеж, где:
# первый элемент — список словарей
# второй элемент — список строк (ошибок)

def process_samples(records: list[dict]) -> tuple[list[dict], list[str]]:
    """Обрабатывает значения проб и присваивает им категорию качества."""
    processed_records = []
    errors = []

    for item in records:
        try:
            item["value"] = float(item["value"])
            
            if item["value"] < 5:
                item["quality"] = "low"
            elif item["value"] > 10:
                item["quality"] = "high"
            else:
                item["quality"] = "normal"
                
            processed_records.append(item)
            
        except Exception as e:
            errors.append(f"Sample {item.get('id')}: {e}")

    return processed_records, errors


data = [
    {"id": "S001", "value": "4.2"},
    {"id": "S002", "value": "7.5"},
    {"id": "S003", "value": "10"},
    {"id": "S004", "value": "12.8"},
    {"id": "S005", "value": "5"},
    {"id": "S006", "value": "error"},
    {"id": "S007", "value": ""},
    {"id": "S008"},
    {"value": "9.1"},
]

valid, errs = process_samples(data)


print("=== УСПЕШНО ОБРАБОТАННЫЕ ЗАПИСИ ===\n")
for record in valid:
    print(f"ID: {record.get('id', '—'):<6} | "
          f"Value: {record['value']:>6} | "
          f"Quality: {record['quality']}")
    
print(f"\n=== ОБНАРУЖЕННЫЕ ОШИБКИ === ({len(errs)} шт.)\n")
if errs:
    for error in errs:
        print(f"!!! {error}")
else:
    print("Ошибок не обнаружено.")

print(f"\nИтого: {len(valid)} успешно | {len(errs)} с ошибками")