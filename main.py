from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def home():
    return render_template("index.html")

@app.route('/<name>/<int:age>')
def profile(name, age):
    return render_template("profile.html", my_name=name, my_age=age)

@app.route('/movies')
def movies():
    return render_template("movies.html")

@app.route('/resume')
def resume():
    return render_template("resume.html")

if __name__ == '__main__':
    app.run(debug=True)