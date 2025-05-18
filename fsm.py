default_state = 0
text_state = 1
image_state = 2

class FSM:
    def __init__(self):
        self.states = {}
    def get_state(self, uid):
        if uid not in self.states:
            self.states[uid] = default_state
        return self.states[uid]
    def set_state(self, uid,state):
        self.states[uid] = state