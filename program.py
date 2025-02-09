# from src.lexer import lex

# source_code = '''
# var x = 10
# var y = x + 5
# print y
# print "Hello, Orbit!"
# '''

# tokens = lex(source_code)
# print(tokens)


# //

# from src.lexer import lex
# from src.parser import Parser

# source_code = '''
# var x = 10
# var y = x + 5
# print y
# print "Hello, Orbit!"
# '''

# tokens = lex(source_code)
# parser = Parser(tokens)
# ast = parser.parse()

# # Print the AST
# for node in ast:
#     print(node.__class__.__name__, node.__dict__)


# //

from src.lexer import lex
from src.parser import Parser
from src.interpreter import Interpreter

source_code = '''
var x = 10
var y = x + 5
print y
print "Hello, Orbit!"
'''

# Lexing
tokens = lex(source_code)
print("Tokens:", tokens)

# Parsing
parser = Parser(tokens)
ast = parser.parse()
print("AST:", ast)

# Interpretation
interpreter = Interpreter()
interpreter.interpret(ast)