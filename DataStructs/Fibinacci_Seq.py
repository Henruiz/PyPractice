# try:
    user_input = int(input("Please enter a number from 1-100: "))
# except:
#     if user_input is not int:
#         print('Sorry wrong input try again')

num1 = 0
num2 = 1


for i in range(user_input):
    if i == 0:
        print(num1, end=", ")
    if i == 1:
        print(num2, end=", ")

    next = num1 + num2
    num1 = num2
    num2 = next

    print(next, end=", ")