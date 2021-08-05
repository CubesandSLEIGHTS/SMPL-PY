class Position:
    def __init__(self, idx, ln, fn, ftxt):
        self.idx = idx
        self.ln = ln
        self.fn = fn
        self.ftxt = ftxt

    def advance(self, current_char):
        self.idx += 1

        if current_char == '\n':
            self.ln += 1

        return self

    def copy(self):
        return Position(self.idx, self.ln, self.fn, self.ftxt)