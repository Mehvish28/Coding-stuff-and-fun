'''Q4. You are given an array A of size N. You need to print elements of A in alternate order (starting
from index 0).
'''

size = int(input("enter the size: "))
           
n = list(map(int,input("enter array: ").strip().split()))[:size]
for i in range(0,len(n),2):  # use size or len(n), same thing
    print(n[i], end=' ')