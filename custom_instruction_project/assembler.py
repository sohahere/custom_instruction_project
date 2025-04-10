# assembler.py
# Custom assembler for: z = a * b + c

# Opcode for MULADD
OPCODE_MULADD = 0x2A  # Custom opcode (00101010)

# Register mapping (example):
# z = R4, a = R1, b = R2, c = R3
reg_z = 4
reg_a = 1
reg_b = 2
reg_c = 3

# Instruction format: [Opcode (8)] [z (6)] [a (6)] [b (6)] [c (6)]
instruction = (OPCODE_MULADD << 24) | (reg_z << 18) | (reg_a << 12) | (reg_b << 6) | reg_c

# Write the instruction to binary file (simulating an .o file)
with open("program.bin", "wb") as f:
    f.write(instruction.to_bytes(4, byteorder='big'))

print("✅ Compiled to program.bin")
