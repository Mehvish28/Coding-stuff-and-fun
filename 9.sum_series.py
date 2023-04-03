'''Write a program 
to find the sum of the given series 1+2+3+ . . . . . .(N terms)'''

N = int(input())
sum = 0
for i in range(1,N+1,1):
    sum = sum + i
print(sum)