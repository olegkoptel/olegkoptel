n=int(input())
x=0
a=list(map(int,input().split()))
m=int(input())
b=list(map(int,input().split()))
if n<=m:
    for i in range(n):
        if a[i] in b :
            x+=1
            b.remove(a[i])
        elif (a[i]+1) in b:
            x+=1
            b.remove(a[i]+1)
if m<n:
    for i in range(m):
        if a[i] in b :
            x+=1
            b.remove(a[i])
        elif (a[i]+1) in b:
            x+=1
            b.remove(a[i]+1)
print(x)
#балы

