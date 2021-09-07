import sys

sys.stdin = open('input.txt', 'r')
sys.stdout = open('output.txt', 'w')
n = int(input())
k = int(input())
x = n //5
z = n-(x*5)
y=(k-1)+z
if y>5:
    y=y-5
print(y)
