def parse_config_from_file(filepath):
    config = {}
    
    with open(filepath, 'r', encoding='utf-8') as file:
        
        # Читаем файл построчно напрямую из объекта file
        for line in file:
            line = line.strip()
            
            if not line or line.startswith('#'):
                continue
                
            parts = line.split('=', 1)
            
            # Если разделение успешно (есть ключ и значение)
            if len(parts) == 2:
                key = parts[0].strip()
                value = parts[1].strip()
                
                # Записываем в словарь
                config[key] = value
                
    return config



test_filename = 'equipment_config.txt'

result = parse_config_from_file(test_filename)

print("Результат парсинга файла:")
print(result)