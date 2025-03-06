import math

num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))

# Add the numbers
sum_result = num1 + num2

# Print the result
print("The sum is:", sum_result)

if sum_result % 2 == 0:
    print(sum_result, "is even")
else:
    print(sum_result, "is odd")

z = math.sqrt(sum_result)
print(z)
