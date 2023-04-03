'''. Given an array of length N, at each step it is reduced by 1 element. In the first step the maximum
element would be removed, while in the second step minimum element of the remaining array would
be removed, in the third step again the maximum and so on. Continue this till the array contains only 1
element. And find the final element remaining in the array'''

def find_last_element(arr):
    # Sort the array in descending order
    arr.sort(reverse=True)

    # Remove elements alternatively until only one is left
    while len(arr) > 1:
        arr.pop(0)  # Remove maximum element, the first one
        if len(arr) > 1:
            arr.pop()  # Remove minimum element, the last one

    # Return the final remaining element
    return arr[0]

# Get user input for the array
n = int(input("Enter the length of the array: "))
arr = []
for i in range(n):
    element = int(input("Enter element #{}: ".format(i+1)))
    arr.append(element)

# arr=[7,8,3,4,2,9,5]
# Call the function with the array
final_element = find_last_element(arr)
print(final_element)