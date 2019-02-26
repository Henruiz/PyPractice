def factorial(num):
    if num == 1:
        return 1
    else:
        return num * factorial(num-1)


number = input("Input number to find Factorial of it: ")
print(factorial(int(number)))