class Memory:
    def __init__(self):
        self.history = []

    def add(self, user, assistant):
        self.history.append({"user":user, "assistant": assistant})

    def get_history(self):
        return self.history