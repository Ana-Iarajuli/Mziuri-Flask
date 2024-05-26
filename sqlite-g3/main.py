import sqlite3

conn = sqlite3.connect('books.sqlite')
# conn.row_factory = sqlite3.Row
cursor = conn.cursor()


# ცხრილის შექმნა
# cursor.execute('''CREATE TABLE books (
#             id  INTEGER PRIMARY KEY AUTOINCREMENT,
#             title VARCHAR(50),
#             author VARCHAR(100),
#             price FLOAT);
#     ''')
#
# # მონაცემების ჩამატება ცხრილში
# cursor.execute("INSERT INTO books (title, author, price) VALUES ('Hamlet', 'William Shakespeare', 10.5);")
# conn.commit()

# b_title = 'zebuloni'
# b_author = 'jemal qarchxadze'
# b_price = 19.0
#
# book1 = (b_title, b_author, b_price)
#
# cursor.execute('INSERT INTO books (title, author, price) VALUES (?, ?, ?)', book1)
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
#
# cursor.executemany('INSERT INTO books (title, author, price) VALUES (?, ?, ?)', book_list)
# conn.commit()

# cursor.execute("SELECT * FROM books")
# record = cursor.fetchone()
# print(record[1])


#
#
# pr_value = 15
# cursor.execute("SELECT * FROM books WHERE price>:pr", {'pr': pr_value})
# records = cursor.fetchall()
# for record in records:
#     print(record)
#
#
# pr_value = 15
# author_value = 'Rowling'
# cursor.execute("SELECT * FROM books WHERE author=:author_name",{'author_name':author_value})
#
# records = cursor.fetchall()
# for record in records:
#     print(record)
# #
# pr_value = 15
# cursor.execute("SELECT * FROM books WHERE price>?", (pr_value, ))
#

# results = cursor.execute("SELECT author from books").fetchall()
# print(results)
# for row in results:
#     # print(dict(row))
#     print(row['author'])
# print(result)
# print(tuple(result))
# print(result.keys())
# print(result['author'])
# print(result[1])
#
# results = cursor.execute("SELECT DISTINCT author FROM books").fetchall()
# print(len(results))
# cursor.execute("SELECT count(DISTINCT author) AS count_row FROM books")
# cursor.execute("SELECT * FROM books WHERE author='Rowling'")
# cursor.execute("SELECT * FROM books WHERE author<>'Rowling'")
# cursor.execute("SELECT * FROM books WHERE price>15")
# cursor.execute("SELECT * FROM books WHERE author<>'Rowling' AND price>15")
# cursor.execute("SELECT * FROM books WHERE NOT author='Rowling' AND price>15")
# cursor.execute("SELECT * FROM books ORDER BY author")
# cursor.execute("SELECT * FROM books ORDER BY author DESC")
# cursor.execute("SELECT * FROM books ORDER BY author, price")
#
# query = 'UPDATE books SET price=12 WHERE id=1'
# cursor.execute(query)
# print(cursor.rowcount)
# conn.commit()

# query = 'UPDATE books SET title="Harry Potter Goblet" WHERE author="Rowling" AND price=24'
# cursor.execute(query)
# print(cursor.rowcount)
# conn.commit()
#
#
# cursor = conn.cursor()
query = "DELETE FROM books WHERE author='William Shakespeare'"
cursor.execute(query)
print(cursor.rowcount)
conn.commit()


conn.close()


