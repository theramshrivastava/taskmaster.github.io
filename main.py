from flask import Flask, render_template, request, redirect

app = Flask("TaskMaster")

tasks = []

@app.route("/")
def index():
    return render_template("index.html", tasks=tasks)

@app.route("/add_task", methods=["POST"])
def add_task():
    task_name = request.form["task"]
    task_duration = int(request.form["duration"])

    task = {"name": task_name, "progress": 0, "duration": task_duration}
    tasks.append(task)

    return redirect("/")

@app.route("/remove_task", methods=["POST"])
def remove_task():
    task_name = request.form["task"]

    for task in tasks:
        if task["name"] == task_name:
            tasks.remove(task)
            break

    return redirect("/")

@app.route("/update_progress", methods=["POST"])
def update_progress():
    task_name = request.form["task"]
    progress = int(request.form["progress"])

    for task in tasks:
        if task["name"] == task_name:
            task["progress"] = progress

            if progress > 50:
                tasks.remove(task)
                tasks.append(task)

            break

    return redirect("/")

if __name__ == "__main__":
    app.run(debug=True)
