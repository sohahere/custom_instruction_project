# 🔧 Mini Compiler Simulation — Python Edition

Welcome to your very own **beginner-friendly compiler simulator** project! If you’ve ever wondered how code goes from something like `z = a * b + c` to machine-like instructions, this project is for you!

---

## 🎯 What’s the Goal?

We’re going to simulate what happens inside a compiler when it sees a simple instruction. Specifically, we’ll:

- **Parse a high-level statement**
- **Detect a custom instruction pattern**
- **Generate fake assembly code**
- **Execute it using Python**

And we’ll do all this with a custom instruction called `MULADD` (which multiplies and adds in one step).

---

## 🧠 Why This is Cool (and Important)

In real compilers, your code is broken down into smaller instructions and optimized to run fast. We simulate that with:

```
z = a * b + c
```

Instead of treating it as two operations, we treat it as one custom instruction:  
```
MULADD a, b, c → z
```

This is how compilers make programs **faster and more efficient**!

---

## 🧰 Files Inside the Folder

| File | Description |
|------|-------------|
| `compiler_simulator.py` | Main Python file that simulates compiler behavior |
| `README.md` | This documentation to help you understand everything |
| `output_screenshot.png` | Screenshot of the result after running the program (optional) |

---

## 💻 How to Run the Program

1. ✅ Make sure Python is installed: [Download here](https://www.python.org/downloads/)
2. ✅ Save the project files in a folder (like `compiler_sim_project`)
3. ✅ Open terminal/command prompt in that folder
4. ✅ Run the file:
```bash
python compiler_simulator.py
```
5. ✅ Enter values for a, b, and c when asked
6. ✅ Watch the output and simulated assembly

---

## 🛠️ How It Works – Step-by-Step

### 1. **Input Stage**  
We give the compiler an expression like:
```
z = a * b + c
```

### 2. **Tokenization**  
The expression is broken into parts:
```
['z', '=', 'a', '*', 'b', '+', 'c']
```

### 3. **Optimization**  
The compiler detects a pattern like `a * b + c` and replaces it with our custom instruction `MULADD`.

### 4. **Code Generation**  
We simulate assembly-like code:
```
LOAD a
LOAD b
LOAD c
MULADD a, b, c → z
```

### 5. **Execution**  
The program asks for values and computes the final result using:
```python
def muladd(a, b, c):
    return a * b + c
```

---

## 🎬 Sample Output

```
🔹 High-level Expression: z = a * b + c
🔹 Tokens: ['z', '=', 'a', '*', 'b', '+', 'c']
✅ Pattern Detected: a * b + c → Replacing with custom instruction MULADD

🔹 Generated Assembly Code:
LOAD a
LOAD b
LOAD c
MULADD a, b, c → z

🔹 Executing MULADD Instruction...
Enter value for a: 2
Enter value for b: 3
Enter value for c: 4
✅ Final Output: z = 10
```

---

## 🧑‍🏫 What You Can Explain in Class

> “This project shows how a compiler takes high-level code, breaks it down, optimizes it using a custom instruction like MULADD, then simulates assembly code and executes the result. It's a fun and visual way to understand what happens behind the scenes in a real compiler!”

---

## 🙌 Final Thoughts

- Great for beginners learning compilers  
- Simple Python simulation of a complex concept  
- Boost your confidence and impress your teacher 😎  

Feel free to add features like variable assignments, or support other expressions too!

---

Made with 🐍 Python and 💡 curiosity by YOU!
