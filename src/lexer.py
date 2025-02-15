import re

# Token types
TOKENS = [
    ('IF', r'if'),                          # if keyword
    ('ELSE', r'else'),                      # else keyword
    ('COMPARISON_OP', r'==|!=|<=|>=|<|>'),  # Comparison operators
    ('LBRACE', r'\{'),                      # Left brace
    ('RBRACE', r'\}'),                      # Right brace
    ('NUMBER', r'\d+'),                     # Integers
    ('STRING', r'"[^"]*"'),                 # Strings
    ('PRINT', r'print'),                    # Print keyword
    ('VAR', r'var'),                        # Variable declaration keyword
    ('IDENTIFIER', r'[a-zA-Z_]\w*'),        # Variable names
    ('OPERATOR', r'[+\-*/]'),               # Arithmetic operators
    ('ASSIGN', r'='),                       # Assignment operator
    # ('IF', r'if'),                          # If keyword
    ('LBRACE', r'\{'),                      # Left brace
    ('RBRACE', r'\}'),                      # Right brace
    ('LPAREN', r'\('),                      # Left parenthesis
    ('RPAREN', r'\)'),                      # Right parenthesis
    ('SEMICOLON', r';'),                    # Semicolon
    ('SKIP', r'[ \t\n]'),                   # Whitespace
]

def lex(source_code):
    tokens = []
    while source_code:
        for token_type, pattern in TOKENS:
            regex = re.compile(pattern)
            match = regex.match(source_code)
            if match:
                value = match.group(0)
                if token_type != 'SKIP':
                    tokens.append((token_type, value))
                source_code = source_code[match.end():]
                break
        else:
            raise SyntaxError(f"Unexpected character: {source_code[0]}")
    return tokens