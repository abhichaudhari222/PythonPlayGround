import random
import time
from openpyxl.workbook import Workbook
from openpyxl import load_workbook
from datetime import date

 
def TimeDate():
    global DateNow,TimeNow
    TimeNow = time.strftime("%H:%M:%S", time.localtime())
    DateNow = date.today()

def greeting():
    global name
    name=input("Enter Your Name: ")
    print(f"Welcome {name}")
    print("1 for Rock.\n2 for Paper.\n3 for Scissors.")
    print("==========================================")


def winLose():
    global Result
    if userInput == 1 and cpu == 2:
        Result="Loose"
        print("You Loose")
    elif userInput == 2 and cpu == 3:
        Result="Loose"
        print("You Loose")
    elif userInput == 3 and cpu == 1:
        Result="Loose"
        print("You Loose")
    elif cpu == userInput:
        Result="Tie"
        print("its Tie")
    else :
        Result="Win"
        print("You Win")

def cpuDisplay():
        global cpuInput
        if (cpu == 1) :
            cpuInput="Rock"
            print("CPU Selected Rock")
        if (cpu == 2) :
            cpuInput="Paper"
            print("CPU Selected Paper")
        if (cpu == 3) :
            cpuInput="Scissors"
            print("CPU Selected Scissors")
def userDisplay():
        global userInput,selected
        if (userInput == 1) :
            selected="Rock"
            print("You Selected Rock")
        if (userInput == 2) :
            selected="Paper"
            print("You Selected Paper")
        if (userInput == 3) :
            selected="Scissors"
            print("You Selected Scissors")

def AppendData():
    workbook_name = 'GameExcel.xlsx'
    wb = load_workbook(workbook_name)
    page = wb.active
    new_RockPaperScissors = [[name,selected,cpuInput,Result,DateNow,TimeNow]]
    for info in new_RockPaperScissors:
        page.append(info)
    wb.save(filename=workbook_name)


TimeDate()
cpu=random.randint(1,3)
greeting()
userInput=int(input("Enter Your Choice : "))
userDisplay()
cpuDisplay()
winLose()
AppendData()
