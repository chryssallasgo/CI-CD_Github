def add(x, y):
    """This function adds two numbers."""
    return x + y

def subtract(x, y):
    """This function subtracts the second number from the first."""
    return x - y

def multiply(x, y):
    """This function multiplies two numbers."""
    return x * y

def divide(x, y):
    """This function divides the first number by the second."""
    if y == 0:
        raise ValueError("Cannot divide by zero.")
    return x / y

def greet(name="Guest"):
    """This function returns a simple greeting, with name title-cased."""
    return f"Hello, {name.title()}!"

if __name__ == "__main__":
    print(f"Adding 5 and 3: {add(5, 3)}")
    print(f"Subtracting 10 from 20: {subtract(20, 10)}")
    print(f"Multiplying 4 and 6: {multiply(4, 6)}")
    print(f"Dividing 15 by 3: {divide(15, 3)}")
    print(greet("world"))
    print(greet())  # default greeting
