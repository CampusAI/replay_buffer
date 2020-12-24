class Transition:
    def __init__(self, s, a, r, done, next_s=None, action_prob=None, td_error=None):
        self.s = s
        self.a = a
        self.r = r
        self.done = done
        self.next_s = next_s
        self.action_prob = action_prob
        self.td_error = td_error