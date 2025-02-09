from src.astt import (
    ASTNode, Number, String, Identifier, BinOp, Assign, Print
)
class Parser:
    def __init__(self, tokens):
        self.tokens = tokens
        self.current_token = None
        self.next_token()

    def next_token(self):
        if self.tokens:
            self.current_token = self.tokens.pop(0)
        else:
            self.current_token = None

    # def parse(self):
    #     statements = []
    #     while self.current_token:
    #         if self.current_token[0] == 'PRINT':
    #             statements.append(self.parse_print())
    #         elif self.current_token[0] == 'IDENTIFIER' and self.tokens[0][1] == '=':
    #             statements.append(self.parse_assignment())
    #         else:
    #             raise SyntaxError(f"Unexpected token: {self.current_token}")
    #     return statements

    def parse(self):
        statements = []
        while self.current_token:
            if self.current_token[0] == 'PRINT':
                statements.append(self.parse_print())
            elif self.current_token[0] == 'VAR':
                statements.append(self.parse_var_declaration())
            else:
                raise SyntaxError(f"Unexpected token: {self.current_token}")
        return statements

    def parse_var_declaration(self):
        self.next_token()  # Skip 'var'
        identifier = Identifier(self.current_token[1])  # Get the variable name
        self.next_token()  # Skip the identifier
        if self.current_token[1] != '=':
            raise SyntaxError("Expected '=' after variable name")
        self.next_token()  # Skip '='
        value = self.parse_expression()  # Parse the expression after '='
        return Assign(identifier, value)

    def parse_print(self):
        self.next_token()  # Skip 'print'
        expression = self.parse_expression()
        return Print(expression)

    def parse_assignment(self):
        identifier = Identifier(self.current_token[1])
        self.next_token()  # Skip identifier
        self.next_token()  # Skip '='
        value = self.parse_expression()
        return Assign(identifier, value)

    def parse_expression(self):
        left = self.parse_term()
        while self.current_token and self.current_token[0] == 'OPERATOR':
            op = self.current_token[1]
            self.next_token()
            right = self.parse_term()
            left = BinOp(left, op, right)
        return left

    def parse_term(self):
        token_type, value = self.current_token
        if token_type == 'NUMBER':
            self.next_token()
            return Number(int(value))
        elif token_type == 'STRING':
            self.next_token()
            return String(value[1:-1])  # Remove quotes
        elif token_type == 'IDENTIFIER':
            self.next_token()
            return Identifier(value)
        else:
            raise SyntaxError(f"Unexpected token: {self.current_token}")