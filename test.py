from functools import reduce
def call(Input):
    String = Input
    Sum = int(str(reduce(lambda x,y: x+y, map(int, [e[::-1] for e in String.split()])))[::-1])
    return Sum

def Check(Input):
    number = Input
    if isinstance(number, int) == True:
        if number <= 10000 and number > 0:
            return Input
        else:
            print("Error: Out of Range")
            return 0
    else:
        print("Error: Data-Type ")
        return 0

def main():
    INPUT = input("Enter the count of input: ")
    INPUT = Check(INPUT)
    for i in range(INPUT):
        value = input()
        if len(value.split())==2:
            Value = value.split()
            if Value[0].isnumeric()== True and Value[1].isnumeric()== True:
                Result = call(value)
                print(Result)
            else:
                print("Error: Non-Positive Integer value")
        else:
            print("0")

if __name__ == "__main__":
    main()
