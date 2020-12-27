def welcome(name):
    print("Welcome",name)
    print(f"Here, you will guess my word\nAre you ready {name}? Yes/No")

user=input("What is your name?\n")
welcome(user)
word="globalai"
turn=0
check=False
answer=input()
if answer=="Yes" or answer=="yes":
    while turn<6:
        print("Please write your guess: ")
        guess=input("Your guess: ")
        turn+=1
        if turn==5:
            print("Sorry for you looser! :(\nIt was:",word)
            break
        if guess==word:
            print("Congratulations!\nWrite exit to close")
            check = True
            close=input()
            if close=="exit":
                quit()
        elif guess!=word:
            print("Try again! You can do it!")