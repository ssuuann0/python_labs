import sys
sys.path.append('C:/Users/Соня/OneDrive/Рабочий стол/git/python_labs-1/src/lib')
from text2 import count_freq, top_n, tokenize, normalize

fr=input()
print(f'Всего слов:{len(tokenize(fr))}')
print(f'Уникальных слов:{len(set(tokenize(fr)))}')
print('Топ-5:')
for i in top_n(count_freq(tokenize(normalize(fr)))):
    print(f'{i[0]}:{i[1]}')