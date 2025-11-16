# AFLL PLY TOOL IMPLEMENTATION — C++ LANGUAGE CONSTRUCTS
# Objective: Implement lexical & syntax analysis for selected C++ constructs

import ply.lex as lex
import ply.yacc as yacc

# LEXER SECTION

tokens = [
    'ID', 'NUMBER',
    'LPAREN', 'RPAREN', 'LBRACE', 'RBRACE',
    'SEMICOLON', 'COMMA', 'LSHIFT', 'RSHIFT', 'ASSIGN',
    'STRING', 'LT', 'GT', 'PLUSPLUS',
    'CIN', 'COUT', 'IFSTREAM', 'OFSTREAM',
    'TRY', 'CATCH', 'THROW', 'FINALLY',
    'STRUCT', 'CLASS', 'UNION', 'ENUM',
    'STATIC', 'EXTERN', 'REGISTER', 'AUTO',
    'FOR', 'WHILE', 'DO',
    'INT'
]

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

reserved = {
    'cin': 'CIN',
    'cout': 'COUT',
    'ifstream': 'IFSTREAM',
    'ofstream': 'OFSTREAM',
    'try': 'TRY',
    'catch': 'CATCH',
    'throw': 'THROW',
    'finally': 'FINALLY',
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

def t_ID(t):
    r'[A-Za-z_][A-Za-z0-9_]*'
    t.type = reserved.get(t.value, 'ID')
    return t

def t_NUMBER(t):
    r'\d+'
    t.value = int(t.value)
    return t

def t_comment(t):
    r'//.*'
    pass

def t_block_comment(t):
    r'/\[\s\S]?\*/'
    t.lexer.lineno += t.value.count('\n')
    pass

def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)

t_ignore = ' \t\r'

def t_error(t):
    print(f"Illegal character '{t.value[0]}' at line {t.lexer.lineno}")
    t.lexer.skip(1)

lexer = lex.lex()

# PARSER SECTION

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

# Allow multiple statements inside blocks
def p_statement_list(p):
    '''statement_list : statement_list statement
                      | statement'''
    pass

# ---- 2.1 Input / Output statements ----
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
    print("Valid: ifstream declaration (file input)")

def p_io_stmt_ofstream(p):
    'io_stmt : OFSTREAM ID SEMICOLON'
    print("Valid: ofstream declaration (file output)")
# ---- 2.2 Exception Handling ----
def p_exception_try(p):
    'exception_stmt : TRY LBRACE statement_list RBRACE CATCH LPAREN ID RPAREN LBRACE statement_list RBRACE'
    print("Valid: try-catch block")
def p_exception_throw(p):
    'exception_stmt : THROW ID SEMICOLON'
    print("Valid: throw statement")

# ---- 2.3 User-defined Data Types ----
def p_udtype_stmt(p):
    'udtype_stmt : utype'
    pass

def p_utype(p):
    '''utype : STRUCT ID LBRACE RBRACE SEMICOLON
             | CLASS ID LBRACE RBRACE SEMICOLON
             | UNION ID LBRACE RBRACE SEMICOLON
             | ENUM ID LBRACE ID RBRACE SEMICOLON'''
    print("Valid: user-defined type definition")

# ---- 2.4 Storage Class Specifiers ----
def p_storage_stmt(p):
    '''storage_stmt : STATIC ID SEMICOLON
                    | EXTERN ID SEMICOLON
                    | REGISTER ID SEMICOLON
                    | AUTO ID SEMICOLON'''
    print("Valid: storage-class specifier declaration")

# ---- 2.5 Looping Constructs ----
def p_loop_for(p):
    '''loop_stmt : FOR LPAREN simple_stmt SEMICOLON condition SEMICOLON simple_stmt RPAREN
                 | FOR LPAREN simple_stmt SEMICOLON condition SEMICOLON simple_stmt RPAREN LBRACE statement_list RBRACE'''
    print("Valid: for loop")

def p_loop_while(p):
    '''loop_stmt : WHILE LPAREN condition RPAREN LBRACE statement_list RBRACE'''
    print("Valid: while loop")
def p_loop_do_while(p):
    '''loop_stmt : DO LBRACE statement_list RBRACE WHILE LPAREN condition RPAREN SEMICOLON'''
    print("Valid: do-while loop")

# ---- 2.6 Expressions ----
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

# ---- 2.7 Error Handling ----
def p_error(p):
    if p:
        print(f"Syntax error at token '{p.value}' (type {p.type})")
    else:
        print("Syntax error at EOF")

parser = yacc.yacc()

# MAIN INTERACTIVE LOOP

def main():
    print("🔹 AFLL PLY Tool — C++ Constructs (Final Working Version)")
    print("Type a statement (or 'exit' to quit)\n")
    examples = [
        'cout << "Hello";',
        'cin >> a >> b;',
        'ifstream myFile;',
        'ofstream res;',
        'try { cout << "error"; } catch (e) { cout << "fix"; }',
        'throw err;',
        'struct Data { };',
        'static counter;',
        'for (int i = 0; i < 5; i++) { cout << i; }',
        'while (x < 5) { cin >> x; }',
        'do { cout << "hi"; } while (y > 5);'
    ]
    print("Examples:")
    for e in examples:
        print("  ", e)
    print("\nStart typing your own below:\n")
    while True:
        try:
            s = input('C++ > ').strip()
        except EOFError:
            break
        if not s or s.lower() == 'exit':
            break
        parser.parse(s, lexer=lexer)

if __name__ == '__main__':
    main()