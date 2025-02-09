import sys
from src.interpreter import Interpreter
from src.lexer import lex
from src.parser import Parser

def run_program(file_path):
    with open(file_path, 'r') as file:
        source_code = file.read()

    # Lexing
    tokens = lex(source_code)

    # Parsing
    parser = Parser(tokens)
    ast = parser.parse()

    # Interpretation
    interpreter = Interpreter()
    interpreter.interpret(ast)

if __name__ == '__main__':
    if len(sys.argv) != 2:
        print("Usage: python run.py <file.orb>")
    else:
        run_program(sys.argv[1])