# ##################################################################
# Given 2 arrays, create func that let's the user know whether
# theses 2 arrays contain any common items
####################################################################
# Example
# a1 = [1,2,3,4]
# a2 = [5,6,7,8]
# should return false
# a3 = [a,b,c,d]
# a4 = [d,e,f,g]
# should return true
####################################################################
# 2 parameters - arrays either ints or strs - no size limits
# return true or false
# brute force nested for loop and Big O(n^2)
###################################################################


def check_for_duplicates(first, second):

    if all(i in second for i in first):
        print("True")
        return True
    else:
        print("False")
        return False


a1 = [1, 2, 3, 4]
a2 = [5, 6, 7, 8]
a3 = ['a', 'b', 'c', 'd']
a4 = ['d', 'e', 'f', 'g']

if check_for_duplicates(a2, a1):
    print("Found duplicates")
else:
    print("No duplicates found")

if check_for_duplicates(a4, a3):
    print("Found duplicates")
else:
    print("No duplicates found")

# t ={}
# # loop through 1st arr & create object where properties == items in the array
# for i in a1:
#     if not t[a1[i]]:
#         item = a1[i]
#         t[item] = True
# print(t)
#
# # loop through 2nd arr & check if item in 2nd arr exists on created objs
# for j in a2:
#     if t[a2[j]]:
#         print("True")
