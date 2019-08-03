import sqlite3

db = sqlite3.connect('./bot.db')
cursor = db.cursor()
cursor.execute('''
    CREATE TABLE users(name TEXT PRIMARY KEY, url TEXT, time INTEGER)
''')
db.commit()

db.close()