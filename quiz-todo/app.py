from flask import Flask, render_template, request, redirect, url_for
app = Flask(__name__)

todo_list = ["shaurma" , "kartofili", "davaleba", "dalageba"]

@app.route('/')
def todo():
    return render_template('index.html', todo_list=todo_list)

@app.route('/add_task')
def add_task():
    new_task = request.args.get('task')
    if new_task:
        todo_list.append(new_task)

    return render_template("add_task.html")


if __name__ == '__main__':
    app.run(debug=True)

