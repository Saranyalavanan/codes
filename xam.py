import math

def operations():
    print("Select a mathematical function:")
    print("1: Factorial")
    print("2: GCD")
    print("3: LCM")
    print("4: Square Root")
    x = int(input("Enter your choice: "))
    
    if x == 1:
        a = int(input("Enter a number : "))
        print(f"Factorial of {a}: {math.factorial(a)}")
    elif x == 2:
        a = int(input("Enter first number: "))
        b = int(input("Enter second number: "))
        print(f"GCD of {a} and {b}: {math.gcd(a, b)}")
    elif x == 3:
        a = int(input("Enter first number : "))
        b = int(input("Enter second number : "))
        print(f"LCM of {a} and {b}: {math.lcm(a, b)}")
    elif x == 4:
       a = int(input("Enter a number : "))
       print(f"Square Root of {a}: {math.sqrt(a)}")
   

if __name__ == "__main__":
    operations()
