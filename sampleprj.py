print("Hello world")

print("This is the sample program for testing the branches in the git")





def sqrt_newton(n, precision=0.00001):
    guess = n / 2  # Initial guess
    while abs(guess * guess - n) > precision:
        guess = (guess + n / guess) / 2
    return guess

num = 25
print(sqrt_newton(num))