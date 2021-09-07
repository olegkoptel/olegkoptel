# 929 930 938 945 946 947

# Ввод нескольких переменных в строчку
a, b, c = map(int, input().split())



#Ввод матрицы в строчку:
n,m=int(input()),int(input())
s=[]
for i in range(n):
    a =[]
    for j in range(m):
         a.append(int(input()))
    s.append(a)

# Ввод массива в строчку
s = []
s = list(map(int, input().split()))
x = 0
y = 0
a = s[0]
b = s[0]

# В строчку(2):
s = [int(s) for s in input().split()]
x = 0
y = 0
a = s[0]
b = s[0]

# В столбик:
n = int(input())
x = 0
y = 0
s = []
for i in range(n):
    s.append(int(input()))
print(*s)
a = s[0]
b = s[0]

# Создание пустой матрицы(1):
N = 3
M = 2
A = []
for i in range(N):
    A.append([0] * M)

# Создание пустой матрицы(2):
N = 3
M = 2
A = [[0] * M for i in range(N)]

# Вывод матрицы(1):
for i in range(len(A)):
    for j in range(len(A[i])):
        print(A[i][j], end=' ')
    print()

# Вывод матрицы(2):
for row in A:
    for elem in row:
        print(elem, end=' ')
    print()

# Ввод матрицы(1):
A = []
n = int(input())
for i in range(n):
    A.append(list(map(int, input().split())))

# Ввод матрицы(2):
A = []
for i in range(n):
    row = input().split()
    for i in range(len(row)):
        row[i] = int(row[i])
    A.append(row)

# Подсчёт времени, затрачиваемого программой:
import time

t0 = time.clock()
print("Hello")
t1 = time.clock() - t0
print("Time elapsed: ", t1 - t0)

# Модуль math:
# math.ceil(X) – округление до ближайшего большего числа.

# math.copysign(X, Y) - возвращает число, имеющее модуль такой же, как и у числа X, а знак - как у числа Y.

# math.fabs(X) - модуль X.

# math.factorial(X) - факториал числа X.

# math.floor(X) - округление вниз.

# math.fmod(X, Y) - остаток от деления X на Y.

# math.frexp(X) - возвращает мантиссу и экспоненту числа.

# math.ldexp(X, I) - X * 2i. Функция, обратная функции math.frexp().

# math.fsum(последовательность) - сумма всех членов последовательности. Эквивалент встроенной функции sum(), но math.fsum() более точна для чисел с плавающей точкой.

# math.isfinite(X) - является ли X числом.

# math.isinf(X) - является ли X бесконечностью.

# math.isnan(X) - является ли X NaN (Not a Number - не число).

# math.modf(X) - возвращает дробную и целую часть числа X. Оба числа имеют тот же знак, что и X.

# math.trunc(X) - усекает значение X до целого.

# math.exp(X) - eX.

# math.expm1(X) - eX - 1. При X → 0 точнее, чем math.exp(X)-1.

# math.log(X, [base]) - логарифм X по основанию base. Если base не указан, вычисляется натуральный логарифм.

# math.log1p(X) - натуральный логарифм (1 + X). При X → 0 точнее, чем math.log(1+X).

# math.log10(X) - логарифм X по основанию 10.

# math.log2(X) - логарифм X по основанию 2. Новое в Python 3.3.

# math.pow(X, Y) - XY.

# math.sqrt(X) - квадратный корень из X.

# math.acos(X) - арккосинус X. В радианах.

# math.asin(X) - арксинус X. В радианах.

# math.atan(X) - арктангенс X. В радианах.

# math.atan2(Y, X) - арктангенс Y/X. В радианах. С учетом четверти, в которой находится точка (X, Y).

# math.cos(X) - косинус X (X указывается в радианах).

# math.sin(X) - синус X (X указывается в радианах).

# math.tan(X) - тангенс X (X указывается в радианах).

# math.hypot(X, Y) - вычисляет гипотенузу треугольника с катетами X и Y (math.sqrt(x * x + y * y)).

# math.degrees(X) - конвертирует радианы в градусы.

# math.radians(X) - конвертирует градусы в радианы.

# math.cosh(X) - вычисляет гиперболический косинус.

# math.sinh(X) - вычисляет гиперболический синус.

# math.tanh(X) - вычисляет гиперболический тангенс.

# math.acosh(X) - вычисляет обратный гиперболический косинус.

# math.asinh(X) - вычисляет обратный гиперболический синус.

# math.atanh(X) - вычисляет обратный гиперболический тангенс.

# math.erf(X) - функция ошибок.

# math.erfc(X) - дополнительная функция ошибок (1 - math.erf(X)).

# math.gamma(X) - гамма-функция X.

# math.lgamma(X) - натуральный логарифм гамма-функции X.

# math.pi - pi = 3,1415926...

# math.e - e = 2,718281...


# int([x], [основание системы счисления]) - преобразование числа x к целочисленному типу в десятичной системе счисления.
# По умолчанию задана система счисления десятичная, но можно основание от 2 до 36.
# bin(x)[2::] - преобразование целого числа в двоичную строку.
# hex(х)[2::] - преобразование целого числа в шестнадцатеричную строку.
# oct(х)[2::] - преобразование целого числа в восьмеричную строку.




#Создание своей функции(поиск максимума)
s=list(input())
def max1(s):
    a=s[0]

    for i in range(len(s)):
        if s[i]>a:
            a=s[i]
    return(a)
print(max1(s))


#Подсчёт простых чисел на промежутке от 1 до n:
from math import sqrt
z=0
b=int(input())
for i in range(2,b+1):
    x=0
    for j in range(1,int(sqrt(i)+1)):
        if i%j==0:
            x=x+1
        if x>1:
            break
    if x==1:
        z+=1
print(z)

