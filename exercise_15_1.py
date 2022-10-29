# Exercise 15.1 Database Email

import sqlite3

conn = sqlite3.connect('emaildb.sqlite')
print('sql connection:', conn, type(conn), dir(conn))
cur = conn.cursor()
print('connection cursor:', cur, type(cur), dir(cur))

cur.execute('DROP TABLE IF EXISTS Counts')
cur.execute('''
CREATE TABLE Counts (email TEXT, count INTEGER)''')

fname = input('Enter file name: ')
if len(fname) < 1 : fname = 'mbox-short.txt'
hand = open(fname)
for line in hand :
    if not line.startswith('From: ') : continue
    words = line.split()
    email = words[1]
    cur.execute('SELECT count FROM Counts WHERE email = ?', (email,))
    row = cur.fetchone()
    if row is None :
        cur.execute('INSERT INTO Counts (email, count) VALUES (?, 1)', (email,))
    else :
        cur.execute('UPDATE Counts SET count = count + 1 WHERE email = ?', (email,))
    conn.commit()

print('sql connection:', conn, type(conn), dir(conn))
print('connection cursor:', cur, type(cur), dir(cur))
sel = 'SELECT email, count FROM Counts ORDER BY count DESC LIMIT 10'
for row in cur.execute(sel) :
    print(row[0], row[1])

cur.close()