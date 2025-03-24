
def merge(arr, low, middle, high):
    n1 = middle - low + 1 
    n2 = high - middle

    Left = [0] * n1
    Right = [0] * n2

    for i in range(n1):
        Left[i] = arr[low + i]
    for j in range(n2):
        Right[j] = arr[ (middle + 1) + j] # middle + 1 because of floor operation in "//"
    i = 0
    j = 0
    k = low

    while i < n1 and j < n2:
        if Left[i] < Right[j]:
            arr[k] = Left[i]
            i += 1
        else:
            arr[k] = Right[j]
            j += 1
        k += 1

    while i < n1:
        arr[k] = Left[i]
        i += 1
        k += 1
    while j < n2:
        arr[k] = Right[j]
        j += 1
        k += 1
    

 
def mergesort(arr, low, high):
    if low < high:
        middle = (high + low) // 2  
        mergesort(arr, low, middle)
        mergesort(arr, middle + 1, high)
        merge(arr, low, middle, high)


if __name__ == '__main__':
    arr = [12,5,8,130,5648,16,14,9]
    print(f"before merge sort {arr}")

    mergesort(arr, 0, len(arr) - 1)
    print(f"after merge sort {arr}")