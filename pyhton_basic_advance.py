''''try:
    num1 = float(input("Enter a dividend: "))
    num2 = float(input("Enter a divisor: "))

    div = num1 / num2
    print(f"{num1} / {num2} = {div}")

except ValueError:
    print("Invalid Input! Enter valid numbers.")

except ZeroDivisionError:
    print("Division by zero is not allowed.")

# area of triangle
try:
    base = float(input("Enter a base length: "))
    height = float(input("Enter a height: "))

    area = 0.5 * base * height

    print(f"area of triangle: {area}")

except ValueError:
    print("invalid input..!")'''


