from tkinter import *
window = Tk()
l = Label(text="Вас приветствует шифровальщик Цезаря!")
l1 = Label(text="Введи в меня сообщение, которое нужно зашифровать или расшифровать")
e = Entry(width=100)
l2 = Label(text="Теперь введи язык, с которым мы работаем(Английский-en,Русский-ru)")
e1 = Entry()
l3 = Label(
    text="Теперь определим, что нам нужно сделать: Если нам нужно зашифровать сообщение, то мы вводим left или right в зависимости от направления сдвига, ",
)
l4=Label(text="eсли мы хотим расшифровать сообщение, то мы вводим обратное направление от того, какое было использовано при шифровке")
e2 = Entry()
l5=Label(text="И,наконец, введите величину сдвига")
e3=Entry()
l6=Label(text="Ваш ответ:")
l7=Label(width=200,height=5,bg="black",fg="white")
def press():
    f=0
    s=e.get()
    x=e1.get()
    y=e2.get()
    n=int(e3.get())
    s1 = ''
    s2 = ' !@"#№$;%:^?&*()_-+=\,/|.><~`'
    if x == 'en':
        if y == 'left':
            for i in range(len(s)):
                if s[i].isalpha()==True:
                    m = ord(s[i]) - n
                    if s[i].isupper() == True:
                        if m < 65:
                            m = 91 - (65 - m)
                    elif s[i].islower() == True:
                        if m < 97:
                            m = 123 - (97 - m)
                    s1 = s1 + str(chr(m))
                else:
                    s1 = s1 + s[i]
        elif y == 'right':
            for i in range(len(s)):
                if s[i].isalpha()==True:
                    m = ord(s[i]) + n
                    if s[i].isupper() == True:
                        if m > 90:
                            m = (m - 90) + 64
                    elif s[i].islower() == True:
                        if m > 122:
                            m = (m - 122) + 96
                    s1 = s1 + str(chr(m))
                else:
                    s1 = s1 + s[i]
    elif x == 'ru':
        if y == 'left':
            for i in range(len(s)):
                if s[i].isalpha()==True:
                    m = ord(s[i]) - n
                    if s[i].isupper() == True:
                        if m < 1040:
                            m = 1072 - (1040 - m)
                    elif s[i].islower() == True:
                        if m < 1072:
                            m = 1104 - (1072 - m)
                    s1 = s1 + str(chr(m))
                else:
                    s1 = s1 + s[i]
        elif y == 'right':
            for i in range(len(s)):
                if s[i].isalpha()==True:
                    m = ord(s[i]) + n
                    if s[i].isupper() == True:
                        if m > 1071:
                            m = (m - 1071) + 1039
                    elif s[i].islower() == True:
                        if m > 1103:
                            m = (m - 1103) + 1071
                    s1 = s1 + str(chr(m))
                else:
                    s1 = s1 + s[i]
        else:
            f=1
    else:
        f=1
    if f!=1:
        text = l7["text"]
        l7["text"] = s1
    else:
        text = l7["text"]
        l7["text"] = "Введите данные корректно"


b = Button(
    master=window,
    text="Нажми",
    command=press
)
l.pack()
l1.pack()
e.pack()
l2.pack()
e1.pack()
l3.pack()
l4.pack()
e2.pack()
l5.pack()
e3.pack()
b.pack()
l6.pack()
l7.pack()
window.mainloop()