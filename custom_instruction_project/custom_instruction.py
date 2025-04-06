def muladd(a, b, c):
    return a * b + c

def main():
    print("=== Custom Instruction Simulator ===")
    try:
        a = int(input("Enter a: "))
        b = int(input("Enter b: "))
        c = int(input("Enter c: "))
        result = muladd(a, b, c)
        print(f"Result using custom instruction (MULADD): {result}")
    except ValueError:
        print("Please enter valid numbers.")

if __name__ == "__main__":
    main()
