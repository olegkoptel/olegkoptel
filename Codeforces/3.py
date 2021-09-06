#алфавитная строка
t=int(input())
for i in range(t):
    f=0
    s=input()
    n=len(s)
    x=s.find('a')
    y=x
    for i in range(1,n):
        z=chr(97+n)
        if (s.find(z)-1)==x:
            x+=1
            continue
        elif (s.find(z)+1)==y:
            y-=1
            continue
        else:
            f=1
            break
    if f==0:
        print('YES')
    else:
        print('NO')