'''Given an array of size N and you have to tell whether the array is perfect or not. An array is said
to be perfect if it's reverse array matches the original array. If the array is perfect then print
"PERFECT" else print "NOT PERFECT".
'''

size = int(input("enter the size: "))
rev =[]          
n = list(map(int,input("enter array: ").strip().split()))[:size]

for i in range(size-1,-1,-1):
  rev.append(n[i])
if n == rev:
  print("PERFECT")
else:
  print("NOT PERFECT")