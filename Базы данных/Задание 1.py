import sqlite3
from time import time
# 1. Вывести список книг
# 2. Вывести список читателей
# 3. Добавить книгу.
# 4. Добавить читателя.
# 5. Выдать книгу читателю
# 6. Принять книгу.


def out_list_books(c):
    c.execute("select id, title from Books;")
    print(*c.fetchall())
    return


def out_list_readers(c):
    c.execute("select id, name from Readers;")
    print(*c.fetchall())
    return


def out_list_records(c):
    c.execute("select * from Records;")
    print(*c.fetchall())
    return



def add_book(c, value):
    c.execute("select count(id) from Books;")
    index = int(c.fetchone()[0]+1)
    c.execute("insert into Books values (?, ?, ?, ?)", (index, *value))
    # conn.commit()
    return


def add_reader(c, value):
    c.execute("select count(id) from Readers;")
    index = c.fetchone()[0]+1
    c.execute("insert into Readers values (?, ?)", [index, value])
    # conn.commit()
    return


def out_book(c, book, reader):
    c.execute("select id from Readers where name = ?", [reader])
    id_reader = c.fetchone()[0]
    c.execute("select id from Books where title = ?", [book])
    id_book = c.fetchone()[0]
    data = time()
    c.execute("insert into Records values (?, ?, ?, ?)", [id_reader, id_book, data, None])
    # conn.commit()
    return


def in_book(c, book):
    data = time()
    c.execute("select id from Books where title = ?", [book])
    id_book = c.fetchone()[0]
    c.execute("update Records set returning_date = ? where book_id = ? and returning_date = NULL", [data, id_book])
    # conn.commit()
    return

print(time())
conn = sqlite3.connect("Upraznenie_1.db")
c = conn.cursor()
# out_list_books(c)
# out_list_readers(c)
# add_book(c, [(8, 'sdg', 'shf', 2356)])
# out_list_books(c)
# add_reader(c, [(7, 'Tim')])
# out_list_readers(c)
# out_list_records(c)
# out_book(c, 'Why?', 'Anna')
# out_list_records(c)
# in_book(c, 'Why?')
# out_list_records(c)
print('Здрасте! Данная программа предоставляет следующие услиги:\n1. Вывести список книг.\n2. Вывести список читателей'
      '\n3. Добавить книгу.\n4. Добавить читателя.\n5. Выдать книгу читателю\n6. Принять книгу.\nВведите номер услиги:')
while True:
    n = int(input())
    if n == 1:
        print('Вы выбрали "Вывести список книг". \nВ данный момент в нашем распоряжении находятся следующие книги:\n')
        out_list_books(c)
    elif n == 2:
        print('Вы выбрали "Вывести список читателей". \nВ данный момент нашими читателями являются:\n')
        out_list_readers(c)
    elif n == 3:
        print('Вы выбрали "Добавить книгу". \nПредоставьте информацию о книге в следующем виде:\n имя автора, название книги, год публикации')
        value = list(input().split(', '))
        value[2] = int(value[2])
        add_book(c, value)
    elif n == 4:
        print('Вы выбрали "Добавить читателя". \nПредоставьте информацию о читателе в следующем виде:\n имя читателя')
        value = input()
        add_reader(c, value)
    elif n == 5:
        print('Вы выбрали "Выдать книгу читателю". \nПредоставьте информацию о книге и читателе в следующем виде:\n название книги, имя читателя')
        value = list(input().split(', '))
        out_book(c, *value)
    elif n == 6:
        print(
            'Вы выбрали "Принять книгу". \nПредоставьте информацию о книге в следующем виде:\n название книги')
        value = input()
        in_book(c, value)
    else:
        print('Что-то пошло не так. Попробуйте еще раз')
    print('Список услиг:\n1. Вывести список книг.\n'
    '2. Вывести список читателей\n'
    '3. Добавить книгу.\n'
    '4. Добавить читателя.\n'
    '5. Выдать книгу читателю\n'
    '6. Принять книгу.\nВведите номер услиги:')




