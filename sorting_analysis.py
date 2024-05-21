from random import randint
import timeit
import copy

def selection_sort(num_list):
    """Iteratively finds the minimum number in a list of numbers and places it
    in the correct place on the left side of the list. Similar to insertion sort
    in that it grows a sorted from the left side of the list. After the first element
    is placed, the subsequent minimum numbers will be placed to the right of the 
    preceding minimum number.

    Parameters
        num_list: a list of numbers
            The list of numbers to be sorted.

    Returns
        Nothing. This function sorts in-place.
    """
    for i in range(len(num_list)):
        minimum_num = num_list[i]
        minimum_index = i
        for j in range(i, len(num_list)):
            if (num_list[j] < minimum_num):
                minimum_num = num_list[j]
                minimum_index = j
        temp = num_list[i]
        num_list[i] = minimum_num
        num_list[minimum_index] = temp

def bubble_sort(num_list):
    """Iterates through a list of numbers and swaps two elements if the first 
    element is greater than the second element. The larger numbers "bubble" to
    the top of the list (right side).

    Parameters
        num_list: a list of numbers
            The list of numbers to be sorted.

    Returns
        Nothing. This functions sorts in-place.
    """
    for i in range(len(num_list)):
        for j in range(len(num_list) - 1):
            if (num_list[j] > num_list[j + 1]):
                temp = num_list[j]
                num_list[j] = num_list[j + 1]
                num_list[j + 1] = temp

def insertion_sort(num_list):
    """Iterates through a list of numbers and builds a sorted list on the left
    end of the list. During iteration, each encountered element is swapped 
    with the element before it until it is in the correct place on the sorted
    side. 

    Parameters
        num_list: a list of numbers
            The list of numbers to be sorted.
    
    Returns
        Nothing. This function sorts in-place.
    """
    for i in range(len(num_list)):
        j = i - 1
        k = i
        while (num_list[k] < num_list[j] and j >= 0):
            temp = num_list[j]
            num_list[j] = num_list[k]
            num_list[k] = temp
            k = j
            j -= 1

def merge_sort(num_list):
    """Recursively divides a list into two smaller lists, left and right, until 
    each list contains one number. These lists are inherently sorted. These
    one number lists are then passed as arguments to the merge() function in 
    order to combine them. The base case is if the list to be sorted only has
    one number.

    Parameters
        num_list: list of numbers
            The list of numbers to be sorted.
    
    Returns
        A sorted list of numbers
    """
    if (len(num_list) == 1):
        return num_list
    else:
        middle = int(len(num_list) / 2)
        left = num_list[:middle]
        right = num_list[middle:len(num_list)]
        l = merge_sort(left)
        r = merge_sort(right)
        return merge(l, r)

def merge(left, right):
    """Helper function to the merge_sort() function. Merges the two list parameters
    by repeatedly appending the lowest head from the two lists into a result list.
    It then iterates through whichever list is not empty and repeatedly appends
    the first element to the result list until the list is empty.

    Parameters
        left: list of numbers
            The list of numbers to the left side of a dividing index
        right: list of numbers
            The list of numbers to the right side of a dividing index

    Returns
        result: list of numbers
            A sorted list of numbers containing those numbers from
            the left and right list
    """
    result = []
    while left != [] and right !=[]:
        if left[0] < right[0]:
            result.append(left[0])
            left = left[1:]
        else:
            result.append(right[0])
            right = right[1:]

    while left != []:
        result.append(left[0])
        left = left[1:]
    while right != []:
        result.append(right[0])
        right = right[1:]
    return result

def quick_sort(num_list):
    """Recursively sorts lists of numbers that are either lower than the pivot
    or higher than the pivot. Since the "middle" list contains those numbers 
    that are equal to the pivot, it is already sorted. It then concatenates the
    sorted lower list, middle list, and higher list. The base case is if the
    length of the list to be sorted has a length of 1 or lower; these lists are
    already sorted.

    Parameters
        num_list: list of numbers
            The list of numbers to be sorted

    Returns
        A sorted list
    """
    if (len(num_list) <= 1):
        return num_list
    else:
        low, middle, high = partition(num_list)
        return quick_sort(low) + middle + quick_sort(high)

def partition(num_list):
    """Helper function to the quick_sort() function. Resembles the "fat partition" 
    named by Bentley and Mcllory. This function chooses the pivot to be the last
    element of the list parameter and creates three lists from the list parameter:
    a list containing numbers that are less than the pivot, a list containing 
    numbers that are equal to the pivot, and a list containing numbers that are 
    greater than the pivot.

    Parameters
        num_list: list of numbers
            The list of numbers to be partitioned. 

    Returns
        low: list of numbers
            The list of numbers that are less than the pivot.
        middle: list of numbers
            The list of numbers that are equal to the pivot.
        high: list of numbers
            The list of numbers that are greater than the pivot.
    """
    pivot = num_list[len(num_list) - 1]
    low = [x for x in num_list if x < pivot]
    middle = [x for x in num_list if x == pivot]
    high = [x for x in num_list if x > pivot]
    return low, middle, high    

nums = []

for i in range(10000):
    nums.append(randint(0, 10000))

ls1 = copy.copy(nums)
ls2 = copy.copy(nums)
ls3 = copy.copy(nums)
ls4 = copy.copy(nums)
ls5 = copy.copy(nums)

start = timeit.default_timer()
selection_sort(ls1)
print(f"Selection Sort: {timeit.default_timer() - start}")
start = timeit.default_timer()
bubble_sort(ls2)
print(f"Bubble Sort: {timeit.default_timer() - start}")
start = timeit.default_timer()
insertion_sort(ls3)
print(f"Insertion Sort: {timeit.default_timer() - start}")
start = timeit.default_timer()
test = merge_sort(ls4)
print(f"Merge Sort: {timeit.default_timer() - start}")
start = timeit.default_timer()
test1 = quick_sort(ls5)
print(f"Quick Sort: {timeit.default_timer() - start}")
