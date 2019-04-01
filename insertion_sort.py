def insertion_sort(arr):
    for i in range(len(arr)):
        # first step is to find any values "out of order", meaning a place where a smaller value is to the right of a larger value
        if arr[i-1] > arr[i]: 
            minval = arr[i] # here we'll store this value in a temp variable since we'll be overwriting it in the following block
            
            # next step is to move all values greater than our temp to the right by one index; we'll start at the current position (one left of our moving value), and move backwards along the array
            for j in range(i-1, -1, -1):
                if arr[j] > minval:
                    arr[j+1] = arr[j]
                    arr[j] = minval
    return arr

print(insertion_sort([5, 2, 10, 7, 108, 74, 59, 60, 58]))