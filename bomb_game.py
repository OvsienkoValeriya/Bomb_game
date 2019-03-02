import tkinter as tk
from tkinter import *


ok_to_press_return = True
bomb = 100
day = 0

def start(event):
    global ok_to_press_return
    if ok_to_press_return == False:
        pass
    else:
        start_label.config(text="")
        update_bomb()
        update_day()
        update_display()

        ok_to_press_return = False

def update_display():
    global bomb, day
    if bomb<=50:
        bomb_normal.config(image = no_photo)
    else:
        bomb_normal.config(image = normal_photo)
    bomb_label.config(text = "Фитиль:" + str(bomb))
    day_label.config(text = "День:" + str(day))
    bomb_normal.after(100, update_display)

def update_bomb():
    global bomb
    bomb -= 1
    if is_alive():
        bomb_label.after(500, update_bomb)

def update_day():
    global day
    day += 1
    if is_alive():
        day_label.after(5000, update_day)

def stop():
    global bomb
    if is_alive():
        if bomb <= 79:
            bomb += 20
        else:
            bomb -= 20

def is_alive():
    global bomb
    if bomb <= 0:
        start_label.config(text = "Bang! Bang!")
        bomb_normal.config (image = bang_photo)
        return False
    else:
        return True

root = tk.Tk()
root.title ("Bang bang!")
root.geometry("500x500+0+0")

start_label = Label(root, text="Нажми Enter, чтобы начать игру", font = ("Helvetica", 12))
bomb_label = Label(root, text="Фитиль:" + str(bomb), font = ("Helvetica", 12))
day_label = Label(root, text="День:" + str(day), font = ("Helvetica", 12))

no_photo = PhotoImage(file="bomb_no.gif")
normal_photo = PhotoImage(file="bomb_normal.gif")
bang_photo = PhotoImage(file="bang.gif")

bomb_normal = Label(root, image = normal_photo)
button_no_bomb = Button(root, text = "Нажми меня!", command = stop)

start_label.pack()
bomb_label.pack()
day_label.pack()

bomb_normal.pack()
button_no_bomb.pack()

bang_bang_photo = Label(root, image = bang_photo)
bang_bang_photo.pack()


root.bind("<Return>", start)

root.mainloop()
