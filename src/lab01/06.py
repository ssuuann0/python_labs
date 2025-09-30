n=int(input())
full=0
dist=0
for i in range(n):
    stud=input().split()
    if stud[-1]=='True':
        full+=1
    if stud[-1]=='False':
        dist+=1
print(full,dist)