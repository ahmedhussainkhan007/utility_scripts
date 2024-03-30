def main ():
    pass

if_name_=="_main_:"
   main()def add(num1, num2):
  """Adds two numbers together and returns the result."""
  return num1 + num2

def subtract(num1, num2):
  """Subtracts one number from another and returns the result."""
  return num1 - num2

def multiply(num1, num2):
  """Multiplies two numbers together and returns the result."""
  return num1 * num2

def divide(num1, num2):
  """Divides one number by another and returns the result.
  Handles division by zero error."""
  if num2 == 0:
    return "Error: Cannot divide by zero."
  else:
    return num1 / num2

def main():
  """Runs the calculator program."""
  print("Welcome to the Simple Calculator!")

  while True:
    # Get user input for operation
    operation = input("Choose an operation (+, -, *, /): ")

    # Get user input for numbers
    try:
      num1 = float(input("Enter the first number: "))
      num2 = float(input("Enter the second number: "))
    except ValueError:
      print("Invalid input. Please enter numbers only.")
      continue

    # Perform calculation based on operation
    if operation == "+":
      result = add(num1, num2)
    elif operation == "-":
      result = subtract(num1, num2)
    elif operation == "*":
      result = multiply(num1, num2)
    elif operation == "/":
      result = divide(num1, num2)
    else:
      print("Invalid operation. Please choose +, -, *, or /.")
      continue

    # Print the result
    print(f"{num1} {operation} {num2} = {result}")

    # Ask user if they want to continue
    choice = input("Do you want to perform another calculation? (y/n): ")
    if choice.lower() != "y":
      break

  print("Thank you for using the Simple Calculator!")

if __name__ == "__main__":
  main()
  