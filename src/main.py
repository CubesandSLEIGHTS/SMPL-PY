from lexer import Lexer

def run(fn):
    lexer = Lexer(fn)
    tokens, error = lexer.make_tokens()

    return tokens, error

result, error = run('tests/Test_1.smplpy')

if error:print(error.as_str())
else:print(result)