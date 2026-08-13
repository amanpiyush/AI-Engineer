# i = 0
# while i < 3:
#     print("Meow")
#     i += 1

# for i in [0,1,2]: #It is a poor design

# for i in range(5):
#     print("Meow")

# while True:  #infinity
#     n = int(input("What is n : \n"))
#     if n > 0:
#         break

# for _ in range(n):
#     print("Meow")

def main():
    number = get_number()
    meow(number)


def get_number():
    while True:
        n = int(input("Enter the N : \n"))
        if n > 0:
            break
    return n


def meow(n):
    for _ in range(n):
        print("Meow")


main()