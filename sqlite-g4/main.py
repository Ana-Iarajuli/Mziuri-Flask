import sqlite3

conn = sqlite3.connect('books.sqlite')
cursor = conn.cursor()

# cursor.execute('''CREATE TABLE books
#                 (id INTEGER PRIMARY KEY AUTOINCREMENT,
#                 title VARCHAR(50),
#                 author VARCHAR(100),
#                 price FLOAT);
# ''')

# cursor.execute("INSERT INTO books (title, author, price) VALUES ('Hamlet', 'William Shakespeare', 10.5)")
# conn.commit()

# b_title = 'Jayos Xiznebi'
# b_author = 'Mixeil Javaxishvili'
# b_price = 0
#
# book1 = (b_title, b_author, b_price)
#
# cursor.execute("INSERT INTO books (title, author, price) VALUES (?, ?, ?)", book1)
# conn.commit()

# book_list = [
#             ('The Book Thief', 'Markus Zusak', 17 ),
#             ('Animal Farm', 'George Orwell', 13 ),
#             ('The Hunger Games', 'Suzanne Collins', 17 ),
#             ('Harry Potter and the Prisoner of Azkaban', 'Rowling',  25),
#             ('Harry Potter and the Goblet of Fire', 'Rowling', 24 ),
#             ('გამზრდელი', 'აკაკი წერეთელი', 8),
#             ('ჩემი თავგადასავალი', 'აკაკი წერეთელი', 8),
#             ('განდეგილი', 'ილია ჭავჭავაძე', 10 ),
#             ('ვეფხისტყაოსანი', 'შოთა რუსთაველი', 29)
#         ]
# cursor.executemany("INSERT INTO books (title, author, price) VALUES (?, ?, ?)", book_list)
# conn.commit()

cursor.execute("SELECT * FROM books;")
record = cursor.fetchone()
print(record)

record = cursor.fetchone()
print(record)

record = cursor.fetchone()
print(record)
print("Author is ", record[2])
# records = cursor.fetchmany(8)
#
# for record in records:
#     print(record)



conn.close()