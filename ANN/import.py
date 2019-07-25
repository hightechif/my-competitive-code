import numpy as np
import pandas as pd

# Data Location
rawdata = r'D:\code\ANN\rawdata_edited.xlsx'

# Training Set Data
training_set = pd.read_excel(rawdata, sheetname=1)
training_set_inputs = np.array(training_set[['Suhu', 'Kelembapan']])
training_set_outputs = np.array(training_set[['Label']])

# Testing Set Data
testing_set = pd.read_excel(rawdata, sheetname=2)
testing_set_inputs = np.array(testing_set[['Suhu','Kelembapan']])   
testing_set_outputs = np.array(testing_set[['Label']])

print(testing_set_inputs)
print(testing_set_outputs)
