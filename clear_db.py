import sqlite3

db = sqlite3.connect('./bot.db')
cursor = db.cursor()
cursor.execute('''
    DROP TABLE users
''')
db.commit()

db.close()