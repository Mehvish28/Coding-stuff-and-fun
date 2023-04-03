# Given an array of N integers. Your task is to print the sum of all of the integers.

size = int(input("enter the size: "))
n = list(map(int,input().strip().split()))[:size]  # a good way of stripping spaces, splitting numbers and mapping them to a list of array
sum =0
for i in n:
    sum = sum + i

print(sum)