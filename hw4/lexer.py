"""Define input reader"""
# Got help from https://ruslanspivak.com/lsbasi-part7/

# Token types
#
# EOF (end-of-file) token is used to indicate that
# there is no more input left for lexical analysis
INTEGER, PLUS, MINUS, MUL, DIV, LPAREN, RPAREN, EOF = (
    'INTEGER', 'PLUS', 'MINUS', 'MUL', 'DIV', '(', ')', 'EOF'
)
BOOLEAN = 'BOOLEAN'
VAR = 'VAR'

def is_int(s):
    try: 
        int(s)
        return True
    except ValueError:
        return False

class Token(object):
    def __init__(self, type, value):
        self.type = type
        self.value = value

    def __str__(self):
        """String representation of the class instance.

        Examples:
            Token(INTEGER, 3)
            Token(PLUS, '+')
            Token(MUL, '*')
        """
        return 'Token({type}, {value})'.format(
            type=self.type,
            value=repr(self.value)
        )

    def __repr__(self):
        return self.__str__()


class Lexer(object):
    def __init__(self, text):
        # client string input, e.g. "4 + 2 * 3 - 6 / 2"
        self.text = text
        self.words = text.split()
        self.word_ind = 0
        self.current_word = self.words[self.word_ind]

    def error(self):
        print("invalid word", self.current_word)
        raise Exception('Invalid word')

    def advance(self):
        """Advance the `word_ind` pointer and set the `current_word` variable."""
        self.word_ind += 1
        if self.word_ind > len(self.words) - 1:
            self.current_word = None
        else:
            self.current_word = self.words[self.word_ind]

    def skip_whitespace(self):
        while self.current_char is not None and self.current_char.isspace():
            self.advance()

    def get_next_token(self):
        """Lexical analyzer (also known as scanner or tokenizer)

        This method is responsible for breaking a sentence
        apart into tokens. One token at a time.
        """
        while self.current_word is not None:
            if is_int(self.current_word):
                n = int(self.current_word)
                self.advance()
                return Token(INTEGER, n)

            if self.current_word == '+':
                self.advance()
                return Token(PLUS, '+')

            if self.current_word == '-':
                self.advance()
                return Token(MINUS, '-')

            if self.current_word == '*':
                self.advance()
                return Token(MUL, '*')

            if self.current_word == '/':
                self.advance()
                return Token(DIV, '/')

            if self.current_word == '(':
                self.advance()
                return Token(LPAREN, '(')

            if self.current_word == ')':
                self.advance()
                return Token(RPAREN, ')')
                
            if self.current_word == ':=':
                self.advance()
                return Token(':=', ':=')
            
            if self.current_word == ';':
                self.advance()
                return Token(';', ';')
            
            if self.current_word == 'while':
                self.advance()
                return Token('while', 'while')
            
            if self.current_word == '¬':
                self.advance()
                return Token('¬', '¬')
            
            if self.current_word == '=':
                self.advance()
                return Token('=', '=')
            
            if self.current_word == 'do':
                self.advance()
                return Token('do', 'do')
            
            if self.current_word == '{':
                self.advance()
                return Token('{', '{')
                
            if self.current_word == 'if':
                self.advance()
                return Token('if', 'if')
            
            if self.current_word == '<':
                self.advance()
                return Token('<', '<')
                
            if self.current_word == 'then':
                self.advance()
                return Token('then', 'then')
                
            if self.current_word == 'else':
                self.advance()
                return Token('else', 'else')
                
            if self.current_word == '>':
                self.advance()
                return Token('>', '>')
                
            if self.current_word == '>=':
                self.advance()
                return Token('>=', '>=')
                
            if self.current_word == '<=':
                self.advance()
                return Token('<=', '<=')
                
            if self.current_word == 'false':
                self.advance()
                return Token(BOOLEAN, False)
            
            if self.current_word == 'true':
                self.advance()
                return Token(BOOLEAN, True)
            
            if self.current_word == 'skip':
                self.advance()
                return Token('skip', 'skip')
                
            if self.current_word == '∧':
                self.advance()
                return Token('∧', '∧')
                
            if self.current_word == '∨':
                self.advance()
                return Token('∨', '∨')
                
            if self.current_word == '}':
                self.advance()
                return Token('}', '}')
            
            if self.current_word.isidentifier():
                var = self.current_word
                self.advance()
                return Token(VAR, var)

            self.error()

        return Token(EOF, None)
