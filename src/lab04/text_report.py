import sys
sys.path.append('C:/Users/Соня/OneDrive/Рабочий стол/git/python_labs-1/src/lib')
from text2 import count_freq, top_n, tokenize, normalize
from io_txt_csv import read_text, write_csv
from pathlib import Path

def text_report(path:Path|str):
    p=Path(path)
    text_str=read_text(p)
    norm_text=tokenize(normalize(text_str))
    freq_text=top_n(count_freq(norm_text))
    write_csv(freq_text,r"C:\Users\Соня\OneDrive\Рабочий стол\git\python_labs-1\src\data\lab_04\report.csv")
    print(f'Всего слов:{len(norm_text)}')
    print(f'Уникальных слов:{len(set(norm_text))}')
    print('Топ-5:')
    for i in freq_text:
        print(f'{i[0]}:{i[1]}')
text_report(r"C:\Users\Соня\OneDrive\Рабочий стол\git\python_labs-1\src\data\lab_04\input.txt")