'''
Print first K (k is input) Fibonacci number
- a series of numbers in which each number ( Fibonacci number ) is the sum of the two preceding numbers.
- The simplest is the series 1, 1, 2, 3, 5, 8, etc.
'''
import os
#k = int(input('Enter number to generate Fibonacci series : \n'))
k = int(os.environ.get("Fibonacci",None))
fib_series=[1]
element = 0
for i in range(1,k):
    fib_series.append(fib_series[-1]+element)
    element = fib_series[-2]
    print(fib_series)

print ("Second approach")

count = 0
n1 = 0
n2 = 1
while (count<k):
    nth = n1+n2
    n1 = n2
    n2 = nth
    count+=1
    print(n1, end=',')






