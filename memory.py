class Memory:
    def _init_(self):
        self.longterm_prefs = {}

    def store_preference(self, user, prefs):
        if user not in self.longterm_prefs:
            self.longterm_prefs[user] = []
        self.longterm_prefs[user].extend(prefs)

    def get_global_preferences(self):
        merged = []
        for p in self.longterm_prefs.values():
            merged.extend(p)
        return list(set(merged))
