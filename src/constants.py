class Constant(object):
    def __init__(self, val):
        super(Constant, self).__setattr__("value", val)
    def __setattr__(self, name, val):
        raise ValueError("Trying to change a constant value", self)

DIGITS = '0123456789'

TT_INT =        Constant("INT")
TT_FLOAT =      Constant("FLOAT")
TT_PLS =        Constant("PLUS")
TT_MIN =        Constant("MIN")
TT_MUL =        Constant("MULT")
TT_DIV =        Constant("DIV")
TT_LPAR =       Constant("LPAREN")
TT_RPAR =       Constant("RPAREN")