#Реализовать консольное приложение заметки, с сохранением, чтением, добавлением, редактированием и удалением заметок.
# Заметка должна содержать идентификатор, заголовок, тело заметки и дату/время создания или последнего изменения заметки.
# Сохранение заметок необходимо сделать в формате json или csv формат
# (разделение полей рекомендуется делать через точку с запятой).
# Реализацию пользовательского интерфейса студент может делать как ему удобнее,
# можно делать как параметры запуска программы (команда, данные),
# можно делать как запрос команды с консоли и последующим вводом данных,
# как-то ещё, на усмотрение студента.

# импортируем модуль
from tkinter import *
from tkinter import messagebox
from tkinter.filedialog import askopenfile, asksaveasfile
import csv
from datetime import datetime

file_name = None

def new_file():
    global file_name
    file_name = "  "
    text.delete(1.0, END)


def save_file():
    out = asksaveasfile(mode="w", defaultextension='.csv')
    data = text.get(1.0, END)
    out.write(text)
    out.close()


def save_as():
    out = asksaveasfile(mode="w", defaultextension='.csv')
    data = text.get(1.0, END)
    try:
        out.write(data.rsrrip())
    except Exception:
        messagebox.showerror(" не сохранен ")

def open_file():
    global file_name
    file = askopenfile(title=' выбор файла', filetypes=((' документы( *.csv)', '*.csv'), (' все файлы', '*.*')))
    if file is None:
        return
        text_fild.delete('1.0', END)
        text_fild.insert('1.0', open(file_path, encoding='utf-8').read())

def exit():
    answer = messagebox.askokcancel(' выход', ' вы точно хотите выйти?')
    if answer:
        root.destroy

    # создание окна
root = Tk()
# заголовок
root.title(" Заметки")
# задаем геометрию (widthxheight)
root.geometry('350x200')

text = Text (root, width = 350, height = 200)
text.pack()

menu_bar = Menu (root)
file_menu = Menu (menu_bar)

file_menu.add_command(label = " новый файл ", command = new_file)
file_menu.add_command(label = " открыть файл ", command = open_file)
file_menu.add_command(label=" сохранить", command=save_file)
file_menu.add_command(label = " сохранить как ", command = save_as)
file_menu.add_command(label=" закрыть ",command= exit )
menu_bar.add_cascade(label=" file ", menu=file_menu)


root.config(menu=menu_bar)
# выполнение программы
root.mainloop()
