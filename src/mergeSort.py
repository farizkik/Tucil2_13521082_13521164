# Merge Sort Algorithm Using Divide and Conquer Approach for Array

# in default, sorting would be ascending
def mergeSort(arr, asc = 1):
    if len(arr) <= 1:
        return arr
    
    # Divide
    mid = len(arr) // 2
    left_arr = arr[:mid]
    right_arr = arr[mid:]
    
    left_arr = mergeSort(left_arr, asc)
    right_arr = mergeSort(right_arr, asc)

    # conquer
    return merge(left_arr, right_arr, asc)


# conquer implementation
def merge(left_arr, right_arr, asc):
    result = []
    left_idx = 0
    right_idx = 0
    
    while left_idx < len(left_arr) and right_idx < len(right_arr):

        # if ascending is True or 1 
        if (asc == 1):    
            if left_arr[left_idx] <= right_arr[right_idx]:
                result.append(left_arr[left_idx])
                left_idx += 1
            else:
                result.append(right_arr[right_idx])
                right_idx += 1
        
        # if ascending is False or any other than 1, hence descending
        else:
            if left_arr[left_idx] >= right_arr[right_idx]:
                result.append(left_arr[left_idx])
                left_idx += 1
            else:
                result.append(right_arr[right_idx])
                right_idx += 1

    if left_idx < len(left_arr):
        result.extend(left_arr[left_idx:])
    if right_idx < len(right_arr):
        result.extend(right_arr[right_idx:])
        
    return result

# Testing
# arr = [2.3, 3, 4.5, 2, 5, 1.5, -99.0, 203.000, -4323.000001, -2]
# arr = ['a', 's', 'n', 'g', 'l', 'r', 'u', 'c', 'b']
# print(mergeSort(arr, True))
# print(mergeSort(arr, 1))
# print(mergeSort(arr))
# print(mergeSort(arr, False))
# print(mergeSort(arr, 3))