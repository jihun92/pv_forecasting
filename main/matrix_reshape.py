import pandas as pd
import numpy as np

# valiable
readExcelFile = 'C:\\Users\\jihun\\Desktop\\PV Forecasting\\test.xlsx'
writeExcelFile = 'C:\\Users\\jihun\\Desktop\\PV Forecasting\\write.xlsx'

xlsx = pd.read_excel(readExcelFile)
arr = xlsx.to_numpy()
arr = np.asmatrix(arr)
arr = arr.flatten('F')

for i in range(0, arr.size):
    print(arr[0][0])

xlsx = pd.DataFrame(data=arr)
xlsx.to_excel(writeExcelFile)
