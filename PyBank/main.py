import os
import csv

csvpath = os.path.join('budget_data.csv')

countv=0
plsum = 0
row = [1]
pl=[]
with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    header =next(csvreader)
    rows =[[row[0], int(row[1])] for row in csvreader]
for row in rows:
        date= row[0]
        pl.append(row[1])
    #data = list(int(rows[1]))
    #datam = max(data)
    #print(datam)
for row in rows:
    countv = countv+1
    plsum += int(row[1])
for row in rows:
    avgpl = plsum/len(row[0])
    if row[1] == max(pl):
        q4 = f"{row[0]} {row[1]}"
    if row[1] == min(pl):
        q5 = f"{row[0]} {row[1]}"
        #if row[1]> row[1]-1
        #maxp = row[1]
print("Financial Analysis")
print("-----------------------------")
print(f"total months:  {countv}")
print(f"total:  {plsum}")
print(f"Average Change:  {avgpl}")
print(f"Greatest Increase in Profits:   {q4}")
print(f"Greatest Decrease in Profits:  {q5}")
Financial_Analysis = open("Financial_Analysis.txt","w")
Financial_Analysis.write(f"Financial Analysis\n ----------------------------- \n total months:  {countv} \n total:  {plsum} \n Average Change:  {avgpl} \n Greatest Increase in Profits:   {q4} \n Greatest Decrease in Profits:  {q5} ")


    #print(type((row[1])))