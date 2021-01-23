"""Parse string input to AST"""
# Got help from https://ruslanspivak.com/lsbasi-part7/

from ast import BinOp, Num, Skip, Var, If, Comma, While, Assign, Neg, Bool
from lexer import Lexer, Token, INTEGER, PLUS, MINUS, MUL, DIV, LPAREN, RPAREN, EOF, BOOLEAN, VAR

class Parser(object):
    def __init__(self, lexer):
        self.lexer = lexer
        # set current token to the first token taken from the input
        self.current_token = self.lexer.get_next_token()

    def error(self):
        raise Exception('Invalid syntax')

    def eat(self, token_type):
        # compare the current token type with the passed token
        # type and if they match then "eat" the current token
        # and assign the next token to the self.current_token,
        # otherwise raise an exception.
        if self.current_token.type == token_type:
            self.current_token = self.lexer.get_next_token()
        else:
            self.error()
    
    def factor(self):
        """factor : INTEGER 
        | LPAREN expr RPAREN
        | { expr }
        """
        token = self.current_token
        if token.type == INTEGER:
            self.eat(INTEGER)
            return Num(token)
        if token.type == LPAREN:
            self.eat(LPAREN)
            node = self.aexp()
            self.eat(RPAREN)
            return node
        if token.type == VAR:
            self.eat(VAR)
            return Var(token.value)
        
    def term(self):
        """term : factor ((MUL | DIV) factor)*"""
        node = self.factor()

        while self.current_token.type in (MUL, DIV):
            token = self.current_token
            if token.type == MUL:
                self.eat(MUL)
            elif token.type == DIV:
                self.eat(DIV)

            node = BinOp(left=node, op=token, right=self.factor())

        return node
    
    def aexp(self):
        node = self.term()

        while self.current_token.type in (PLUS, MINUS):
            token = self.current_token
            if token.type == PLUS:
                self.eat(PLUS)
            elif token.type == MINUS:
                self.eat(MINUS)
            node = BinOp(left=node, op=token, right=self.term())

        return node
    
    def bcmpr(self):
        if self.current_token.type == '¬':
            self.eat('¬')
            b = self.b_or()
            return Neg(b)
        if self.current_token.type == LPAREN:
            self.eat(LPAREN)
            node = self.b_or()
            self.eat(RPAREN)
            return node
        if self.current_token.type == BOOLEAN:
            b = Bool(self.current_token)
            self.eat(BOOLEAN)
            return b
        node = self.aexp()
        if self.current_token.type == '=':
            self.eat('=')
            return BinOp(left=node, op=Token('=', '='), right=self.aexp())
        if self.current_token.type == '<':
            self.eat('<')
            return BinOp(left=node, op=Token('<','<'), right=self.aexp())

    def b_and(self):
        node = self.bcmpr()
        while self.current_token.type == '∧':
            self.eat('∧')
            node = BinOp(left=node, op=Token('∧','∧'), right=self.bcmpr())
        return node
        
    def b_or(self):
        """
        b_or   : b_and (∨ b_and)*
        b_and   : bterm (∧ bterm)*
        bterm   : bfactor ((< | =) bfactor)*
        bfactor : BOOLEAN | LPAREN expr RPAREN
        """
        node = self.b_and()
        if self.current_token.type == '∨':
            self.eat('∨')
            node = BinOp(left=node, op=Token('∨','∨'), right=self.b_and())
        return node

    def command(self):
        """ c ::=
        skip
        | x := e
        | if b then c1 else c2
        | while b do c
        """
        if self.current_token.type == '{':
            self.eat('{')
            c = self.comma_command()
            self.eat('}')
            return c
        if self.current_token.type == 'skip':
            return Skip()
        if self.current_token.type == 'if':
            self.eat('if')
            b = self.b_or()
            self.eat('then')
            c1 = self.comma_command()
            self.eat('else')
            c2 = self.comma_command()
            return If(b, c1, c2)
        if self.current_token.type == 'while':
            # print("current token:", self.current_token.type, self.current_token.value)
            self.eat('while')
            # print("current token:", self.current_token.type, self.current_token.value)
            b = self.b_or()
            # print(b, b.token, b.value)
            # print("current token:", self.current_token.type, self.current_token.value)
            self.eat('do')
            # print("current token:", self.current_token.type, self.current_token.value)
            c = self.command()
            # print(c)
            # print("current token:", self.current_token.type, self.current_token.value)
            return While(b, c)
        if self.current_token.type == VAR:
            x = Var(self.current_token.value)
            self.eat(VAR)
            self.eat(':=')
            e = self.aexp()
            return Assign(x, e)

    def comma_command(self):
        """ c ::= c1 ;c2 
        | { comm }"""
        node = self.command()
        # print(node)
        while self.current_token.type == ';':
            self.eat(';')
            c2 = self.command()
            # print(c2)
            node =  Comma(node, c2)
        return node
    def parse(self):
        return self.comma_command()
