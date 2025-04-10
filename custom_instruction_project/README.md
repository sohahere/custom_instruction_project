# 🔧 Custom Instruction Compiler & objdump Simulation

Welcome! This is a mini-project that simulates how a compiler and an `objdump` tool would handle a **custom instruction** of the form:

z = a * b + c

yaml
Copy
Edit

---

## 🚀 What We Built

We designed a **custom instruction** called `MULADD` and implemented:

1. A **compiler** (`assembler.py`) that encodes this instruction into a binary `.bin` file.
2. A **disassembler** (`objdump.py`) that reads the binary and shows a human-readable output—just like a real `objdump`.

---

## 🧠 The Custom Instruction: MULADD

MULADD dest, src1, src2, src3

yaml
Copy
Edit

This performs:

dest = src1 * src2 + src3

yaml
Copy
Edit

We use 5 fields packed into a 32-bit instruction:

| Field     | Size     | Example   |
|-----------|----------|-----------|
| Opcode    | 8 bits   | `0x2A`    |
| dest (z)  | 6 bits   | R4        |
| src1 (a)  | 6 bits   | R1        |
| src2 (b)  | 6 bits   | R2        |
| src3 (c)  | 6 bits   | R3        |

---

## 🛠️ File Structure

📁 custom-compiler/ ├── assembler.py # Encodes the instruction into binary ├── objdump.py # Decodes binary back to readable form ├── program.bin # Binary output of assembler └── README.md # You're reading it!

yaml
Copy
Edit

---

## 🔧 How It Works

### 1️⃣ `assembler.py` – Compiler

```python
OPCODE_MULADD = 0x2A
reg_z, reg_a, reg_b, reg_c = 4, 1, 2, 3
instruction = (OPCODE_MULADD << 24) | (reg_z << 18) | (reg_a << 12) | (reg_b << 6) | reg_c
with open("program.bin", "wb") as f:
    f.write(instruction.to_bytes(4, byteorder='big'))
🔹 This encodes the instruction into a .bin file that mimics a real compiled object file.

2️⃣ objdump.py – Disassembler
python
Copy
Edit
def decode_instruction(inst):
    opcode = (inst >> 24) & 0xFF
    z = (inst >> 18) & 0x3F
    a = (inst >> 12) & 0x3F
    b = (inst >> 6) & 0x3F
    c = inst & 0x3F
    return f"MULADD R{z}, R{a}, R{b}, R{c}"
🔹 This reads program.bin, extracts fields, and reconstructs a readable version like:

css
Copy
Edit
00000000 <main>:
   0:    2a 10 08 43    MULADD R4, R1, R2, R3
🧪 How to Run
Step 1: Compile the instruction
bash
Copy
Edit
python3 assembler.py
Step 2: Disassemble it
bash
Copy
Edit
python3 objdump.py
🎉 Done! You'll see output like MULADD R4, R1, R2, R3.

💡 Why This Project?
To understand how instructions are encoded.

To simulate a tiny real-world compiler and disassembler.

To learn bit manipulation and binary file handling in Python.