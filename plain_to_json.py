import json

input_file = "ruDomainsList.txt"
output_file = "ruDomainsList.json"

domains = []

with open(input_file, "r", encoding="utf-8") as f:
    for line in f:
        # Убираем комментарий (всё после #)
        line = line.split("#", 1)[0]

        # Убираем пробелы и переносы строк
        domain = line.strip()

        # Пропускаем пустые строки
        if domain:
            domains.append(domain)

result = {"domains": domains}

with open(output_file, "w", encoding="utf-8") as f:
    json.dump(result, f, indent=4, ensure_ascii=False)
