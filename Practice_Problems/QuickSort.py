# Implementing quick sort for an array
# Note: average case is O(n log n)

def quicksort(array):

    # Initializing my vars
    less_than = []
    greater_than = []
    equal_to = []

    # sorting algorithm
    if len(array) > 1:

        # selecting pivot point
        pivot = array[0]

        # recursive pass and sort
        for x in array:
            if x < pivot:
                less_than.append(x)
            if x > pivot:
                greater_than.append(x)
            elif x == pivot:
                equal_to.append(x)


        return quicksort(less_than)+equal_to+quicksort(greater_than)
    else:
        return array




y = quicksort([6,4,7,1,2,9,12,3])

print(y)