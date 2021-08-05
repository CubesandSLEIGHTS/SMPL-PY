from tokens import Tokens
from position import Position
from errors import IllCharError
from constants import TT_INT, TT_FLOAT, TT_PLS, TT_MIN, TT_MUL, TT_DIV, DIGITS, TT_LPAR, TT_RPAR

class Lexer:
    def __init__(self, fn):
        self.fn = fn
        self.contents = None
        self.current_char = None
        self.pos = Position(-1, -1, fn, self.contents)
    
    def read_file(self):
        with open(self.fn, 'r') as f:
            self.contents = f.read()
    
    def advance(self):
        self.pos.advance(self.current_char)
        self.current_char = self.read_file()[self.pos.idx] if self.pos.idx < len(self.text) else None
    
    def make_num(self):
        num_str = ''
        dot_cnt = 0
        
        while self.current_char != None and self.current_char in DIGITS + '.':
            if self.current_char == '.':
                if dot_cnt == 1:break
                dot_cnt += 1
                num_str += '.'
            else:
                num_str += self.current_char
            self.advance()
        
        if dot_cnt == 0:
            return Tokens(TT_INT, int(num_str))
        else:
            return Tokens(TT_FLOAT, float(num_str))

             

    def make_tokens(self):
        tokens = []

        while self.current_char != None:
            if self.current_char in ' \t':
                self.advance()
            elif self.current_char in DIGITS:
                tokens.append(self.make_num())
                self.advance()
            elif self.current_char == '+':
                tokens.append(Tokens((TT_PLS)))
                self.advance()
            elif self.current_char == '-':
                tokens.append(Tokens((TT_MIN)))
                self.advance()
            elif self.current_char == '*':
                tokens.append(Tokens((TT_MUL)))
                self.advance()
            elif self.current_char == '/':
                tokens.append(Tokens((TT_DIV)))
                self.advance()
            elif self.current_char == '(':
                tokens.append(Tokens((TT_LPAR)))
                self.advance()
            elif self.current_char == ')':
                tokens.append(Tokens((TT_RPAR)))
                self.advance()
            
            else:
                pos_start = self.pos.copy()
                char = self.current_char
                self.advance()
                return [], IllCharError(pos_start, self.pos, f'Illegal Character "{char}" ')

