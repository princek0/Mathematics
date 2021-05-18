# Sorting algorithms.

def bubble(list):  # Bubble sort algorithm for lists.
    length = len(list)

    for i in range(length):
        for item in range(length - i - 1):
            if list[item] > list[item + 1]:
                list[item], list[item + 1] = list[item + 1], list[item]

    return list


def merge(list):  # Merge sort algorithm for lists.
    if len(list) > 1:

        # Splits the main list into sub lists.
        midpoint = len(list) // 2
        left_list = list[:midpoint]
        right_list = list[midpoint:]

        merge(left_list)
        merge(right_list)

        i, j, k = 0, 0, 0  # Counters for items in lists.

        while i < len(left_list) and j < len(right_list):
            if left_list[i] < right_list[j]:  # If item in left list is less than item in right list.
                list[k] = left_list[i]
                i += 1
            else:  # If item in right list is less than item in less list.
                list[k] = right_list[j]
                j += 1
            k += 1

        """
        It is possible that all items in one of the lists (left or right) were already moved to the main list
        and so the while loop above will end and thus the code below is needed for the case when there are items
        yet to be moved.
        """

        while i < len(left_list):
            list[k] = left_list[i]
            i += 1
            k += 1

        while j < len(right_list):
            list[k] = right_list[j]
            j += 1
            k += 1

    return list


# Searching algorithms.

def linear(list, item):  # linear search algorithm for lists. Returns where in the list the specified item is.
    for i in range(len(list)):
        if list[i] == item:
            return i


def binary(list, item):  # Binary search algorithm for lists. Returns where in the list the specified item is.
    # List must be sorted before using this algorithm.

    first_item = 0
    last_item = len(list) - 1
    position = -1

    while list[position] != item and first_item <= last_item:
        midpoint = (first_item + last_item) // 2
        if list[midpoint] == item:
            position = midpoint
        else:
            if item < list[midpoint]:
                last_item = midpoint - 1
            else:
                first_item = midpoint + 1

    return position


def interpol(list, item):  # Interpolation search algorithm for lists. Returns where in the list the specified item is.
    first_item = 0
    last_item = len(list) - 1

    while first_item <= last_item and list[first_item] <= item <= list[last_item]:
        index = first_item + int(
            (float(last_item - first_item) / (list[last_item] - list[first_item]) * (item - list[first_item])))
        if list[index] == item:
            return index
        if list[index] < item:
            first_item = index + 1
        else:
            last_item = index - 1

    return index
