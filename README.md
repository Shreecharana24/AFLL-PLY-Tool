# AFLL PLY TOOL — C++ Language Constructs

**Lexical & Syntax Analysis using PLY (Python Lex-Yacc)**

This project implements lexical analysis and syntax analysis for selected C++ language constructs using PLY (Python Lex & Yacc). It is created as part of the **Automata, Formal Languages & Logic (AFLL)** coursework.

## 📂 Project Overview

The tool accepts C++-like statements as input and checks whether they are syntactically valid according to the grammar rules implemented using PLY.

It supports the following construct categories:

- **Input/Output:** `cout`, `cin`, `ifstream`, `ofstream`
- **Exception Handling:** `try-catch`, `throw`
- **User-Defined Types:** `struct`, `class`, `union`, `enum`
- **Storage Classes:** `static`, `extern`, `register`, `auto`
- **Looping Constructs:** `for`, `while`, `do...while`
- **Expressions:** Assignment (`=`), Increment (`++`), Comparison (`<`, `>`)

When the input matches the grammar, the tool prints validation messages such as:
> "Valid: for loop" or "Valid: cout output statement"

## 🛠 Technologies Used
- **Python 3**
- **PLY (Python Lex-Yacc)**

## 📁 Project Structure

```text
/project-folder
│
├── afllp.py        # AFLL PLY Tool (complete lexer + parser)
└── README.md
```

## 🚀 How to Run

### 1. Install dependencies
You need to install the PLY library:

```bash
pip install ply
```

### 2. Run the program
Execute the main Python script:

```bash
python main.py
```

### 3. Interaction
You will get an interactive prompt where you can type C++ code:

```text
AFLL PLY Tool — C++ Constructs (Final Working Version)
C++ > cout << "Hello";
Valid: cout output statement

C++ > for (int i = 0; i < 5; i++) { cout << i; }
Valid: for loop
```

## 📝 Supported Example Inputs

You can copy and paste these into the tool to test it:

```cpp
// Input / Output
cout << "Hello";
cin >> a >> b;
ifstream myFile;
ofstream res;

// Exception Handling
try { cout << "error"; } catch (e) { cout << "fix"; }
throw err;

// User Defined Types
struct Data { };
class X { };
enum Color { RED };

// Storage Classes
static counter;
extern value;

// Loops
for (int i = 0; i < 5; i++) { cout << i; }
while (x < 5) { cin >> x; }
do { cout << "hi"; } while (y > 5);
```

## 🚨 Error Handling

The parser detects and reports:
1.  **Illegal characters** (Lexical errors)
2.  **Syntax errors** with specific token details
3.  **Syntax errors at end-of-input** (Incomplete commands)

**Example Error Output:**
```text
Syntax error at token '{' (type LBRACE)
```

## 🎯 Purpose of the Project

The project demonstrates:
- Tokenization using regular expressions.
- Context-free grammar-based parsing.
- Building a recognizer for C++-like constructs.
- Applying Lex/Yacc concepts to practical AFLL problems.
