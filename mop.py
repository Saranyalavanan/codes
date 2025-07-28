import math

def operators():
    a=int(input("Enter the a value:"))
    b=int(input("Enter the b value:"))
    print(f"Addition (a + b): {a + b}")
    print(f"Subtraction (a - b): {a - b}")
    print(f"Multiplication (a * b): {a * b}")
    print(f"Division (a / b): {a / b}")
    print(f"Floor Division (a // b): {a // b}")
    print(f"Modulus (a % b): {a % b}")
    print(f"Exponentiation (a ** b): {a ** b}")


def advanced_math_functions():
    
    num = 12
    angle = math.radians(30)

    print(f"\nSquare Root of {num}: {math.sqrt(num)}")
    print(f"Factorial of 7: {math.factorial(7)}")
    print(f"Greatest Common Divisor (GCD) of 56 and 16: {math.gcd(56, 16)}")
    print(f"LCM of 21 and 42: {math.lcm(21, 42)}")
    print(f"Absolute Value of -50: {math.fabs(-50)}")
    print(f"Ceiling of 10.8: {math.ceil(10.8)}")
    print(f"Floor of 8.6: {math.floor(8.6)}")
    print(f"Power (8^2): {math.pow(8, 2)}")
    print(f"Logarithm (log(204)): {math.log(204)}")
    print(f"Logarithm base 10 (log10(100)): {math.log10(100)}")
    print(f"Exponential (e^3): {math.exp(3)}")



if __name__ == "__main__":
    print("<<< OPERATORS >>>")
    operators()
    print("---------------------------------------------------")
    print("<<< ADVANCED MATH FUNCTIONS >>>")
    advanced_math_functions()
    
    
    
    

 





      
    
    
