def merge_sort(arr):
    if len(arr) <= 1:
        return arr

    # Split array into two halves
    mid = len(arr) // 2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])

    # Merge the sorted halves
    return merge(left, right)


def merge(left, right):
    result = []
    i = j = 0

    # Compare elements and merge
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1

    # Add remaining elements
    result.extend(left[i:])
    result.extend(right[j:])
    return result


# Example usage

n = int(input("Enter the number of orders : "))
arr = []
for i in range(n):
    arr.append(int(input("Enter delivery time : ")))

print("Original Delivery Times : ", arr)
sorted_arr = merge_sort(arr)
print("Sorted Delivery Times : ", sorted_arr)
