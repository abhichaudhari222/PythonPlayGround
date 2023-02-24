import random
def greeting():
    name=input("Enter Your Name: ")
    print(f"Welcome {name}")
def winLose():
        if userInput == 1 and cpu == 2:
            print("You Loose")
        elif userInput == 2 and cpu == 3:
            print("You Loose")
        elif userInput == 3 and cpu == 1:
            print("You Loose")
        elif cpu == userInput:
            print("its Tie")
        else :
            print("You Win")
def cpuDisplay():
        if (cpu == 1) :
            print("CPU Selected Rock")
        if (cpu == 2) :
            print("CPU Selected Paper")
        if (cpu == 3) :
            print("CPU Selected Scissors")
def userDisplay():
        if (userInput == 1) :
            print("You Selected Rock")
        if (userInput == 2) :
            print("You Selected Paper")
        if (userInput == 3) :
            print("You Selected Scissors")
cpu=random.randint(1,3)
greeting()
print("1 for Rock.\n2 for Paper.\n3 for Scissors.")
print("==========================================")
userInput=int(input("Enter Your Choice : "))
userDisplay()
cpuDisplay()
winLose()