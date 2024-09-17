import sqlite3

# Создание соединения к БД
conn = sqlite3.connect('Task_105/films.db')
cursor = conn.cursor()

# Создание таблицы для фильмов, если её нету
cursor.execute('''CREATE TABLE IF NOT EXISTS films
                 (title TEXT, genre TEXT, release_year INTEGER)''')


def add_film(title, genre, release_year):
    # Проверка на существование фильма в БД
    cursor.execute("SELECT * FROM films WHERE title=? AND genre=? AND release_year=?", (title, genre, release_year))
    if cursor.fetchone():
        # Обновляем существующую запись
        cursor.execute("UPDATE films SET title=?, genre=?, release_year=? WHERE title=? AND genre=? AND release_year=?", (title, genre, release_year, title, genre, release_year))
        print(f'{title} обновлён.\n')
    else:
        # Вставляем новую запись в БД
        cursor.execute("INSERT INTO films VALUES (?, ?, ?)", (title, genre, release_year))
        print(f'{title} добавлен в список.\n')
    conn.commit()


def remove_film(title):
    if title in [row[0] for row in cursor.execute("SELECT title FROM films")]:
        cursor.execute("DELETE FROM films WHERE title = ?", (title,))
        conn.commit()
        print(f'{title} удален из списка.')
    else:
        print(f'{title} не найден в списке.')



add_film('Возрождение Шаошанка', 'Драма', 1994)
add_film('Крестный отец', 'Криминал', 1972)

print(list(cursor.execute("SELECT * FROM films")))

remove_film('Возрождениеаошанка')
remove_film('Возрождение Шаошанка')

print("\nСписок всех фильмов в БД: " , list(cursor.execute("SELECT * FROM films")), '\n')

# Отсоединяемся от БД
conn.close()
