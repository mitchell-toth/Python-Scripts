import pandas as pd

excelFilePath = "pythonExcelTesting.xlsx"
excelFile = pd.read_excel(excelFilePath)
print(excelFile['ID'])
print(excelFile['Employee'])

