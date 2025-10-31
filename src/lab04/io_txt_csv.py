from pathlib import Path

def read_text(path: str | Path, encoding: str = "utf-8") -> str:
    p=Path(path)
    try:
        with open(p,'r',encoding=encoding) as file:
                return str(' '.join(file.read().split()))
    except FileNotFoundError as e:
         raise FileNotFoundError('Файл не найден') from e
    except UnicodeDecodeError as e:
         raise ValueError('Неправильная коодировка') from e
#print(read_text(r"C:\Users\Соня\OneDrive\Рабочий стол\git\python_labs-1\src\lab_04\input.txt"))#пользователь может выбрать другую кодировку, прописав это 

import csv

def write_csv(rows: list[tuple | list], path: str | Path, header: tuple[str, ...] | None = None) -> None:
    p = Path(path)
    rows = list(rows)
    if rows:
        first_length = len(rows[0])
        for i, row in enumerate(rows):
            if len(row) != first_length:
                raise ValueError(f"Строка {i+1} имеет длину {len(row)}, ожидается {first_length}")

    if header is not None and rows:
        if len(header) != len(rows[0]):
            raise ValueError(f"Header имеет длину {len(header)}, а строки - {len(rows[0])}")

    with p.open("w", newline="", encoding="utf-8") as f:
        w = csv.writer(f)
        if header is not None:
            w.writerow(header)
        for r in rows:
            w.writerow(r)

write_csv([("word","count"),("test",3)], r"C:\Users\Соня\OneDrive\Рабочий стол\git\python_labs-1\src\lab_04\check.csv")