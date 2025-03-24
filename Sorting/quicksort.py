def partition(arr, low, high):
    pivot = arr[high]

    i = low - 1 # First case is -1.

    for j in range(low, high):
        if arr[j] < pivot:
            i += 1
            swap(arr, i, j) 
            print(f"processing: {arr}")
    
    swap(arr, i + 1, high)
    print(f"processing: {arr}")
    return i + 1

def swap(arr, i, j):
    arr[i], arr[j] = arr[j], arr[i]

def quicksort(arr, low, high):
    if low < high:
        pi = partition(arr, low, high)
        print(arr)
        # Pivot is in the middle. Sort left and right of it.
        quicksort(arr, low, pi - 1)     
        quicksort(arr, pi + 1, high)

if __name__ == '__main__':
    arr = [12,5,8,130,5648,16,14,9]
    print(f"before array {arr}")

    quicksort(arr, 0, len(arr) - 1)
    print(f"after quicksort {arr}")