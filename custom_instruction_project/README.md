🛠️ Mini Compiler Project – Turning Math into Assembly!
🧠 What is this?
Ever wondered what happens when you write a simple line like this in a programming language?

c
Copy
Edit
z = a * b + c;
Behind the scenes, your computer turns that math into machine instructions that your CPU can understand. Cool, right?

This project is a mini-compiler that takes simple arithmetic expressions and converts them into assembly-style instructions — just like a real compiler does, but in a simpler, bite-sized form!

🚀 What This Compiler Can Do
Take an input like:

ini
Copy
Edit
z = a * b + c
And generate output like:

css
Copy
Edit
MOV R1, a
MOV R2, b
MUL R3, R1, R2
MOV R4, c
ADD R5, R3, R4
MOV z, R5
It respects operator precedence, uses register-based architecture, and mimics how real compilers break down instructions.

🧩 How It Works
The compiler is built in Python and goes through these phases:

Phase	What it does
Lexical Analysis	Tokenizes the input expression
Parsing	Builds a tree based on operator rules
Code Generation	Translates parsed logic into assembly
Under the hood, it uses custom logic to recursively evaluate expressions and assign them to temporary registers (R1, R2, etc.).

⚙️ Code Overview (Simplified)
Here’s a sneak peek at the Python logic:

python
Copy
Edit
MOV R1, a       # Load variable a into R1
MOV R2, b       # Load variable b into R2
MUL R3, R1, R2  # Multiply a and b -> store in R3
MOV R4, c       # Load variable c into R4
ADD R5, R3, R4  # Add (a * b) + c -> store in R5
MOV z, R5       # Save result in z
The compiler figures this all out from just one line of input!

🎯 Why This Project Rocks
✅ It brings compiler theory to life.

🧠 It shows how expressions are parsed and translated.

🔧 It’s extensible: you can add more operators, support parentheses, even target real architectures like RISC-V or x86.

🌱 Possible Extensions
Want to level up? Try adding:

Parentheses support → z = (a + b) * c

Subtraction, division, modulus

Type checking (int, float, etc.)

Real assembly output (e.g., NASM or ARM syntax)

📚 What I Learned
How a compiler pipeline works: from parsing to code generation

Importance of operator precedence and expression trees

How low-level instructions mirror high-level logic

