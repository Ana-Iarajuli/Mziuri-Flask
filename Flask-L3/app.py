from flask import Flask, render_template, request
app = Flask(__name__)

@app.route('/')
def home():
    return render_template("index.html")

@app.route('/profile/')
def profile():
    name = request.args.get('name', 'jasurbeki')
    age = request.args.get('age')
    return render_template("profile.html", my_name=name, age=age)

@app.route('/login')
def login():
    return render_template("login.html")


if __name__ == '__main__':
    app.run(debug=True)