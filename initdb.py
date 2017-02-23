import sqlite3 as lite

con = lite.connect('database.db')
print('Database created')

con.execute('CREATE TABLE IF NOT EXISTS movies (title TEXT, genre TEXT)')
print('Table created')

con.close()

