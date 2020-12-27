#IDENTITY
name= "OKTAY"
surname= "POLAT"

#IDENTITY VALIDATION
check = False
for i in range(3):
    loginName = (input("Write your name: "))
    loginName=loginName.upper()
    loginSurname = input("Write your surname: ")
    loginSurname=loginSurname.upper()
    if loginName==name and loginSurname==surname:
        print(f"Welcome {name} {surname}")
        check=True
        break
    elif loginName!=name or loginSurname!=surname:
        print("Please try again later!")
    else:
        print("Invalid access request!")
if not check:
    print("Sorry, you can not access\nClosing...")
    quit()

#TAKING LESSONS
lessons=[]
count=0
for i in range(0,5):
    lesson=input("Write the lesson you want: ")
    lessons.append(lesson)
    count+=1
    print("Do you want to add another? Yes/No")
    answer=input()
    if answer=="No" or answer=="no":
        if count>=3:
            print("Your lessons are ready.")
            break
        else:
            print("You failed in class!\nClosing...")
            quit()
    elif answer=="Yes" or "yes":
        print("Your lesson is added.")

#TAKING EXAMS
lessonExam=input("Which lesson's exams do you want to take?\nLesson: ")
lessongrades= [50,60,70]
exams={"midterm":0,"final":0,"project":0}
y=0
for i in exams:
    exams[i]=lessongrades[y]
    y+=1

#IF WE WANT USER INPUT:
# exams["midterm"]=int(input("Write your midterm point: "))
# exams["final"]=int(input("Write your final point: "))
# exams["project"]=int(input("Write your project point: "))

grade=(exams["midterm"]*30/100)+(exams["final"]*50/100)+(exams["project"]*20/100)

#GRADE CHARACTER
if 90<=grade<=100:
    print("Your grade is AA")
elif 70<=grade<90:
    print("Your grade is BB")
elif 50<=grade<70:
    print("Grade: ",grade)
    print("Your grade is CC")
elif 30<=grade<50:
    print("Your grade is DD")
elif grade<30:
    print("Your grade is FF\nYou should take the exam again!")
else:
    print("Invalid score!")