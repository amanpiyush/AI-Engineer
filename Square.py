def main():
    Num = int(input("Enter the Number : \n"))
    print(f"Square : {square(Num)}")
    print(f"squareroot : {round(squareroot(Num))}")


def square(x):
    return pow(x, 5)

def squareroot(x):
    return x ** 0.5
    

main()