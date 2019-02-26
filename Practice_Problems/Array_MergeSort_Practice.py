######################################################################################
# Given two unsorted or sorted Arrays. Merge them and sort them.
# Account for the arrays to be different sizes, yet similar types.
# Account for the one of them to be empty or both.
######################################################################################
#
#
#####################################################################################


def merge(array1, array2):
    result = []
    i = j = 0
    total = len(array1) + len(array2)
    # loop through until result is the length of both put together
    while len(result) != total:
        if len(array1) == i:  # if the first array is empty
            result += array2[j:]
            break
        elif len(array2) == j:  # if the second array is empty
            result += array1[i:]
            break
        elif array1[i] < array2[j]:  # if the element in array 1 < array2's element
            result.append(array1[i])
            i += 1
        else:
            result.append(array2[j])
            j += 1
    return result


print(merge([1, 2, 6, 7], [1, 3, 5, 9]))
print(merge([0, 3, 4, 31], [4, 6, 30]))


