"""Interpret AST tree"""
# Got help from https://ruslanspivak.com/lsbasi-part7/

from lexer import Lexer, Token, INTEGER, PLUS, MINUS, MUL, DIV, LPAREN, RPAREN, EOF
from parse import Parser
from ast import BinOp, Num, Skip, Var, If, Comma, While, Assign, Neg, Bool

class NodeVisitor(object):
    def visit(self, node):
        method_name = 'visit_' + type(node).__name__
        visitor = getattr(self, method_name, self.generic_visit)
        return visitor(node)

    def generic_visit(self, node):
        raise Exception('No visit_{} method'.format(type(node).__name__))


class Interpreter(NodeVisitor):
    def __init__(self, parser):
        self.parser = parser
        self.vars = {}
        self.report_vars = []

    def visit_BinOp(self, node):
        if node.op.type == PLUS:
            return self.visit(node.left) + self.visit(node.right)
        elif node.op.type == MINUS:
            return self.visit(node.left) - self.visit(node.right)
        elif node.op.type == MUL:
            return self.visit(node.left) * self.visit(node.right)
        elif node.op.type == DIV:
            return self.visit(node.left) / self.visit(node.right)
        elif node.op.type == '=':
            return self.visit(node.left) == self.visit(node.right)
        elif node.op.type == '>':
            return self.visit(node.left) > self.visit(node.right)
        elif node.op.type == '<':
            return self.visit(node.left) < self.visit(node.right)
        elif node.op.type == '<=':
            return self.visit(node.left) <= self.visit(node.right)
        elif node.op.type == '>=':
            return self.visit(node.left) >= self.visit(node.right)
        elif node.op.type == '∧':
            return self.visit(node.left) and self.visit(node.right)
        elif node.op.type == '∨':
            return self.visit(node.left) or self.visit(node.right)

    def visit_Num(self, node):
        return node.value
    
    def visit_Bool(self, node):
        return node.value
    
    def visit_Var(self, node):
        if node.name not in self.vars:
            self.vars[node.name] = 0
        return self.vars[node.name]
    
    def visit_Neg(self, node):
        return not self.visit(node.b)
    
    def visit_Assign(self, node):
        name = node.x.name
        if name not in self.report_vars:
            self.report_vars.append(name)
        val = self.visit(node.e)
        self.vars[name] = val
        
    def visit_Skip(self, node):
        pass
        
    def visit_Comma(self, node):
        self.visit(node.left)
        self.visit(node.right)
        
    def visit_If(self, node):
        # print('b: ', self.visit(node.b))
        if self.visit(node.b):
            self.visit(node.c1)
        else:
            self.visit(node.c2)
        
    def visit_While(self, node):
        # print('b: ', self.visit(node.b))
        while self.visit(node.b):
            self.visit(node.c)
            
    def small_step(self):
        tree = self.parser.parse()
        

    def interpret(self):
        tree = self.parser.parse()
        # print("top level:", tree)
        self.visit(tree)
        s = '{'
        first = True
        self.report_vars.sort()
        for i in self.report_vars:
            if first == False:
                s += ', '
            first = False
            s += i
            s += ' → '
            s += str(self.vars[i])
        s += '}'
        return s
