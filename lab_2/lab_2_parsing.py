import re

# Замените путь к файлу на путь к вашему файлу CSV
file_path = "/Users/egorov_y/TOIB/lab_2/SotM30-anton.csv"

# Чтение логов из файла
with open(file_path, 'r') as file:
    log_data = file.read()

# Пример упрощенного парсера
regex_pattern = r'(\w{3} \d{1,2} \d{2}:\d{2}:\d{2}) (\S+) (\S+): (\S+ \S+): (\S+)=([\w\d.:]+) (\S+)=([\w\d.:]+) (\S+)=([\w\d.:]+) (\S+)=([\w\d.:]+) (\S+)=([\w\d.:]+) (\S+)=([\w\d.:]+) (\S+)=([\w\d.:]+) (\S+)=([\w\d.:]+) (\S+)=([\w\d.:]+) (\S+)=([\w\d.:]+) (\S+)=([\w\d.:]+) (\S+)=([\w\d.:]+) (\S+)=([\w\d.:]+) (\S+)=([\w\d.:]+) (\S+)=([\w\d.:]+)'

matches = re.finditer(regex_pattern, log_data)

result_file_path = "result.txt"  # Путь к файлу для записи результатов

with open(result_file_path, 'w') as result_file:
    for match in matches:
        groups = match.groups()
        labels = ["Date and Time", "Device Name", "Kernel", "Message Type", "Incoming Interface",
                  "Physical Incoming Interface", "Outgoing Interface", "Physical Outgoing Interface",
                  "Source IP", "Destination IP", "Length", "TOS", "PREC", "TTL", "ID", "Protocol",
                  "Source Port", "Destination Port", "Window", "RES", "Flag SYN", "URG pointer"]

        for label, value in zip(labels, groups):
            result_file.write(f"{label}: {value}\n")

        result_file.write("\n")
