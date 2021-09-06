from random import *
n,a,b,c=int(input()),int(input()),int(input()),int(input())
s1=[a,b]
x=c*n
if float(x/n)>float(b):
    print(-1)
else:
    while x > sum(s1):
        y = randint(a, b)
        s1.append(y)
    z = sum(s1) - x
    y = s1[-1]
    s1.remove(y)
    s1.append(y - z)
    print(*s1)
#Бочки с топливом
