# Phase 1: High-level input
expression = "z = a * b + c"
print("🔹 High-level Expression:", expression)

# Phase 2: Tokenization (Parsing)
tokens = expression.replace("=", " = ").replace("*", " * ").replace("+", " + ").split()
print("🔹 Tokens:", tokens)

# Phase 3: Recognize optimization pattern (a * b + c)
# For our hardcoded case, correct positions are:
# tokens = ['z', '=', 'a', '*', 'b', '+', 'c']
if tokens[2] == 'a' and tokens[3] == '*' and tokens[4] == 'b' and tokens[5] == '+' and tokens[6] == 'c':
    print("✅ Pattern Detected: a * b + c → Replacing with custom instruction MULADD")
    optimized = "MULADD a, b, c → z"
else:
    optimized = "NO OPTIMIZATION FOUND"

# Phase 4: Generate mock assembly
assembly_code = [
    "LOAD a",
    "LOAD b",
    "LOAD c",
    optimized
]

print("\n🔹 Generated Assembly Code:")
for line in assembly_code:
    print(line)

# Phase 5: Simulate execution
print("\n🔹 Executing MULADD Instruction...")

# Take user input values for a, b, c
a = int(input("Enter value for a: "))
b = int(input("Enter value for b: "))
c = int(input("Enter value for c: "))

# Custom instruction simulation
def muladd(x, y, z):
    return x * y + z

z = muladd(a, b, c)
print("✅ Final Output: z =", z)
