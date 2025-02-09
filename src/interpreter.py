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