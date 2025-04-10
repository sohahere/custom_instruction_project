# objdump.py
# Custom disassembler (like objdump) for custom instruction set

def decode_instruction(inst):
    opcode = (inst >> 24) & 0xFF
    z = (inst >> 18) & 0x3F
    a = (inst >> 12) & 0x3F
    b = (inst >> 6) & 0x3F
    c = inst & 0x3F

    if opcode == 0x2A:
        return f"MULADD R{z}, R{a}, R{b}, R{c}"
    else:
        return "UNKNOWN INSTRUCTION"

# Read the binary file
with open("program.bin", "rb") as f:
    bytes_data = f.read()
    inst = int.from_bytes(bytes_data, byteorder='big')
    hex_str = ' '.join(f"{b:02x}" for b in bytes_data)
    decoded = decode_instruction(inst)

# Simulate objdump output
print("00000000 <main>:")
print(f"   0:\t{hex_str}\t{decoded}")
