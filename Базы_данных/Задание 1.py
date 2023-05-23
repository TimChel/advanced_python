import sqlite3
from time import time
# 1. Вывести список книг
# 2. Вывести список читателей
# 3. Добавить книгу.
# 4. Добавить читателя.
# 5. Выдать книгу читателю
# 6. Принять книгу.


def out_list_books(c):
    c.execute("select * from Books;")
    print(*c.fetchall())
    return


def out_list_readers(c):
    c.execute("select * from Readers;")
    print(*c.fetchall())
    return


def out_list_records(c):
    c.execute("select * from Records;")
    print(*c.fetchall())
    return



def add_book(c, value):
    c.execute("select title from Books where author = ? and title = ? and publish_year = ?", value)
    if c.fetchone() is None:
        c.execute("select count(id) from Books;")
        index = int(c.fetchone()[0]+1)
        c.execute("insert into Books values (?, ?, ?, ?)", [index, *value])
        print('Книга добавлена')
    else:
        print('К сожалению, такая книга уже есть в списке.')
    conn.commit()
    return


def add_reader(c, value):
    c.execute("select name from Readers where name = ?", [value])
    if c.fetchone() is None:
        c.execute("select count(id) from Readers;")
        index = c.fetchone()[0]+1
        c.execute("insert into Readers values (?, ?)", [index, value])
        print('Читатель добавлен')
    else:
        print('К сожалению, такой читатель уже существует.')
    conn.commit()
    return


def out_book(c, value):
    c.execute("select id from Readers where name = ?", [value[3]])
    id_reader = c.fetchone()
    if id_reader is None:
        print('К сожалению, такого читателя нет в наших списках.')
        return
    else:
        id_reader = id_reader[0]
    c.execute("select id from Books where author = ? and title = ? and publish_year = ?", value[:3])
    id_book = c.fetchone()
    if id_book is None:
        print('К сожалению, такой книги нет в наших списках.')
        return
    else:
        id_book = id_book[0]
    c.execute("select returning_date from Records where book_id = ?", [id_book])
    list_in_date = c.fetchall()
    if (None,) not in list_in_date:
        data = time()
        c.execute("insert into Records values (?, ?, ?, ?)", [id_reader, id_book, data, None])
        print('Выдача книги прошла успешно. Интересного чтения!')
    else:
        print('К сожалению, данная книга находится у другого читателя.')
    conn.commit()
    return


def in_book(c, book):
    c.execute("select id from Books where author = ? and title = ? and publish_year = ?", value)
    id_book = c.fetchone()
    if id_book is None:
        print('К сожалению, такой книги нет в наших списках.')
        return
    else:
        id_book = id_book[0]
    c.execute("select returning_date from Records where book_id = ?", [id_book])
    list_in_date = c.fetchall()
    if (None,) in list_in_date:
        data = time()
        c.execute("update Records set returning_date = ? where book_id = ?  and returning_date is NULL", [data, id_book])
        print('Возврат книги успешно произведен. Удачного вам дня!')
    else:
        print('К сожалению, данная книга не числится выданной.')
    conn.commit()
    return


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
      '\n3. Добавить книгу.\n4. Добавить читателя.\n5. Выдать книгу читателю\n6. Принять книгу.\n7. Выйти из программы\nВведите номер услиги:')
a = True
while a:
    n = input()
    if n == '0':
        print('Вы выбрали "Вывести записи выдачи книг": \n')
        out_list_records(c)
    elif n == '1':
        print('Вы выбрали "Вывести список книг". \nВ данный момент в нашем распоряжении находятся следующие книги:\n')
        out_list_books(c)
    elif n == '2':
        print('Вы выбрали "Вывести список читателей". \nВ данный момент нашими читателями являются:\n')
        out_list_readers(c)
    elif n == '3':
        print('Вы выбрали "Добавить книгу". \nПредоставьте информацию о книге в следующем виде:\n имя автора, название книги, год публикации')
        value = list(input().split(', '))
        if len(value) != 3:
            print('Кажется, вы неверно ввели информацию о книге. Попробуйте еще раз')
        else:
            try:
                value[2] = int(value[2])
                add_book(c, value)
            except ValueError:
                print('Кажется, вы ввели неверную дату. Попробуйте еще раз')
                pass
    elif n == '4':
        print('Вы выбрали "Добавить читателя". \nПредоставьте информацию о читателе в следующем виде:\n имя читателя')
        value = input()
        add_reader(c, value)
    elif n == '5':
        print('Вы выбрали "Выдать книгу читателю". \nПредоставьте информацию о книге и читателе в следующем виде:\n'
              ' имя автора, название книги, год публикации, имя читателя')
        value = list(input().split(', '))
        if len(value) != 4:
            print('Кажется,вы неверно ввели информацию о книге и читателе. Попробуйте еще раз.')
        else:
            out_book(c, value)
    elif n == '6':
        print(
            'Вы выбрали "Принять книгу". \nПредоставьте информацию о книге в следующем виде:\n '
            'имя автора, название книги, год публикации')
        value = list(input().split(', '))
        if len(value) != 3:
            print('Кажется, вы неверно ввели информацию о книге. Попробуйте еще раз')
        else:
            in_book(c, value)
    elif n == '7':
        print('До скорой встречи!')
        conn.close()
        break
    else:
        print('Что-то пошло не так. Попробуйте еще раз')
    while True:
        print('Желаете продолжить?\n'
            '1. Да\n'
            '2. Нет')
        n = input()
        if n == '2':
            print('До скорой встречи!')
            conn.close()
            a = False
            break
        elif n == '1':
            print('Список услиг:\n'
                  '0. Вывести записи выдачи книг.\n'
                  '1. Вывести список книг.\n'
                  '2. Вывести список читателей\n'
                  '3. Добавить книгу.\n'
                  '4. Добавить читателя.\n'
                  '5. Выдать книгу читателю\n'
                  '6. Принять книгу.\n'
                  '7. Выйти из программы\n'
                  'Введите номер услиги:')
            break
        else:
            print('Что-то пошло не так. Попробуйте еще раз')





