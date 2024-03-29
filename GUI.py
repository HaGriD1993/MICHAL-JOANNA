from tkinter import *
from tkinter import filedialog
from pygame import mixer
import projekt
from tkinter import font

# window define section
window_main = Tk()
window_main.title("Projekt Joanna i Michał (i Bartek :) )")
window_main.minsize(width=380,height=410)
window_main.maxsize(width=380,height=410)
window_main.configure(bg = "#967BB6")

fileToOpen = ""

def open_file():
    global fileToOpen
    fileToOpen= filedialog.askopenfile(mode ='r', filetypes =[('Data files', '*.data')])
    if fileToOpen is not None:
        content = fileToOpen.read()
        print(content)
def delete():
    label_x1.config(text = " ")
    label_x2.config(text = " ")
    label_x3.config(text = " ")
    label_x4.config(text = " ")
    label_x5.config(text = " ")
    label_x6.config(text = " ")
def insert():
    wartosci = projekt.wczytajPlik(fileToOpen.name)

    label_x1.config(text= wartosci[0])
    label_x2.config(text= wartosci[1])
    label_x3.config(text= wartosci[2])
    label_x4.config(text= wartosci[3])
    label_x5.config(text= wartosci[4])
    label_x6.config(text= wartosci[5])
def music_on():
    mixer.music.load("Goosebumps Theme.mp3")
    mixer.music.play()
def music_off():
    mixer.music.stop()

my_font = font.Font(family='Monospace', size=10, weight='bold')
mixer.init()

button_0 = Button(window_main, text = "Wybierz Plik do wczytania", width = 30,command = open_file ,
                               bg = "black",fg ="white",font = my_font)
button_0.grid(row = 0, column = 0)

label_1 = Label(window_main, width = "24" ,height = "3" ,bg="#967BB6",font = my_font,
                             text = "Liczba osób od 18 - 25 r.ż\nzarabiajacych od 50 tys.zł")
label_2 = Label(window_main, width = "22" ,height = "3" ,bg="#967BB6",font = my_font,
                             text = "Liczba osób od 18 - 25 r.ż\nzarabiających poniżej 50 tys.zł")
label_3 = Label(window_main, width = "24" ,height = "3" ,bg="#967BB6",font = my_font,
                             text = "Liczba mężczyzn od 18 - 25 r.ż\nzarabiajacych powyżej 50 tyś.zł")
label_4 = Label(window_main, width = "24" ,height = "3" ,bg="#967BB6",font = my_font,
                             text = "Liczba mężczyzn od 18 - 25 r.ż\nzarabiających poniżej 50 tyś.zł")
label_5 = Label(window_main, width = "24" ,height = "3" ,bg="#967BB6",font = my_font,
                             text = "Liczba kobiet od 18 - 25 r.ż\nzarabiających powyżej 50 tyś.zł")
label_6 = Label(window_main, width = "24" ,height = "3" ,bg="#967BB6",font = my_font,
                             text ="Liczba kobiet od 18 - 25 r.ż\nzarabiających ponizej 50 tyś.zł")

label_1.grid(row = 1, column = 0)
label_2.grid(row = 2, column = 0)
label_3.grid(row = 3, column = 0)
label_4.grid(row = 4, column = 0)
label_5.grid(row = 5, column = 0)
label_6.grid(row = 6, column = 0)

label_x1 = Label(window_main,width = "5",bg ="#0D95E2",fg ="white",font = my_font)
label_x2 = Label(window_main,width = "5",bg ="#0D95E2",fg ="white",font = my_font)
label_x3 = Label(window_main,width = "5",bg ="#0D95E2",fg ="white",font = my_font)
label_x4 = Label(window_main,width = "5",bg ="#0D95E2",fg ="white",font = my_font)
label_x5 = Label(window_main,width = "5",bg ="#0D95E2",fg ="white",font = my_font)
label_x6 = Label(window_main,width = "5",bg ="#0D95E2",fg ="white",font = my_font)

label_x1.grid(row = 1, column = 1)
label_x2.grid(row = 2, column = 1)
label_x3.grid(row = 3, column = 1)
label_x4.grid(row = 4, column = 1)
label_x5.grid(row = 5, column = 1)
label_x6.grid(row = 6, column = 1)

button_1 = Button(window_main, text = "Usuń Dane", width = 13,command = delete,bg = "black",fg ="white",font = my_font)
button_1.grid(row = 7, column = 0)
button_2 = Button(window_main, text = "Wczytaj Dane",width = 13,command = insert,bg = "black",fg ="white",font = my_font)
button_2.grid(row = 7, column = 1)
button_3 = Button(window_main, text = "Muzyka ON", width = 13,command = music_on,bg = "black",fg ="white",font = my_font)
button_3.grid(row = 8, column = 0)
button_4 = Button(window_main, text = "Muzyka OFF",width = 13,command = music_off,bg = "black",fg ="white",font = my_font)
button_4.grid(row = 8, column = 1)


window_main.mainloop()