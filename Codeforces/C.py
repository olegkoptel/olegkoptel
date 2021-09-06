x = input()
if len(x) % 4 != 0:
    x = x + 'a' * (4 - (len(x) % 4))
s1 = []
g1 = 0
r1 = 0
b1 = 0
y1 = 0
for i in range(0, len(x), 4):
    s1 = x[i:i + 4]
    if 'R' not in s1 and '!' in s1 and 'a' not in s1:
        r1 = r1 + 1
    if 'B' not in s1 and '!' in s1 and 'a' not in s1:
        b1 = b1 + 1
    if 'Y' not in s1 and '!' in s1 and 'a' not in s1:
        y1 = y1 + 1
    if 'G' not in s1 and '!' in s1 and 'a' not in s1:
        g1 = g1 + 1
    elif 'a' in s1 and '!' in s1:
        z = s1.find('!')
        while x[z] == '!':
            z = z + 4
        if x[z] == 'R':
            r1 = r1 + 1
        elif x[z] == 'B':
            b1 = b1 + 1
        elif x[z] == 'Y':
            y1 = y1 + 1
        elif x[z] == 'G':
            g1 = g1 + 1
print(r1, b1, y1, g1)
#гирлянда