n = int(input())
s1 = []
s3 = []
s = list(map(int, input().split()))
for i in range(min(s)):
    if min(s) % (i + 1) == 0:
        s1.append(i + 1)
for i in range(len(s)):
    for j in range(len(s1)):
        if s[i] % s1[j] != 0:
            s3.append(s1[j])
for i in range(len(s3)):
    if s3[i] in s1:
        s1.remove(s3[i])
print(len(s1))
#Делитель