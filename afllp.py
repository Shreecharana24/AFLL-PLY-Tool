import ply.lex as lex
import ply.yacc as yacc

# Lexer and parser to validate selected C++ constructs using Python and PLY

tokens = [
    'ID', 'NUMBER',
    'LPAREN', 'RPAREN', 'LBRACE', 'RBRACE',
    'SEMICOLON', 'COMMA',
    'LSHIFT', 'RSHIFT', 'ASSIGN',
    'STRING', 'LT', 'GT', 'PLUSPLUS',
    'CIN', 'COUT', 'IFSTREAM', 'OFSTREAM',
    'TRY', 'CATCH', 'THROW',
    'STRUCT', 'CLASS', 'UNION', 'ENUM',
    'STATIC', 'EXTERN', 'REGISTER', 'AUTO',
    'FOR', 'WHILE', 'DO',
    'INT'
]

# Regular expressions for basic tokens
t_LPAREN    = r'\('
t_RPAREN    = r'\)'
t_LBRACE    = r'\{'
t_RBRACE    = r'\}'
t_SEMICOLON = r';'
t_COMMA     = r','
t_LSHIFT    = r'<<'
t_RSHIFT    = r'>>'
t_ASSIGN    = r'='
t_STRING    = r'\"([^\\\n]|(\\.))*?\"'
t_LT        = r'<'
t_GT        = r'>'
t_PLUSPLUS  = r'\+\+'

# Reserved words
reserved = {
    'cin': 'CIN',
    'cout': 'COUT',
    'ifstream': 'IFSTREAM',
    'ofstream': 'OFSTREAM',
    'try': 'TRY',
    'catch': 'CATCH',
    'throw': 'THROW',
    'struct': 'STRUCT',
    'class': 'CLASS',
    'union': 'UNION',
    'enum': 'ENUM',
    'static': 'STATIC',
    'extern': 'EXTERN',
    'register': 'REGISTER',
    'auto': 'AUTO',
    'for': 'FOR',
    'while': 'WHILE',
    'do': 'DO',
    'int': 'INT'
}

# Identifier rule
def t_ID(t):
    r'[A-Za-z_][A-Za-z0-9_]*'
    t.type = reserved.get(t.value, 'ID')
    return t

# Number rule
def t_NUMBER(t):
    r'\d+'
    t.value = int(t.value)
    return t

# Ignore spaces and tabs
t_ignore = ' \t'

# Track newlines
def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)

# Comments
def t_comment(t):
    r'//.*'
    pass

def t_block_comment(t):
    r'/\*(.|\n)*?\*/'
    t.lexer.lineno += t.value.count('\n')
    pass

# Handle illegal characters
def t_error(t):
    print(f"Illegal character '{t.value[0]}'")
    t.lexer.skip(1)

lexer = lex.lex()

start = 'program'

def p_program(p):
    '''program : program statement
               | statement'''
    pass

def p_statement(p):
    '''statement : io_stmt
                 | exception_stmt
                 | udtype_stmt
                 | storage_stmt
                 | loop_stmt'''
    pass

# Input/output statements
def p_io_stmt_cout(p):
    'io_stmt : COUT LSHIFT cout_list SEMICOLON'
    print("Valid: cout output statement")

def p_cout_list(p):
    '''cout_list : cout_list LSHIFT cout_item
                 | cout_item'''
    pass

def p_cout_item(p):
    '''cout_item : STRING
                 | ID'''
    pass

def p_io_stmt_cin(p):
    'io_stmt : CIN RSHIFT id_list SEMICOLON'
    print("Valid: cin input statement")

def p_id_list(p):
    '''id_list : id_list RSHIFT ID
               | ID'''
    pass

def p_io_stmt_ifstream(p):
    'io_stmt : IFSTREAM ID SEMICOLON'
    print("Valid: ifstream declaration")

def p_io_stmt_ofstream(p):
    'io_stmt : OFSTREAM ID SEMICOLON'
    print("Valid: ofstream declaration")

# Exception handling
def p_exception_try(p):
    'exception_stmt : TRY LBRACE RBRACE CATCH LPAREN ID RPAREN LBRACE RBRACE'
    print("Valid: try-catch block")

def p_exception_throw(p):
    'exception_stmt : THROW ID SEMICOLON'
    print("Valid: throw statement")

# User-defined types
def p_udtype_stmt(p):
    'udtype_stmt : utype'
    pass

def p_utype(p):
    '''utype : STRUCT ID LBRACE RBRACE SEMICOLON
             | CLASS ID LBRACE RBRACE SEMICOLON
             | UNION ID LBRACE RBRACE SEMICOLON
             | ENUM ID LBRACE ID RBRACE SEMICOLON'''
    print("Valid: user-defined type definition")

# Storage class specifiers
def p_storage_stmt(p):
    '''storage_stmt : STATIC ID SEMICOLON
                    | EXTERN ID SEMICOLON
                    | REGISTER ID SEMICOLON
                    | AUTO ID SEMICOLON'''
    print("Valid: storage-class specifier")

# Looping constructs
def p_loop_for(p):
    '''loop_stmt : FOR LPAREN simple_stmt SEMICOLON condition SEMICOLON simple_stmt RPAREN
                 | FOR LPAREN simple_stmt SEMICOLON condition SEMICOLON simple_stmt RPAREN LBRACE RBRACE'''
    print("Valid: for loop")

def p_loop_while(p):
    'loop_stmt : WHILE LPAREN condition RPAREN LBRACE RBRACE'
    print("Valid: while loop")

def p_loop_do_while(p):
    'loop_stmt : DO LBRACE RBRACE WHILE LPAREN condition RPAREN SEMICOLON'
    print("Valid: do-while loop")

# Expressions inside loops
def p_simple_stmt(p):
    '''simple_stmt : ID ASSIGN NUMBER
                   | INT ID ASSIGN NUMBER
                   | ID PLUSPLUS
                   | ID'''
    pass

def p_condition(p):
    '''condition : ID LT NUMBER
                 | ID GT NUMBER
                 | ID'''
    pass

# Error handling
def p_error(p):
    if p:
        print(f"Syntax error at token '{p.value}' (type {p.type})")
    else:
        print("Syntax error at EOF")

parser = yacc.yacc()

def main():
    print("AFLL Tool — C++ Construct Validation")
    print("Type a statement (or 'exit' to quit)\n")
    while True:
        try:
            s = input('C++ > ')
        except EOFError:
            break
        if not s or s.lower() == 'exit':
            break
        parser.parse(s)

if __name__ == '__main__':
    main()
