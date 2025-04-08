class RegisterGenerator:
    def __init__(self):
        self.count = 1

    def new_register(self):
        reg = f"R{self.count}"
        self.count += 1
        return reg

class AssemblyCompiler:
    def __init__(self):
        self.reg_gen = RegisterGenerator()
        self.instructions = []

    def compile(self, expr):
        lhs, rhs = expr.replace(" ", "").split("=")
        result_reg = self._parse_expression(rhs)
        self.instructions.append(f"MOV {lhs}, {result_reg}")
        return self.instructions

    def _parse_expression(self, expr):
        # Handle + and -
        for op in ['+', '-']:
            parts = self._split(expr, op)
            if parts:
                left_reg = self._parse_expression(parts[0])
                right_reg = self._parse_expression(parts[1])
                result_reg = self.reg_gen.new_register()
                self.instructions.append(f"{'ADD' if op == '+' else 'SUB'} {result_reg}, {left_reg}, {right_reg}")
                return result_reg

        # Handle * and /
        for op in ['*', '/']:
            parts = self._split(expr, op)
            if parts:
                left_reg = self._parse_expression(parts[0])
                right_reg = self._parse_expression(parts[1])
                result_reg = self.reg_gen.new_register()
                self.instructions.append(f"{'MUL' if op == '*' else 'DIV'} {result_reg}, {left_reg}, {right_reg}")
                return result_reg

        # Base case: variable or constant
        reg = self.reg_gen.new_register()
        self.instructions.append(f"MOV {reg}, {expr}")
        return reg

    def _split(self, expr, operator):
        depth = 0
        for i in range(len(expr)-1, -1, -1):
            if expr[i] == ')':
                depth += 1
            elif expr[i] == '(':
                depth -= 1
            elif expr[i] == operator and depth == 0:
                return [expr[:i], expr[i+1:]]
        return None

# === Example Usage ===
compiler = AssemblyCompiler()
input_expr = "z = a * b + c"
asm = compiler.compile(input_expr)

print("Assembly Code:")
for line in asm:
    print(line)
