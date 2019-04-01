def selection_sort(arr):
    for i in range (len(arr)):
        minval = arr[i]
        for j in range(i,len(arr)):
            if arr[j] < minval:
                minval = arr[j]
                arr[j] = arr[i]
                arr[i] = minval
    return arr

arr = [5, 12, 4, 50, 10]
print(selection_sort(arr))