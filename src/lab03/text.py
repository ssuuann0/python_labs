
def normalize(text: str, *, casefold: bool = True, yo2e: bool = True):
    if casefold:
        text=text.casefold()
    if yo2e:
        text=text.replace('ё','е').replace('Ё','Е')
    if '\t' in text or '\n' in text or '\r' in text:
        text=text.replace('\t',' ').replace('\n',' ').replace('\r',' ')
    text=' '.join(text.split())
    return text
n='ёжик, Ёлка'
print(normalize(n))

import re
def tokenize(text):
    pat=r'[^\w-]'
    text= re.sub(pat,'  ',text)
    return text.split()
m="по-настоящему круто"
print(tokenize(m))

def count_freq(tokens: list[str]):
    counts=dict()
    for i in (sorted(set(tokens))):
            counts[i] = tokens.count(i)
    return counts

def top_n(freq: dict[str, int], n: int = 5):
     sorted_freq = sorted(freq.items(), key=lambda x: (-x[1], x[0]))
     return  sorted_freq [:n]

x={"a":3,"b":2,"c":1}
print(top_n(x,n=2))