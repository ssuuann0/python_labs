import pytest
import csv, json
from pathlib import Path
import sys

sys.path.append("C:/Users/Соня/OneDrive/Рабочий стол/git/python_labs-1/src/lib")
from json_csv2 import json_to_csv, csv_to_json


def test_json_to_csv_roundtrip(tmp_path: Path):
    src = (
        tmp_path / "people.json"
    )  # создаёт путь к исходному JSON файлу в временной директории
    dst = (
        tmp_path / "people.csv"
    )  # создаёт путь к целевому CSV файлу в той же временной директории
    data = [
        {"name": "Alice", "age": 22},
        {"name": "Bob", "age": 25},
    ]
    src.write_text(
        json.dumps(data, ensure_ascii=False, indent=2), encoding="utf-8"
    )  # записывает полученную JSON строку в src
    json_to_csv(str(src), str(dst))

    with dst.open(encoding="utf-8") as f:
        rows = list(csv.DictReader(f))  # создает список словарей из строк csv

    assert len(rows) == 2  # проверка строк
    assert {"name", "age"} <= set(rows[0].keys())  # проверка ключей


def test_csv_to_json_roundtrip(tmp_path: Path):
    src = tmp_path / "people.csv"
    dst = tmp_path / "people.json"
    rows = [
        {"name": "Alice", "age": "22"},
        {"name": "Bob", "age": "25"},
    ]
    with src.open("w", encoding="utf-8", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=["name", "age"])
        writer.writeheader()
        writer.writerows(rows)

    csv_to_json(str(src), str(dst))

    data_out = json.loads(dst.read_text(encoding="utf-8"))  # json в python объект

    assert len(data_out) == len(rows)
    assert {"name", "age"} <= set(rows[0].keys())
    assert data_out[0]["name"] == "Alice"
    assert data_out[0]["age"] == "22"


def test_json_to_csv_empty_file(tmp_path: Path):
    # пустой JSON файл - ValueError
    src = tmp_path / "sample.json"
    dst = tmp_path / "sample.csv"
    src.write_text("", encoding="utf-8")

    with pytest.raises(ValueError):
        json_to_csv(str(src), str(dst))


def test_csv_to_json_empty_file(tmp_path: Path):
    # пустой CSV файл - ValueError
    src = tmp_path / "sample.csv"
    dst = tmp_path / "sample.json"
    src.write_text("", encoding="utf-8")

    with pytest.raises(ValueError):
        csv_to_json(str(src), str(dst))


def test_json_to_csv_file_not_found():
    # несуществующий JSON файл - FileNotFoundError
    with pytest.raises(FileNotFoundError):
        json_to_csv("input.json", "output.csv")


def test_csv_to_json_file_not_found():
    # несуществующий CSV файл - FileNotFoundError
    with pytest.raises(FileNotFoundError):
        csv_to_json("input.csv", "output.json")
