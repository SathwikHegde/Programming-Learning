def merge_sorted_arrays(arr1, arr2):
    # Initialize pointers for both arrays
    i, j = 0, 0
    merged_array = []

    # Traverse both arrays and merge them
    while i < len(arr1) and j < len(arr2):
        if arr1[i] < arr2[j]:
            merged_array.append(arr1[i])
            i += 1
        else:
            merged_array.append(arr2[j])
            j += 1

    # If there are remaining elements in arr1
    while i < len(arr1):
        merged_array.append(arr1[i])
        i += 1

    # If there are remaining elements in arr2
    while j < len(arr2):
        merged_array.append(arr2[j])
        j += 1

    return merged_array

# Example usage
arr1 = [1, 3, 5, 7]
arr2 = [2, 4, 6, 8]
merged = merge_sorted_arrays(arr1, arr2)
print("Merged Array:", merged)
