"""Problem using a Hash Table

    Given an array, print out the first reccuring number or string.
    a1 = [5,1,2,5,1,7,5,9,2,3,]
    returns 5

    a2 = [2,1,1,2,3,5,1,2,4]
    returns 1

    a3 = [2,3,4,5]
    returns no recurring item
"""

# O(n^2)


def first_recurring_item(input):
    for i in input:
        for  j in input:
            if input[i] == input[j]:
                return(input[i])

    return ('No Dice')

print('-----------------------------------------------')

a1 = [5, 1, 2, 5, 1, 7, 5, 9, 2, 3]
ans = first_recurring_item(a1)
print(ans)

a2 = [2, 1, 1, 2, 3, 5, 1, 2, 4]
ans = first_recurring_item(a2)
print(ans)

a3 = [2, 3, 4, 5]
ans = first_recurring_item(a3)
print(ans)


print('-----------------------------------------------')



# using a hash table
def first_recurring_item_2(input):
    d = {}
    # looping through each char in string
    for i in input:
        if i in d:  # if char is already present return char
            return i
        else:
            d[i] = 0  # add to has
    return 'No Recursion Found'


ans1 = first_recurring_item_2(['5', '1', '2', '5', '1', '7', '5', '9', '2', '3', '6', '7' ])
print(ans1)

ans2 = first_recurring_item_2(['2', '1', '1', '2', '3', '5', '1', '2', '4'])
print(ans2)

ans3 = first_recurring_item_2(['2', '3', '4', '5'])
print(ans3)

print('-----------------------------------------------')

