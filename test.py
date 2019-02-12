
import csv
import numpy as np
import matplotlib.pyplot as plt



data_path = 'dataold/Systems.csv'
with open(data_path, 'r') as f:
    reader = csv.reader(f, delimiter=';')
    # get header from first row
    headers = next(reader)
    # get all the rows as a list
    data = list(reader)
    # transform data into numpy array
    #data = np.array(data).astype(float)
    
print(headers)
#print(data.shape)
print(data[0])