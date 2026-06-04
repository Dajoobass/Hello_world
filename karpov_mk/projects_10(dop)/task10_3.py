import json

def analyze_process_logs(jsonl_path, report_path):
    # Словарь для хранения счетчиков уровней логов
    level_counts = {}
    total_events = 0
    
    with open(jsonl_path, 'r', encoding='utf-8') as file:
        for line in file:

            if not line.strip():
                continue
                
            # Превращаем строку JSON в Python-словарь
            log_entry = json.loads(line)
            
            # Извлекаем уровень (INFO, ERROR и т.д.)
            level = log_entry.get('level')
            
            if level:
                # Если такой уровень уже есть в словаре, увеличиваем счетчик
                if level in level_counts:
                    level_counts[level] += 1
                # Если уровня еще нет, создаем его со значением 1
                else:
                    level_counts[level] = 1
                    
                total_events += 1

    with open(report_path, 'w', encoding='utf-8') as report_file:

        report_file.write("Process Log Report\n")
        report_file.write("==================\n")
        
        #  Метод .items() позволяет нам доставать одновременно и ключ, и его значение. 
        #  Они попадают в переменные level и count.
        for level, count in level_counts.items():
            report_file.write(f"{level}: {count}\n")
            
        # Пишем общее количество
        report_file.write(f"Total: {total_events}\n")
        
    
    return level_counts

test_jsonl = 'process_logs.jsonl'
test_report = 'log_report.txt'


result_dict = analyze_process_logs(test_jsonl, test_report)

print("Функция вернула словарь:")
print(result_dict)

print("\n--- Содержимое созданного файла отчета ---")
with open(test_report, 'r', encoding='utf-8') as f:
    print(f.read())