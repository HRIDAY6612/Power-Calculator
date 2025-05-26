
# Power Calculator Program by Varisha

def calculate_powers(base, n):
    print(f"\nPowers of {base} up to {n}:")
    for i in range(1, n + 1):
        result = base ** i
        print(f"{base}^{i} = {result}")

def main():
    print("Welcome to Varisha's Power Calculator!")
    try:
        base = float(input("Enter the base number: "))
        n = int(input("Enter the maximum power (n): "))
        
        if n < 1:
            print("Please enter a positive integer for the power.")
            return
        
        calculate_powers(base, n)
    except ValueError:
        print("Invalid input. Please enter numeric values.")

if __name__ == "__main__":
    main()
