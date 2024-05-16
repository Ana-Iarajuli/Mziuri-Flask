from flask import Flask, render_template, url_for, redirect, request

app = Flask(__name__)

books = [
    {'id': 1, 'title': 'Book 1', 'author': 'Author 1', 'year': '2020'},
    {'id': 2, 'title': 'Book 2', 'author': 'Author 2', 'year': '2021'},
    {'id': 3, 'title': 'Book 3', 'author': 'Author 3', 'year': '2022'}
]


@app.route('/')
def index():
    return render_template('index.html', books=books)


@app.route('/book/<int:book_id>')
def book(book_id):
    book = next((book for book in books if book['id'] == book_id))
    if book:
        return render_template('book.html', book=book)
    else:
        return "Book not found", 404


@app.route('/add_book', methods=['GET', 'POST'])
def add_book():
    if request.method == 'POST':
        title = request.form['title']
        author = request.form['author']
        year = request.form['year']
        new_book = {'id': len(books) + 1, 'title': title, 'author': author, 'year': year}
        books.append(new_book)
        return redirect(url_for('index'))
    return render_template('add_book.html')


if __name__ == '__main__':
    app.run(debug=True)
