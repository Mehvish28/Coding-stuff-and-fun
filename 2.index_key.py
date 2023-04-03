'''Given an array A[] of N integers and an index Key. Your task is to print the element present at
index key in the array.'''


size = int(input("enter the size: "))
index = int(input("enter index key: "))

n = list(map(int,input().strip().split()))[:size]  # a good way of stripping spaces, splitting numbers and mapping them to a list of array
print(n[index])