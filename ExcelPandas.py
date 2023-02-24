import pandas as pd
from openpyxl import load_workbook

def CreateExcelFile(Name):
    writer = pd.ExcelWriter(F'{Name}.xlsx', engine='xlsxwriter')
    writer.save()


CreateExcelFile("Abhi")
