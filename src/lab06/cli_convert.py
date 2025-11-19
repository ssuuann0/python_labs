import argparse
from pathlib import Path
import sys
sys.path.append('C:/Users/Соня/OneDrive/Рабочий стол/git/python_labs-1/src/lab_05')
from json_csv import json_to_csv, csv_to_json
from csv_xlsx import csv_to_xlsx


def main():
    parser = argparse.ArgumentParser(description="Конвертеры данных")
    sub = parser.add_subparsers(dest="cmd")

    p1 = sub.add_parser("json2csv",help='Перевести json в csv')
    p1.add_argument("--in", dest="input", required=True)
    p1.add_argument("--out", dest="output", required=True)

    p2 = sub.add_parser("csv2json",help='Перевести csv в json')
    p2.add_argument("--in", dest="input", required=True)
    p2.add_argument("--out", dest="output", required=True)

    p3 = sub.add_parser("csv2xlsx",help='Перевести csv в xlsx')
    p3.add_argument("--in", dest="input", required=True)
    p3.add_argument("--out", dest="output", required=True)

    args = parser.parse_args()

    try:
        if args.cmd == 'json2csv':
            json_to_csv(args.input, args.output)
        if args.cmd == 'csv2json':
            csv_to_json(args.input, args.output)
        if args.cmd == 'csv2xlsx':
            csv_to_xlsx(args.input, args.output)
    except FileNotFoundError:
        raise FileNotFoundError('Нет входного файла')


if __name__ == "__main__":
    main()


#py -m src.lab_06.cli_convert json2csv --in  src/data/lab_05/samples/people.json  --out src/data/lab_06/out/people2_from_json.csv

#py -m src.lab_06.cli_convert csv2json --in  src/data/lab_05/samples/people.csv  --out src/data/lab_06/out/people2_from_csv.json

#py -m src.lab_06.cli_convert csv2xlsx --in  src/data/lab_05/samples/people.csv  --out src/data/lab_06/out/people2.xlsx 

#py -m src.lab_06.cli_convert --help