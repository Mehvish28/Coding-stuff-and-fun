''' Given an sorted array A of size N. Find number of elements which are less than or equal to given
element X.
'''

size = int(input("enter the size: "))
X = int(input("enter element X: "))

n = list(map(int,input("enter array: ").strip().split()))[:size]
count = 0
for i in n:
    if i <= X:
        count = count + 1
print(count)