import csv
import statistics as st 

with open('data.csv', newline='') as f:
    reader = csv.reader(f)
    fileData = list(reader)

fileData.pop(0)
Data = []

for i in range(len(fileData)):
    n_num = fileData[i][2]
    Data.append(float(n_num))


m = len(Data)
Data.sort()


#mean
sum = sum(Data)
mean = sum/len(Data)
print(mean)

#median
if m % 2 == 0:
    median1 = float(Data[m//2])
    median2 = float(Data[m - 1])
    median = (median1 + median2) / 2

else:
    median = Data[m//2]

print(median)


#mode 

mode = st.mode(Data)
print(mode)
