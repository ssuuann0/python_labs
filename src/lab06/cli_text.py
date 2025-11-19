import argparse
from pathlib import Path
import sys
sys.path.append('C:/Users/Соня/OneDrive/Рабочий стол/git/python_labs-1/src/lib')
from text2 import *

def main():
    parser = argparse.ArgumentParser(description="CLI‑утилиты лабораторной №6") 
    subparsers = parser.add_subparsers(dest="command",required=True)

    # подкоманда cat
    cat_parser = subparsers.add_parser("cat", help="Вывести содержимое файла")
    cat_parser.add_argument("--input", required=True)
    cat_parser.add_argument("-n", action="store_true", help="Нумеровать строки")

    # подкоманда stats
    stats_parser = subparsers.add_parser("stats", help="Частоты слов")
    stats_parser.add_argument("--input", required=True)
    stats_parser.add_argument("--top", type=int, default=5)

    args = parser.parse_args()
    try:
        path_input = Path(args.input)
        str_input = path_input.read_text(encoding='utf-8')#открывает файл,читает как строку и закрывает

        if args.command == "cat":
            """ Реализация команды cat """
            for num, word in enumerate(str_input.split('\n')):#num-номер строки(с 0), а word сама строку
                if args.n:
                    print(num + 1, word)
                else:
                    print(word)
        elif args.command == "stats":
            """ Реализация команды stats """
            print(f'Всего слов:{len(tokenize(str_input))}')
            print(f'Уникальных слов:{len(set(tokenize(str_input)))}')
            print(f'Топ-{args.top}:')
            for i in top_n(count_freq(tokenize(normalize(str_input))),args.top):
                print(f'{i[0]}:{i[1]}')
    except FileNotFoundError:
        raise FileNotFoundError("Нет входного файла")


if __name__ == "__main__":
    main()

#py -m src.lab_06.cli_text cat --input  src/data/lab_06/my_cli.txt -n

#py -m src.lab_06.cli_text stats --input  src/data/lab_06/my_cli.txt --top 3

#py -m src.lab_06.cli_text stats --help