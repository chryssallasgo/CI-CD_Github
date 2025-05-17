def add(x, y):
  """This function adds two numbers."""
  return x + y

def subtract(x, y):
  """This function subtracts the second number from the first."""
  return x - y

def divide(x, y):
  """This function divides the first number by the second."""
  if y == 0:
    return "Error: Cannot divide by zero."
  return x / y

def greet(name):
  """This function returns a simple greeting."""
  return f"Hello, {name}!"

if __name__ == "__main__":
  print(f"Adding 5 and 3: {add(5, 3)}")
  print(f"Subtracting 10 from 20: {subtract(20, 10)}")
  print(f"Dividing 10 by 2: {divide(10, 2)}")
  print(greet("World"))