from tkinter import *
def handler1(event):
    print("hello world x=", event.x, "y=", event.y)

def handler2(event):
    exit()


#инициализация
root = Tk()
hello_label = Label(root, text='Hello World ', font="times 40")
hello_label.pack()

#привязка оброботчиков к паре (событие, виджет)
hello_label.bind('<Button-1>', handler1)
hello_label.bind('<Button-3>', handler2)

#главный цкл(проэкт)
root.mainloop()

print('Программа заканчивается. Вышли из главного цикла.')