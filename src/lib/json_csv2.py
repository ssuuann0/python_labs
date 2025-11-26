from pathlib import Path

import json
import csv


def json_to_csv(json_path: str, csv_path: str) -> None:
    """
    Преобразует JSON-файл в CSV.
    Поддерживает список словарей [{...}, {...}], заполняет отсутствующие поля пустыми строками.
    Кодировка UTF-8. Порядок колонок — как в первом объекте или алфавитный (указать в README).
    """
    p_json = Path(json_path)
    p_csv = Path(csv_path)
    if (
        p_json.suffix.lower() != ".json" or p_csv.suffix.lower() != ".csv"
    ):  # проверка типа файла
        raise ValueError("Неверный тип файла")
    try:
        with open(json_path, "r", encoding="utf-8") as f:
            people_dict = json.load(f)  # переводит json в список словарей
        if len(people_dict) == 0:
            raise ValueError("Пустой JSON или неподдерживаемая структура")
        if not isinstance(people_dict[0], dict):
            raise ValueError("Неверное содержание файла")
        with open(csv_path, "w", encoding="utf-8") as c:
            sort_keys = set()
            sort_keys.update(people_dict[0].keys())
            sort_keys.update(people_dict[1].keys())
            fieldnames = list(
                sorted(sort_keys)
            )  # сохраняет ключи словаря для будущих заголовков csv в алфавитном порядке
            writer = csv.DictWriter(c, fieldnames=fieldnames)
            writer.writeheader()  # запись заголовка
            writer.writerows(people_dict)  # заполнение столбцов

    except FileNotFoundError:
        raise FileNotFoundError("Файл не найден")
    except json.JSONDecodeError:
        raise ValueError(
            "Ошибка декодирования JSON: файл пустой или содержит некорректный JSON"
        )
    except Exception as e:
        # Для всех других исключений выбрасываем ValueError
        raise ValueError(f"Ошибка обработки файла: {str(e)}")


def csv_to_json(csv_path: str, json_path: str) -> None:
    """
    Преобразует CSV в JSON (список словарей).
    Заголовок обязателен, значения сохраняются как строки.
    json.dump(..., ensure_ascii=False, indent=2)
    """
    p_json = Path(json_path)
    p_csv = Path(csv_path)
    if (
        p_json.suffix.lower() != ".json" or p_csv.suffix.lower() != ".csv"
    ):  # проверка типа файла
        raise ValueError("Неверный тип файла")
    try:
        with open(csv_path, "r", encoding="utf-8") as cs:
            csv_dict = list(
                csv.DictReader(cs)
            )  # преобразует csv файл в список словарей
        if len(csv_dict) == 0:
            raise ValueError("Пустой файл")
        with open(json_path, "w", encoding="utf-8") as js:
            json.dump(csv_dict, js, ensure_ascii=False, indent=2)
    except FileNotFoundError:
        raise FileNotFoundError("Файл не найден")
    except Exception as e:
        # Для всех других исключений выбрасываем ValueError
        raise ValueError(f"Ошибка обработки файла: {str(e)}")
