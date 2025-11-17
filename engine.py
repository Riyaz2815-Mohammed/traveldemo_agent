import random

def pick_best(items, user_prefs):
    scored = []
    for item in items:
        score = random.randint(0, 2)
        for pref in user_prefs:
            if pref.lower() in item["tags"]:
                score += 2
        scored.append((score, item))
    scored.sort(reverse=True, key=lambda x: x[0])
    return [s[1] for s in scored]
