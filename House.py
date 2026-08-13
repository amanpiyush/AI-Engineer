House = str(input("Enter the Name : \n"))

match House:
    case "Harry" |  "Hermione" | "Ron":
        print("Gryffindor")

    case "Draco":
        print("Slytherin")

    case _:
        print("Who?")