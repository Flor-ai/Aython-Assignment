def common_elements(list1, list2):
    # Convert one of the lists to a set for faster lookups
    set1 = set(list1)
    
    # Iterate through the other list and collect common elements
    common = [item for item in list2 if item in set1]
    
    return common

# Example usage
list1 = [1, 2, 3, 4, 5, 6]
list2 = [4, 5, 6, 7, 8, 9]

print(f"Common elements: {common_elements(list1, list2)}")

