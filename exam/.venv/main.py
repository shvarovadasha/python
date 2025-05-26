import re
import sys
import json
from collections import Counter

# Регулярное выражение для парсинга строки лога
LOG_PATTERN = re.compile(
    r'(?P<ip>\d+\.\d+\.\d+\.\d+) - - \[(?P<datetime>[^\]]+)\] "(?P<method>\S+) (?P<url>\S+) \S+" (?P<status>\d{3}) \d+'
)

def parse_log_line(line):
    """Парсит строку лога, возвращает словарь или None."""
    match = LOG_PATTERN.match(line)
    if not match:
        return None
    d = match.groupdict()
    date_only = d['datetime'].split(':')[0]  # Извлекаем только дату
    return {
        'ip': d['ip'],
        'date': date_only,
        'url': d['url'],
        'status': d['status']
    }

def filter_and_collect_stats(filename, filter_date):
    """Фильтрует лог по дате и собирает статистику."""
    ip_counter = Counter()
    url_counter = Counter()
    status_counter = Counter()

    try:
        with open(filename, 'r', encoding='utf-8') as f:
            for line_num, line in enumerate(f, 1):
                parsed = parse_log_line(line)
                if parsed is None:
                    print(f"Пропущена некорректная строка {line_num}")
                    continue
                if parsed['date'] == filter_date:
                    ip_counter[parsed['ip']] += 1
                    url_counter[parsed['url']] += 1
                    status_counter[parsed['status']] += 1
    except FileNotFoundError:
        print(f"Ошибка: файл '{filename}' не найден.")
        sys.exit(1)
    except Exception as e:
        print(f"Ошибка при чтении файла: {e}")
        sys.exit(1)

    return ip_counter, url_counter.most_common(5), status_counter

def print_report(ip_counter, top_urls, status_counter, date):
    """Выводит отчёт в консоль."""
    print(f"\n--- Log Analysis Report for {date} ---\n")

    print("Requests per IP:")
    if ip_counter:
        for ip, count in ip_counter.items():
            print(f"{ip}: {count}")
    else:
        print("(нет данных)")

    print("\nTop 5 Requested URLs:")
    if top_urls:
        for url, count in top_urls:
            print(f"{url}: {count}")
    else:
        print("(нет данных)")

    print("\nRequests per Status Code:")
    if status_counter:
        for status, count in status_counter.items():
            print(f"{status}: {count}")
    else:
        print("(нет данных)")

def save_report_to_json(ip_counter, top_urls, status_counter, date):
    """Сохраняет отчёт в файл report.json."""
    report = {
        "date": date,
        "requests_per_ip": dict(ip_counter),
        "top_urls": top_urls,
        "requests_per_status_code": dict(status_counter)
    }
    try:
        with open('report.json', 'w', encoding='utf-8') as f:
            json.dump(report, f, indent=2, ensure_ascii=False)
        print("\nОтчёт сохранён в report.json")
    except Exception as e:
        print(f"Ошибка при сохранении JSON: {e}")

def main():
    filename = input("Введите имя файла лога: ").strip()
    filter_date = input("Введите дату (ДД/Мес/ГГГГ, например 10/Oct/2023): ").strip()

    ip_counter, top_urls, status_counter = filter_and_collect_stats(filename, filter_date)
    print_report(ip_counter, top_urls, status_counter, filter_date)
    save_report_to_json(ip_counter, top_urls, status_counter, filter_date)

if __name__ == "__main__":
    main()
