global user_input

counter = 0
def fibinacci(num1, num2, counter):
    counter += 1
    if (num1 > num2):
        return 1

    if counter > int(user_input):
        return ("Finished")

    print(num1)

    return fibinacci(num2, num1+num2, counter)

try:
    user_input = input("Please enter a number from 1-100: ")
except TypeError:
    print("This is a type error make sure you type an interger")



num1 = 0
num2 = 1

fibinacci(num1, num2, counter)



#
# for i in range(user_input):
#     if i == 0:
#         print(num1, end=", ")
#     if i == 1:
#         print(num2, end=", ")
#
#     next = num1 + num2
#     num1 = num2
#     num2 = next
#
#     print(next, end=", ")


