from flask import Flask, jsonify, render_template, request
from pymongo import MongoClient
import json
import certifi

app = Flask(__name__)

# MongoDB Atlas connection
client = MongoClient("mongodb+srv://akshay123:akshay123@ecomclustor1.vddmp.mongodb.net/", tls=True,
    tlsCAFile=certifi.where())
db = client["formDB"]
collection = db["userData"]

# -------------------------------
# API Route - Reads data from file
# -------------------------------
@app.route("/api")
def api_data():
    with open("data.json", "r") as file:
        data = json.load(file)
    return jsonify(data)

# -------------------------------
# Form Page
# -------------------------------
@app.route("/", methods=["GET", "POST"])
def form():
    error = None

    if request.method == "POST":
        try:
            name = request.form["name"]
            email = request.form["email"]

            collection.insert_one({
                "name": name,
                "email": email
            })

            return render_template("success.html")

        except Exception as e:
            error = str(e)

    return render_template("form.html", error=error)


if __name__ == "__main__":
    app.run(debug=True)
