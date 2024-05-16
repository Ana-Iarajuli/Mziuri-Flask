from flask import Flask, render_template, url_for, redirect, request

app = Flask(__name__)

books = [
    {'id':1, 'name':"treasure island", 'author':'roberta', "year":1883},
    {'id':2, 'name':"treasure", 'author':'robert', "year":1882},
    {'id':3, 'name':"island", 'author':'robera', "year":1880}
]

@app.route('/')
def home():
    return render_template('index.html',books=books)


@app.route("/book/<int:book_id>")
def show(book_id):
    for i in books:
        if i['id'] == book_id:
            return render_template('book.html', book=i)

@app.route("/add_book", methods=["POST","GET"])
def add_book():
    if request.method == "POST":
        id = len(books)+1
        title = request.form["title"]
        author = request.form["author"]
        year = request.form["year"]
        books.append({'id': id,'name': title,'author': author,'year': year})
        return redirect(url_for('home'))
    return render_template("add_book.html")


if __name__ == '__main__':
    app.run(debug=True)