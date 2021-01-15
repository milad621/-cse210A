"""Define AST objects"""
# Got help from https://ruslanspivak.com/lsbasi-part7/

class AST(object):
    pass
    
class Num(AST):
    def __init__(self, token):
        self.token = token
        self.value = token.value
        
class BinOp(AST):
    def __init__(self, left, op, right):
        self.left = left
        self.token = self.op = op
        self.right = right