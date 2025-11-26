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
![Картинка 1](./images/lab07/test_text.png)
