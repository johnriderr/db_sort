import tkinter as tk
import json
from functools import partial

root = tk.Tk()
root.title("Сортировщик баз")


def center(win):
    win.update_idletasks()
    width = win.winfo_width()
    height = win.winfo_height()
    x = (win.winfo_screenwidth() // 2) - (width // 2)
    y = (win.winfo_screenheight() // 2) - (height // 2)
    win.geometry('{}x{}+{}+{}'.format(width, height, x, y))


def create_db(countries, country):
    new_db = []
    with open('db.txt', 'r') as f:
        for line in f.readlines():
            for mail_domain in countries[country]:
                if mail_domain in line:
                    new_db.append(line)

    with open('db_'+country+'.txt', 'w') as f:
        f.write(''.join(new_db))


def create_db_without(countries, country):
    new_db = []
    with open('db.txt', 'r') as f:
        for line in f.readlines():
            for mail_domain in countries[country]:
                if mail_domain not in line:
                    new_db.append(line)

    with open('db_no_'+country+'.txt', 'w') as f:
        f.write(''.join(new_db))


with open('countries.cfg') as f:
    countries  = json.loads(f.read())['countries']
    for i, country in enumerate(countries):
        b = tk.Button(root, text='Создать ' + country + ' базу', height = 2, width = 25)
        b.grid(row=i+1, column=0)
        action_with_arg = partial(create_db, countries, country)
        b.config(command=action_with_arg)

    for i, country in enumerate(countries):
        b = tk.Button(root, text='Создать базу без ' + country, height = 2, width = 25)
        b.grid(row=i+1, column=1)
        action_with_arg = partial(create_db_without, countries, country)
        b.config(command=action_with_arg)

l = tk.Label(root, text = 'by j_rider', font=("Comic Sans MS", 6, "bold"))
l.grid(row=i+2, column=1)
center(root)
root.mainloop()
