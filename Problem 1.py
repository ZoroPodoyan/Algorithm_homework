"Implement Insertion Sort recursively."

def Insertion_Sort(arr, len):
    if len <= 1:
        return

    Insertion_Sort(arr, len - 1)

    i, j = arr[len - 1], len - 2

    while (j >= 0) and (arr[j] > i):
        arr[j + 1] = arr[j]
        j -= 1

    arr[j + 1] = i

arr = [50, 10, -4, 0, 1, 5, 2]
print("The given array: ", arr)
Insertion_Sort(arr, len(arr))
print("The sorted array is: ", arr)



"Implement Selection Sort recursively."

def Selection_Sort(arr, n, ind=0):
    if ind == n:
        return

    min_ind = ind
    for j in range(ind + 1, n):
        if arr[j] < arr[min_ind]:
            min_index = j

    arr[ind], arr[min_ind] = arr[min_ind], arr[ind]
    Selection_Sort(arr, n, ind + 1)

print()
arr = [-2, 1, 4, 0, 11, 44, 12, -5, 78]
print("The given array is:", arr)
Selection_Sort(arr, len(arr))
print("The sorted array is:", arr)
