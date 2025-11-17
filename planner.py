import random
from recommender import attractions, restaurants

def generate_itinerary(destination, start, end, memory):
    final_plan = []
    days = 3
    user_prefs = memory.get_global_preferences()

    sorted_attractions = sorted(
        attractions,
        key=lambda x: random.random() + (1 if any(p in x["tags"] for p in user_prefs) else 0),
        reverse=True
    )

    pointer = 0
    for day in range(1, days + 1):
        day_plan = {
            "day": day,
            "morning": sorted_attractions[pointer]["name"],
            "lunch": random.choice(restaurants)["name"],
            "evening": sorted_attractions[pointer + 1]["name"],
        }
        pointer += 2
        final_plan.append(day_plan)
    return final_plan
