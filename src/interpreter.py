from src.astt import (
    Number, String, Identifier, BinOp, Assign, Print
)

class Interpreter:
    def __init__(self):
        self.variables = {}

    def visit(self, node):
        if isinstance(node, Number):
            return node.value
        elif isinstance(node, String):
            return node.value
        elif isinstance(node, Identifier):
            return self.variables.get(node.name, 0)
        elif isinstance(node, BinOp):
            left = self.visit(node.left)
            right = self.visit(node.right)
            if node.op == '+':
                return left + right
            elif node.op == '-':
                return left - right
            elif node.op == '*':
                return left * right
            elif node.op == '/':
                return left / right
        elif isinstance(node, Assign):
            self.variables[node.identifier.name] = self.visit(node.value)
        elif isinstance(node, Print):
            print(self.visit(node.expression))

    def interpret(self, ast):
        for node in ast:
            self.visit(node)

# class Interpreter:
    # def __init__(self):
    #     self.variables = {}

    # def visit(self, node):
    #     if isinstance(node, Number):
    #         return node.value
    #     elif isinstance(node, String):
    #         return node.value
    #     elif isinstance(node, Identifier):
    #         return self.variables.get(node.name, 0)
    #     elif isinstance(node, BinOp):
    #         left = self.visit(node.left)
    #         right = self.visit(node.right)
    #         if node.op == '+':
    #             return left + right
    #     elif isinstance(node, Assign):
    #         value = self.visit(node.value)
    #         self.variables[node.name.name] = value
    #         return value
    #     elif isinstance(node, Print):
    #         value = self.visit(node.value)
    #         print(value)
    #         return value

# Define the node classes
# class Number:
#     def __init__(self, value):
#         self.value = value

# class String:
#     def __init__(self, value):
#         self.value = value

# class Identifier:
#     def __init__(self, name):
#         self.name = name

# class BinOp:
#     def __init__(self, left, op, right):
#         self.left = left
#         self.op = op
#         self.right = right

# class Assign:
#     def __init__(self, name, value):
#         self.name = name
#         self.value = value

# class Print:
#     def __init__(self, value):
#         self.value = value