from functools import reduce
number = int(input("Enter the number of input:")) 
for i in range(number):
    s= input() # taking input values in string format
    # If condition to check wheter the given input is size of 2 or not and print 0 if no input is given
    if len(s.split()) == 2:
        Sum = int(str(reduce(lambda x,y: x+y, map(int, [e[::-1] for e in s.split()])))[::-1])
        print(Sum)
    else:
        print("0")
