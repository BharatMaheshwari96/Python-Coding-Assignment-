from functools import reduce
number = int(input("Enter the number of input:")) 
for i in range(number):
    s= input() # taking input values in string format
    Sum = int(str(reduce(lambda x,y: x+y, map(int, [e[::-1] for e in s.split()])))[::-1])
    print(Sum)
