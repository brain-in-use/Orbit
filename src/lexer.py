import re

# Token types
TOKENS = [
    ('NUMBER', r'\d+'),                     # Integers
    ('STRING', r'"[^"]*"'),                 # Strings
    ('IDENTIFIER', r'[a-zA-Z_]\w*'),        # Variable names
    ('OPERATOR', r'[+\-*/]'),               # Arithmetic operators
    ('ASSIGN', r'='),                       # Assignment operator
    ('PRINT', r'print'),                    # Print keyword
    ('IF', r'if'),                          # If keyword
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