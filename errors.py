# while True:
#     try:
#         a = int(input("Enter a number 1: "))
#         b = int(input("Enter a number 2: "))

#         print(f"The division of {a} and {b} is {a / b}")

#     except ValueError:
#         print("Invalid input. Please enter valid typecast.")

#     except ZeroDivisionError:
#         print("Division by zero is not allowed.")

#     except Exception as e:
#         print("Unknown error occurred:", e)


a = int(input("Enter a number 1: "))
b = int(input("Enter a number 2: "))

if b == 0:
    raise ValueError("Division by zero is not allowed.")

print(f"The division of {a} and {b} is {a / b}")