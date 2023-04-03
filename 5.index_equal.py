'''Given an array Arr of N positive integers. Your task is to find the elements whose value is equal
to that of its index value ( Consider 1-based indexing ).'''

size = int(input("enter the size: "))
           
n = list(map(int,input("enter array: ").strip().split()))[:size]
for i in range(0,size):
    if i+1 == n[i]:
        print(n[i])
