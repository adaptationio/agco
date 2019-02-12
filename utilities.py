
import csv
import numpy as np
import matplotlib.pyplot as plt


class Transforms():
    def __init__(self):
        love = "Ramona"

    def csv_to_list(self, path, delim=';'):
        data_path = path
        with open(data_path, 'r') as f:
            reader = csv.reader(f, delimiter=delim)
        # get header from first row
            headers = next(reader)
        # get all the rows as a list
            data = list(reader)
        # transform data into numpy array
        #data = np.array(data).astype(float)
    
        print(headers)
        #print(data.shape)
        print(data[0])
        return headers, data

    def tocsv(self, x, path):
        with open(path, "a", newline='') as fp:
            wr = csv.writer(fp, dialect='excel')
            for i in range(len(x)):
                wr.writerow(x[i])

    def merge_data(self, data1, data2, index):
        new_data = []
        #new_data.append(['id', 'serial', 'selling', 'serviceInterval', 'commission', 'lastService', 'nextService', 'service', 'status', 'type', 'createdAt', 'updatedAt', 'OrganisationId', 'User', 'address', 'city', 'state', 'postcode', 'CouncilId'])
        #new_data.append(['id', 'name', 'firstName', 'lastName', 'email', 'mobile', 'createdAt', 'updatedAt'])
        new_data.append(['id', 'serial', 'selling', 'serviceInterval', 'commission', 'lastService', 'nextService', 'service', 'status', 'type', 'createdAt', 'updatedAt', 'OrganisationId', 'User'])
        for i in range(len(data1)):
            ident = data1[i][13]
            for k in range(len(data2)):
                if ident == data2[k][index]:
                    #new_data.append([data1[i][0], data1[i][1], data1[i][13], data2[k][2]])
                    new_data.append([data1[i][0], data1[i][1], data1[i][2], data1[i][3], data1[i][4], data1[i][5], data1[i][6], data1[i][7], data1[i][8], data1[i][9], data1[i][10], data1[i][11], data1[i][12], data2[k][1]] )
        
        return new_data

                

                

        


test = Transforms()
headers, data0 = test.csv_to_list('dataold/SystemOwners.csv')
headers, data1 = test.csv_to_list('dataold/Systems.csv')
headers, data2 = test.csv_to_list('dataold/Locations.csv')
headers, data3 = test.csv_to_list('dataold/Users.csv')
headers, data4 = test.csv_to_list('dataold/Systems_withuser.csv', ',')
headers, data5 = test.csv_to_list('dataold/Systems_with_address.csv',',')
headers, data6 = test.csv_to_list('data/CURRENT CUSTOMER LIST NAMES MATCHED TO XERO.csv', ',')
print(len(data5[0]))
print(len(data1[0]))


#test.tocsv(data, 'dataold/test.csv')

new_data = test.merge_data(data1, data6, 0)
test.tocsv(new_data, 'dataold/Systems_with_user_address_current_2.csv')
#print(new_data)