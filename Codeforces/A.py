s1 = []
x = 0
n = int(input())
for i in range(n):
    s = input()
    if i > 0:
        for j in range(len(s)):
            if s[j] != s1[j]:
                x = x + 1
    s1 = s
if (x // n) - 1 <= 0:
    print(0)
else:
    print((x // n) - 1)
# бары
