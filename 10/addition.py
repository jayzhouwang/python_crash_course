print("Enter two numbers and I will return you the sum of these numbers.")
input1 = input("Please enter the first number:")
input2 = input("Please enter the second number:")
try:
    num1 = int(input1)
    num2 = int(input2)
except ValueError:
    print("Please enter numbers!")
else:
    print(f"{num1} + {num2} = {num1 + num2}")