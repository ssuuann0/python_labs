s=input()
ind=0
for i in s:
    if i not in 'QWERTYUIOPLKJHGFDSAZXCVBNM':
        ind+=1
    else:
        break
s1=s[ind:]
step=0
for i in s1:
    if i not in '0123456789':
        step+=1
    else:
        step+=1
        break
ind=-1
finall=''
for i in s1:
    ind+=1
    if i != '.':
        if ind%step==0:
            finall+=i
    else:
        finall+='.'
        break
print(finall)