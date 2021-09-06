n = int(input())
s2 = []
f = 0
s4 = []
s3 = []
s1 = []
for i in range(n):
    s = [s for s in input().split()]
    if s[1] == 'South' and sum(s1) < 20000 and sum(s3) < 20000 and int(s[0]) <= 20000:
        s1.append(int(s[0]))
    elif s[1] == 'East' and i > 0 and sum(s1) < 20000 and sum(s3) < 20000 :
        s2.append(int(s[0]))
    elif s[1] == 'North' and i > 0 and sum(s1) < 20000 and sum(s3) < 20000 and int(s[0]) <= 20000:
        s3.append(int(s[0]))
    elif s[1] == 'West' and i > 0 and sum(s1) < 20000 and sum(s3) < 20000 :
        s4.append(int(s[0]))
    elif s[1] == 'North' and sum(s1) == 20000 and sum(s3) < 20000 and int(s[0]) < 20000:
        s3.append(int(s[0]))
        s1.clear()
    elif s[1] == 'South' and sum(s3) == 20000 and sum(s1) < 20000 and int(s[0]) < 20000:
        s1.append(int(s[i]))
        s3.clear()
    elif s[1] == 'South' and int(s[0]) > 20000:
        if (int(s[0]) / 20000) < 2:
            s3.append(int(s[0]) - 20000)
        elif (int(s[0]) / 20000) % 2 == 0 and int(s[0]) / 20000 == int:
            s3.append(20000)
        elif (int(s[0]) / 20000) % 2 != 0 and int(s[0]) / 20000 == int:
            s1.append(20000)
        elif (int(s[0]) / 20000) == float and (int(s[0]) // 20000) % 2 != 0 and (int(s[0]) / 20000) > 2:
            s3.append(int(s[0]) - (20000 * (int(s[0]) // 20000)))
        elif (int(s[0]) / 20000) == float and (int(s[0]) // 20000) % 2 == 0 and (int(s[0]) / 20000) > 2:
            s1.append(int(s[0]) - (20000 * (int(s[0]) // 20000)))
    elif s[1] == 'North' and int(s[0]) > 20000:
        if (int(s[0]) / 20000) < 2:
            s1.append(int(s[0]) - 20000)
        elif (int(s[0]) / 20000) % 2 == 0 and int(s[0]) / 20000 == int:
            s1.append(20000)
        elif (int(s[0]) / 20000) % 2 != 0 and int(s[0]) / 20000 == int:
            s3.append(20000)
        elif (int(s[0]) / 20000) == float and (int(s[0]) // 20000) % 2 != 0 and (int(s[0]) / 20000) > 2:
            s1.append(int(s[0]) - (20000 * (int(s[0]) // 20000)))
        elif (int(s[0]) / 20000) == float and (int(s[0]) // 20000) % 2 == 0 and (int(s[0]) / 20000) > 2:
            s3.append(int(s[0]) - (20000 * (int(s[0]) // 20000)))
    else:
        f = 1
if sum(s3) == 20000:
    s3.clear()
if sum(s1) != sum(s3):
    f = 1
if f == 1:
    print('NO')
else:
    print('YES')
# Северный полюс
