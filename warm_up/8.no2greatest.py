'''Given an array of N distinct elements, the task is to find all elements in array except two greatest
elements in sorted order'''

def find_2_element(arr):
    # Sort the array in ascending order
    arr.sort()

    # Remove  only the last 2 elements
    arr.pop()  # Remove maximum element, the first one
    arr.pop()
    

    # Return the final remaining element
    return arr

# Get user input for the array
n = int(input("Enter the length of the array: "))
arr = []
for i in range(n):
    element = int(input("Enter element #{}: ".format(i+1)))
    arr.append(element)

# arr=[7,8,3,4,2,9,5] # can use this for hard input
# Call the function with the array
final_element = find_2_element(arr)
print(final_element)