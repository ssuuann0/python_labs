# Лабораторная 7

# Задание 1

```python
import pytest  # библиотека pytest для создания и запуска тестов
from pathlib import Path
import sys

sys.path.append("C:/Users/Соня/OneDrive/Рабочий стол/git/python_labs-1/src/lib")
from text2 import normalize, tokenize, count_freq, top_n


# параметризация для запуска одного теста с разными наборами данных
@pytest.mark.parametrize(
    "source, expected",  # параметры: source - входной текст, expected - итог
    [
        ("ПрИвЕт\nМИр\t", "привет мир"),
        ("ёжик, Ёлка", "ежик, елка"),
        ("Hello\r\nWorld", "hello world"),
        ("  двойные   пробелы  ", "двойные пробелы"),
        ("", ""),
    ],
)
def test_normalize_basic(source, expected):
    # функция теста для normalize, берет данные из параметризации
    assert (
        normalize(source) == expected
    )  # проверяем что normalize(source) возвращает expected


@pytest.mark.parametrize(
    "source,expected",
    [
        ("привет мир", ["привет", "мир"]),
        ("hello,world!!!", ["hello", "world"]),
        ("по-настоящему круто", ["по-настоящему", "круто"]),
        ("2025 год", ["2025", "год"]),
        ("emoji 😀 не слово", ["emoji", "не", "слово"]),
        ("", []),
    ],
)
def test_tokenize_basic(source, expected):
    assert tokenize(source) == expected


def test_count_freq_and_top_n():  # проверяет функции count_freq и top_n
    tokens = ["a", "b", "a", "c", "b", "a"]
    freq = count_freq(tokens)
    assert freq == {"a": 3, "b": 2, "c": 1}
    assert top_n(freq, 2) == [("a", 3), ("b", 2)]
    assert top_n(freq, 0) == []
    assert top_n(freq, 5) == [("a", 3), ("b", 2), ("c", 1)]
    assert count_freq([]) == {}
    assert top_n({}, 5) == []


def test_top_n_tie_breaker():  # проверяет top_n с одинаковыми частотами
    freq = count_freq(["bb", "aa", "bb", "aa", "cc"])
    assert top_n(freq, 3) == [("aa", 2), ("bb", 2), ("cc", 1)]
```
<img src="https://github.com/ssuuann0/python_labs/blob/d5a09bbbd83ce3f794f9e3256096f32ab36a74bf/images/lab07/test_text.png" alt="Картинка 1" />

# Задание 2

```python
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
```
<img src="https://github.com/ssuuann0/python_labs/blob/d5a09bbbd83ce3f794f9e3256096f32ab36a74bf/images/lab07/test_json_csv.png" alt="Картинка 1" />
