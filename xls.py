
import xlsxwriter

workbook = xlsxwriter.Workbook('RockPaperScissors.xlsx')#File Create
worksheet = workbook.add_worksheet('GameLog')#Sheet Created & Named
#Updating titles
worksheet.write('A2', 'SrNo')
worksheet.write('B2', 'TimeSlot')
worksheet.write('C2', 'Player')
worksheet.write('D2', 'Input')
worksheet.write('E2','Result')
workbook.close()



def greeting():
    name=input("Enter Your Name: ")
    print(f"Welcome {name}")


def getXlData():
    for i in range(3,5):
        worksheet.write(f'A{i}','{i}')













