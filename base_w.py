import sqlite3
import random

def init(user_id, user_username):
    conn = sqlite3.connect('base.db')
    cursor = conn.cursor()
    cursor.execute('INSERT INTO users (id, phone, username) VALUES (?, ?, ?)',(user_id, None, user_username))
    conn.commit()
    cursor.close()
    conn.close()

def users():
    conn = sqlite3.connect('base.db')
    cursor = conn.cursor()

    cursor.execute('SELECT id FROM users ')
    write = cursor.fetchall()

    conn.commit()
    cursor.close()
    conn.close()
    wr = []
    for i in write:
        wr.append(i[0])
    return wr

def select_number(user_id):
    conn = sqlite3.connect('base.db')
    cursor = conn.cursor()
    cursor.execute('SELECT phone FROM users WHERE id=:user_id', {'user_id': user_id})
    write = cursor.fetchone()
    conn.commit()
    cursor.close()
    conn.close()
    return write

def create_sale(text, photo, answers):
    conn = sqlite3.connect('base.db')
    cursor = conn.cursor()
    cursor.execute('INSERT INTO vote (textq, photo, answers) VALUES (?, ?, ?)', (text, photo, answers))
    conn.commit()
    cursor.close()
    conn.close()

def select_one_sale():
    conn = sqlite3.connect('base.db')
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM vote')
    write = cursor.fetchall()
    conn.commit()
    cursor.close()
    conn.close()
    return random.choice(write)

def update(user_id, phone):
    conn = sqlite3.connect('base.db')
    cursor = conn.cursor()
    cursor.execute('UPDATE users SET phone=:phone WHERE id=:user_id', {'phone': phone, 'user_id': user_id})
    conn.commit()
    cursor.close()
    conn.close()

def create_razdel(name_of):
    conn = sqlite3.connect('base.db')
    cursor = conn.cursor()
    cursor.execute('INSERT INTO parts (title, photo_id,texts) VALUES (?, ? ,?)', (name_of,None,' '))
    conn.commit()
    cursor.close()
    conn.close()

def add_text_to_rezel(texts, title):
    conn = sqlite3.connect('base.db')
    cursor = conn.cursor()
    cursor.execute('SELECT texts FROM parts WHERE title=:title', {'title': title})
    write = cursor.fetchone()
    texts = write[0] + texts
    cursor.execute('UPDATE parts SET texts=:texts WHERE title=:title', {'title': title, 'texts': texts})
    conn.commit()
    cursor.close()
    conn.close()

def save_photo(photo_id, title):
    conn = sqlite3.connect('base.db')
    cursor = conn.cursor()
    cursor.execute('UPDATE parts SET photo_id=:photo_id WHERE title=:title', {'title': title, 'photo_id': photo_id})
    conn.commit()
    cursor.close()
    conn.close()

def all_name_of_razdel():
    conn = sqlite3.connect('base.db')
    cursor = conn.cursor()
    cursor.execute('SELECT title FROM parts')
    write = cursor.fetchall()
    conn.commit()
    cursor.close()
    conn.close()
    wr = []
    for i in write:
        wr.append(i[0])
    return wr

def on_razdel(name_of):
    conn = sqlite3.connect('base.db')
    cursor = conn.cursor()
    cursor.execute('UPDATE parts SET is_on=:is_on', {'is_on': False})
    cursor.execute('UPDATE parts SET is_on=:is_on WHERE title=:title', {'title': name_of, 'is_on': True})
    conn.commit()
    cursor.close()
    conn.close()

def set_razdel():
    conn = sqlite3.connect('base.db')
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM parts WHERE is_on=:is_on', {'is_on': '1'})
    write = cursor.fetchone()
    conn.commit()
    cursor.close()
    conn.close()
    return write

def off_razdel():
    conn = sqlite3.connect('base.db')
    cursor = conn.cursor()
    cursor.execute('UPDATE parts SET is_on=:is_on', {'is_on': False})
    conn.commit()
    cursor.close()
    conn.close()

def delete_razdel(name):
    conn = sqlite3.connect('base.db')
    cursor = conn.cursor()
    cursor.execute('DELETE FROM parts WHERE title=:title', {'title': name})
    conn.commit()
    cursor.close()
    conn.close()