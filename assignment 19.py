def sort_list(lst):
    n = len(lst)
    
    # Perform bubble sort
    for i in range(n):
        for j in range(0, n-i-1):
            # Swap if the element found is greater than the next element
            if lst[j] > lst[j+1]:
                lst[j], lst[j+1] = lst[j+1], lst[j]
    
    return lst

# Example usage
numbers = [64, 34, 25, 12, 22, 11, 90]
sorted_numbers = sort_list(numbers)
print(f"Sorted list: {sorted_numbers}")
