# students = {
#     "Hermione"  : "Gryffindor",
#     "Harry"     : "Gryffindor",
#     "Ron"       : "Gryffindor",
#     "Draco"     :  "Slytherin"
# }

# for student in students:
#     print(student," : ",students[student])   



students = [
    {
        "Name"  :"Hermione",
        "House" : "Gryffindor",
        "Patrous" : "Otter"
    },
    {
        "Name"  :"Harry",
        "House" : "Gryffindor",
        "Patrous" : "Stag"
    },
    {
        "Name"  :"Ron",
        "House" : "Gryffindor",
        "Patrous" : "Jack Russell Terrier"
    },
    {
        "Name"  :"Dacro",
        "House" : "Slytherin",
        "Patrous" : None
    }

]

for student in students:
    print(student["Name"],"  :", student["Patrous"])