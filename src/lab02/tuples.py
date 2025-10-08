def format_record(rec):
    if len(rec)!=3:
        return 'ValueError'
    if len(rec)==3 and type(rec[2]) is not float:
        return 'TypeError'
    name=[]
    name.append(rec[0].split())
    fullinit=''#имя+инициалы
    fullinit=fullinit+name[0][0][0].upper()+name[0][0][1:]+' '+name[0][1][0].upper()+'.'
    if len(name[0])==3:
        fullinit=fullinit+name[0][2][0].upper()+'.'
    group=rec[1]
    gpa=f'{rec[2]:.2f}'
    final=f'{fullinit},гр. {group},GPA {gpa}'
    return final
n=("Иванов Иван Иванович", "BIVT-25", 4.6)
print(format_record(n))
n=("Петров Пётр", "IKBO-12", 5.0)
print(format_record(n))
n=("Петров Пётр Петрович", "IKBO-12", 5.0)
print(format_record(n))
n=("  сидорова  анна   сергеевна ", "ABB-01", 3.999)
print(format_record(n))
n=( "ABB-01", 3.999)
print(format_record(n))