class ASTNode:
    pass

class Number(ASTNode):
    def __init__(self, value):
        self.value = value

class String(ASTNode):
    def __init__(self, value):
        self.value = value

class Identifier(ASTNode):
    def __init__(self, name):
        self.name = name

class BinOp(ASTNode):
    def __init__(self, left, op, right):
        self.left = left
        self.op = op
        self.right = right

class Assign(ASTNode):
    def __init__(self, identifier, value):
        self.identifier = identifier
        self.value = value

class Print(ASTNode):
    def __init__(self, expression):
        self.expression = expression