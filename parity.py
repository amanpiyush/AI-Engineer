def main():
    x = int(input("Enter the Num : \n"))
    if evenOff(x):
        print(f"Even Number {x}")
    else:
        print(f"Odd Number {x}")



def evenOff(x):
    # if x % 2 == 0:
    #     return True

    # else:
    #     return False

    #Refined Version
    # return True if x % 2 == 0 else False

    #Refined Version 2.0
    return x % 2 == 0





main()