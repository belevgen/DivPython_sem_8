# Задание 1
# Вспоминаем задачу 3 из прошлого семинара. Мы сформировали текстовый файл с псевдо именами и произведением чисел.
# Напишите функцию, которая создаёт из созданного ранее файла новый с данными в формате JSON.
# Имена пишите с большой буквы.
# Каждую пару сохраняйте с новой строки.

# import json
# from pathlib import Path
#
# def convert(file: Path) -> None:
#     data = {}
#     with open(file, 'r', encoding='utf-8') as f:
#         for line in f:
#             # print(line.split())
#             name, number = line.split()
#             data[name.title()] = float(number)
#         # print(data)
#     with open(file.stem+'.json', 'w', encoding='utf-8') as f:
#         json.dump(data, f, ensure_ascii=False, indent=2)
#
#
# if __name__ == "__main__":
#     convert(Path('C:/Users/77011/OneDrive/Документы/GeekBrains/Уроки/Погружение в Python_06.09.23/Погружение в Python. Часть 1 (лекции)/Семинар 8. Сериализация/seminar_8/results.txt'))

# Задание 2
# Напишите функцию, которая в бесконечном цикле запрашивает имя, личный идентификатор и уровень доступа (от 1 до 7).
# После каждого ввода добавляйте новую информацию в JSON файл.
# Пользователи группируются по уровню доступа.
# Идентификатор пользователя выступает ключём для имени.
# Убедитесь, что все идентификаторы уникальны независимо от уровня доступа.
# При перезапуске функции уже записанные в файл данные должны сохраняться.

# import json
# from pathlib import Path
#
#
# def set_user(file: Path) -> None:
#     unique_id = set()
#     if file.is_file():
#         with open(file, "r", encoding="utf-8") as f:
#             data = json.load(f)
#             print(data)
#
#             for value in data.values():
#                 unique_id.update(value.keys())
#                 print(value)
#                 print(unique_id)
#                 print()
#             return
#     else:
#         data = {str(i): {} for i in range(1, 8)}
#     while True:
#         name = input("Name: ")
#         if not name:
#             break
#         id = input("ID: ")
#         level = input("Level [1, 7]: ")
#         # if id in unique_id and data[level].get(id) is None:
#         #     continue
#         data[level].update({id: name})
#         print(data)
#
#         with open(file, "w", encoding="utf-8") as f:
#             json.dump(data, f, indent=2, ensure_ascii=False)
#
#
# if __name__ == "__main__":
#     set_user(Path("users.json"))

# Задание №3
# Напишите функцию, которая сохраняет созданный в прошлом задании файл в формате CSV.

import csv
import json
from pathlib import Path

def json_to_csv(file: Path) -> None:
    print(file)
    with open(file, "r", encoding="utf-8") as f:
        data = json.load(f)
        print(data)
    rows = []
    for level, value in data.items():
        print(level, value, sep="=")
        for id, name in value.items():
            print("\t"+id, name, sep="-")
            rows.append({'level': int(level), 'id': int(id), 'name': name})
    print(rows)
    with open(f'{file.stem}.csv', "w", encoding="utf-8", newline="") as f:
        csv_write = csv.DictWriter(f, fieldnames=['level', 'id', 'name'], dialect='excel-tab')
        csv_write.writeheader()
        csv_write.writerows(rows)

if __name__ == "__main__":
    json_to_csv(Path("users.json"))


# Задание №4
# Прочитайте созданный в прошлом задании csv файл без использования csv.DictReader.
# Дополните id до 10 цифр незначащими нулями.
# В именах первую букву сделайте прописной.
# Добавьте поле хеш на основе имени и идентификатора.
# Получившиеся записи сохраните в json файл, где каждая строка csv файла представлена как отдельный json словарь.
# Имя исходного и конечного файлов передавайте как аргументы функции.

# Задание №5
# Напишите функцию, которая ищет json файлы в указанной директории и сохраняет их содержимое в виде одноимённых pickle файлов.

import pickle
import json
from pathlib import Path


def json_to_picle(path: Path) -> None:
    for file in path.iterdir():
        # print(file.suffix)
        if file.is_file() and file.suffix == ".json":
            with open(file, "r", encoding="utf-8") as f:
                data = json.load(f)
            with open(f"{file.stem}.pickle", "wb") as f:
                pickle.dump(data, f)


if __name__ == "__main__":
    json_to_picle(Path("C:/GeekBrain/Погружение в Python/project/Seminars"))


# Задание №6
# Напишите функцию, которая преобразует pickle файл хранящий список словарей в табличный csv файл.
# Для тестированию возьмите pickle версию файла из задачи 4 этого семинара.
# Функция должна извлекать ключи словаря для заголовков столбца из переданного файла.

# Задание №7
# Прочитайте созданный в прошлом задании csv файл без использования csv.DictReader.
# Распечатайте его как pickle строку.