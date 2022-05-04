import csv 
import plotly
import math


with open("D:\project\class105\data.csv") as f:
    csv_reader=csv.reader(f)
    data=list(csv_reader)

data.pop(0)

no=[]
for i in data:
    no.append(int(i[1]))
sum=0
for i in no :  
  sum=sum+i
n=len(no)  
mean=sum/n
print(mean)

diff_list=[]
for i in no:
    diff_list.append(i-mean)
sq_list=[]
for i in diff_list:
    sq_list.append(i**2)   
sum=0
for i in sq_list:
    sum=sum+i
temp=sum/n 
sd=math.sqrt(temp)
print(sd)