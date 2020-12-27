person=[]
firstName=input("Write your name: ")
lastName=input("Write your lastname: ")
age=int(input("Write your age: "))
birthyear=input("Write your birth year: ")
person.append(f"Firstname: {firstName}")
person.append(f"Lastname: {lastName}")
person.append(f"Age: {age}")
person.append(f"Birthyear: {birthyear}")

for i in person:
    print(i)
if age<18:
    print("You can't go out because it is too dangerous.")
else:
    print("You can go out to the street.")