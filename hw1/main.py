"""Read ARITH language input, create ast, interpret ast, and output the value"""

from interpreter import Interpreter
from parse import Parser
from lexer import Lexer


def eval(ast):
    interpreter = Interpreter(parser)
    return interpreter.interpret()

def main():
    text = raw_input()
    lexer = Lexer(text)
    ast = Parser(lexer)
    interpreter = Interpreter(ast)
    result = interpreter.interpret()
    print(result)


if __name__ == '__main__':
    main()
