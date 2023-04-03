'''Bonus Question
Given an array of even size N, task is to find minimum value that can be added to an element so that
array become balanced. An array is balanced if the sum of the left half of the array elements is equal
to the sum of right half.
'''

size = int(input("Enter the size: "))
arr = list(map(int,input("Input numbers: "),strip().split()))

for i in range(0,(size/2+1)):
    sum1 = sum1 + i

for j in range((size/2), size +1):
    sum2 = sum2 + j

if sum1== sum2:
    print("Balance")
else:
    print("Not Balance")
