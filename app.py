from flask import Flask, render_template, request, redirect
from pymongo import MongoClient

app = Flask(__name__)

# MongoDB Connection
client = MongoClient("mongodb://localhost:27017/")
db = client["notes_db"]
notes = db["notes"]


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/save", methods=["POST"])
def save():

    note = request.form["note"]
    date = request.form["date"]

    notes.insert_one({
        "note": note,
        "date": date
    })

    return redirect("/")


@app.route("/search")
def search():

    date = request.args.get("date")

    result = notes.find({"date": date})

    return render_template("index.html", notes=result)


if __name__ == "__main__":
    app.run(debug=True)