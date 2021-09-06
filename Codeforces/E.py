n, m = map(int, input().split())
x = 0
q = 0
c = 0
y = 0
f = 0
s = []
s1 = []
for i in range(n):
    s.append(list(map(int, input().split())))
for i in range(m):
    s1.append(list(map(int, input().split())))
for i in range(n):
    q = q + 1
    for j in range(m):
        if s[i][1] == s1[j][1] and s[i][0] != s1[j][0]:
            f = 1
            s1[j][1] = 'a'
            break

        elif s[i][1] == s1[j][1] and s[i][0] == s1[j][0]:
            c = 1
            s1[j][1] = 'a'
            break
    if f == 1 and c != 1:
        x = x + 1
    if c == 1:
        x = x + 1
        y = y + 1
    c = 0
    f = 0
print(x, y)
# Фломастеры
