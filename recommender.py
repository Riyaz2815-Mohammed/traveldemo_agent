import json
from engine import pick_best

def load_json(name):
    with open(f"data/{name}.json") as f:
        return json.load(f)

attractions = load_json("attractions")
restaurants = load_json("restaurants")
hotels = load_json("hotels")

def recommend_items(preferences, memory):
    user_prefs = preferences + memory.get_global_preferences()
    return {
        "hotels": pick_best(hotels, user_prefs)[:3],
        "restaurants": pick_best(restaurants, user_prefs)[:3],
        "attractions": pick_best(attractions, user_prefs)[:5]
    }
