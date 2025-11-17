from flask import Flask, render_template, request, jsonify
from recommender import recommend_items
from planner import generate_itinerary
from memory import Memory

app = Flask(_name_)

memory = Memory()

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/api/recommend", methods=["POST"])
def recommend_api():
    data = request.json
    user = data["user"]
    prefs = data["preferences"]
    memory.store_preference(user, prefs)
    return jsonify(recommend_items(prefs, memory))

@app.route("/api/plan", methods=["POST"])
def plan_api():
    data = request.json
    user = data["user"]
    start = data["start"]
    end = data["end"]
    destination = data["destination"]
    return jsonify(generate_itinerary(destination, start, end, memory))

if _name_ == "_main_":
    app.run(debug=True)
