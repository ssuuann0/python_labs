name=[]
name=[x for x in input('ФИО:').split()]
print(f'Инициалы: {name[0][:1]}{name[1][:1]}{name[2][:1]}')
print('Длина (символов):',len(name[0])+len(name[1])+len(name[2])+2)