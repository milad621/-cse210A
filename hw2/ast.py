"""Define AST objects"""
# Got help from https://ruslanspivak.com/lsbasi-part7/

class AST(object):
    pass

# integer
class Num(AST):
    def __init__(self, token):
        self.token = token
        self.value = token.value
        # print("num", self.token, self.value)

# booleans. true or false
class Bool(AST):
    def __init__(self, token):
        self.token = token
        self.value = token.value
        
# locations(assignable variables)
class Var(AST):
    def __init__(self, name):
        self.name = name
        self.value = 0

# all binary operations. {+, -, *, /, =, >, <, ∧, ∨}
class BinOp(AST):
    def __init__(self, left, op, right):
        self.left = left
        self.token = self.op = op
        self.right = right

class Neg(AST):
    def __init__(self, b):
        self.b = b

# x := e           
class Assign(AST):
    def __init__(self, x, e):
        self.x = x
        self.e = e

# skip        
class Skip(AST):
    pass

# c1 ; c2          
class Comma(AST):
    def __init__(self, left, right):
        # print("creating comma", left, right)
        self.left = left
        self.right = right
            
# if b then c1 else c2
class If(AST):
    def __init__(self, b, c1, c2):
        self.b = b
        self.c1 = c1
        self.c2 = c2
        
# while b do c
class While(AST):
    def __init__(self, b, c):
        self.b = b
        self.c = c

