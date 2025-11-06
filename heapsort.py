# Heap Sort Program in Python
# Sorts an array in ascending order using Max-Heap

def heapify(arr, n, i):
    largest = i        # Initialize largest as root
    left = 2 * i + 1   # left child index
    right = 2 * i + 2  # right child index

    # If left child is larger than root
    if left < n and arr[left] > arr[largest]:
        largest = left

    # If right child is larger than largest so far
    if right < n and arr[right] > arr[largest]:
        largest = right

    # If largest is not root
    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]  # Swap
        heapify(arr, n, largest)  # Recursively heapify the affected subtree


def heapSort(arr):
    n = len(arr)

    # Step 1: Build a maxheap
    for i in range(n // 2 - 1, -1, -1):
        heapify(arr, n, i)

    # Step 2: Extract elements from heap one by one
    for i in range(n - 1, 0, -1):
        # Move current root to end
        arr[i], arr[0] = arr[0], arr[i]
        # call max heapify on the reduced heap
        heapify(arr, i, 0)


# ---------- Main Code ----------
arr = [12, 11, 13, 5, 6, 7]
print("Original Array:", arr)

heapSort(arr)

print("Sorted Array in Ascending Order:", arr)
