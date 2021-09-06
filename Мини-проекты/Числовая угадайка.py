from random import *
from turtle import *

s=[]
s1=[]
s2=['red','blue','black','orange','purple','green','yellow','pink']
b = 0
y = 0
z = 0
u = 0
x = randint(1, 101)
print("Добро пожаловать в числовую угадайку")


def is_valid(n):
    if n.isdigit() == True:
        if 1 <= int(n) <= 100:
            return True
        else:
            return False
    if n == 'Подсказка':
        return True
    if n == 'Стоп':
        return True
    if n == 'Большой папин живот':
        return True
    else:
        return False


print('Введите число от 1 до 100')
n = input()
while is_valid(n) == False:
    print("Всё-таки введите,пожалуйста,число от 1 до 100")
    n = input()
while n == 'Подсказка' or n == 'Стоп' or n == 'Большой папин живот' or int(n) != x:
    if n != 'Подсказка' and n != 'Большой папин живот' and int(n) > x:
        print("Увы,ваше число больше")
        z = int(n)
        print('Введите новое число или попросите подсказку')
        print('(Чтобы попросить подсказку напишите "Подсказка")')
        print('Если вы хотите выйти введите "Стоп"')
        n = input()
        while is_valid(n) == False:
            print("Всё-таки введите,пожалуйста,число от 1 до 100")
            n = input()

    elif n != 'Подсказка' and n != 'Большой папин живот' and int(n) < x:
        print('Увы,ваше число меньше')
        y = int(n)
        print('Введите новое число или попромите подсказку')
        print('(Чтобы попросить подсказку напишите "Подсказка")')
        n = input()
        while is_valid(n) == False:
            print("Всё-таки введите,пожалуйста,число от 1 до 100")
            n = input()
    elif n == 'Подсказка' and n != 'Большой папин живот':
        if y == 0 and z != 0:
            print('Искомое число меньше чем', z)
        elif y == 0 and z == 0:
            print('Нельзя сразу просить подсказку:)')
        elif y != 0 and z == 0:
            print('Искомое число больше чем', y)
        elif y != 0 and z != 0:
            print('Искомое число больше чем', y, 'и меньше чем', z)
        print('Введите новое число')
        n = input()
        while is_valid(n) == False:
            print("Всё-таки введите,пожалуйста,число от 1 до 100")
            n = input()
    elif n == 'Большой папин живот':
        print('Здравствуйте, мой господин!')
        print('Искомое число :', x)
        u = 1
        break
    elif n == 'Стоп':
        print('Жаль, что вы покидаете нас(((')
        b = 1
        break
if u != 1 and b != 1:
    print('Ура, вы угадали!!!')
    from turtle import *
    t = Turtle()
    t.screen.setup(800, 800)
    t.speed(0)
    t.shape("turtle")
    t.hideturtle()
    t.screen.bgcolor("pink")
    t.pensize(2)
    t.pencolor('orange')
    t.begin_fill()
    t.fillcolor('red')
    t.left(90)
    t.circle(50, 185)
    t.fd(15)
    t.left(35)
    t.fd(150)
    t.left(100)
    t.fd(150)
    t.left(30)
    t.fd(10)
    t.circle(50, 180)
    t.end_fill()
    t.penup()
    t.goto(-55, -50)
    t.write('LOVE', False, font=('cool', 30, 'normal'))
    t.screen.exitonclick()
    t.screen.mainloop()
    print("Возвращайтесь к нам :) ")
elif u==1 and b!=1:
    print("Я нарисовал для вас картину")
    from turtle import *
    t = Turtle()
    t.screen.setup(800, 800)
    for i in range(50):
        s.append(randint(1,14))
        s1.append(randint(10,200))
    for i in range(len(s)):
        if s[i]==1:
            t.left(s1[i])
        elif s[i]==2:
            t.right(s1[i])
        elif s[i]==3:
            t.setheading(randint(20,361))
        elif s[i]==4:
            t.circle(randint(1,100),randint(20,361))
        elif s[i]==5:
            t.fd(s1[i])
        elif s[i]==6:
            t.bk(s1[i])
        elif s[i]==7:
            t.stamp()
        elif s[i]==8:
            t.pencolor(choice(s2))
        elif s[i]==9:
            t.screen.bgcolor(choice(s2))
        t.screen.exitonclick()
        t.screen.mainloop()

