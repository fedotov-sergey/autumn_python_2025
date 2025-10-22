# todo: Flask App https://daehnhardt.com/blog/2025/02/11/todo-flask-app/
# Расширьте приложение и добавьте него поля ввода:
# description - описание задачи
# start_date - когда начать задачу
# При добавлении двух дополнительных полей откорректируйте структуру таблицы,
# запросы на сохранение данных и шаблон вывода-вывода.
import datetime
from flask import Flask, render_template, request, redirect, url_for, g
import sqlite3

app = Flask(__name__)
DATABASE = "todo.db"
if __name__ == "__main__":
    app.run(debug=True)


def get_db():
    db = getattr(g, "_database", None)
    if db is None:
        db = g._database = sqlite3.connect(DATABASE)
        db.execute(
            """
            CREATE TABLE IF NOT EXISTS tasks (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                task TEXT NOT NULL,
                description TEXT NOT NULL,
                date TEXT NOT NULL,
                priority INTEGER NOT NULL,
                complete BOOLEAN NOT NULL CHECK (complete IN (0, 1))
            )
        """
        )
    return db


@app.route("/")
def index():
    db = get_db()
    cur = db.execute("SELECT id, task, description, date, priority, complete FROM tasks")
    tasks = [
        {
            "id": row[0],
            "task": row[1],
            "description": row[2],
            "date": row[3],
            "priority": row[4],
            "complete": bool(row[5]),
        }
        for row in cur.fetchall()
    ]
    return render_template("index.html", tasks=tasks)


@app.route("/add", methods=["POST"])
def add():
    task = request.form["task"]
    description = request.form["description"]
    date = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    priority = int(request.form["priority"])
    db = get_db()
    db.execute(
        "INSERT INTO tasks (task, description, date, priority, complete) VALUES (?, ?, ?, ?, ?)",
        (task, description, date, priority, False),
    )
    db.commit()
    return redirect(url_for("index"))


@app.route("/complete/<int:task_id>")
def complete(task_id):
    db = get_db()
    db.execute("UPDATE tasks SET complete = NOT complete WHERE id = ?", (task_id,))
    db.commit()
    return redirect(url_for("index"))


@app.route("/delete/<int:task_id>")
def delete(task_id):
    db = get_db()
    db.execute("DELETE FROM tasks WHERE id = ?", (task_id,))
    db.commit()
    return redirect(url_for("index"))


@app.route("/edit/<int:task_id>", methods=["GET", "POST"])
def edit(task_id):
    db = get_db()
    if request.method == "POST":
        task = request.form["task"]
        priority = int(request.form["priority"])  # Get priority from the form
        db.execute("UPDATE tasks SET task = ?, priority = ? WHERE id = ?", (task, priority, task_id))
        db.commit()
        return redirect(url_for("index"))
    else:
        cur = db.execute("SELECT task, priority FROM tasks WHERE id = ?", (task_id,))
        task_data = cur.fetchone()
        return render_template("edit.html", task=task_data[0], priority=task_data[1], task_id=task_id)


@app.teardown_appcontext
def close_connection(exception):
    db = getattr(g, "_database", None)
    if db is not None:
        db.close()
