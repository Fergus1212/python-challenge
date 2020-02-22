import os
import csv
csvpath = ('election_data.csv')
countv = 0
with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    header =next(csvreader)
    rows =[[row[0], row[1], row[2]] for row in csvreader]
for row in rows:
    countv = countv+1

canidates = []
Khan = 0
Correy = 0
Li = 0
otools = 0

for row in rows:
    if row[2] not in canidates:
        canidates.append(row[2])
    if row[2] == "Khan":
        Khan += 1
    if row[2] == "Correy":
        Correy += 1
    if row[2] == "Li":
        Li += 1
    if row[2] == "O'Tooley":
        otools += 1

KhanP = (Khan/countv)*100
CorreyP = (Correy/countv)*100
LiP = (Li/countv)*100
otoolsP = (otools/countv)*100

#print(round(KhanP,4))
winner = max(Khan,Correy, Li, otools)
if winner == Khan:
    winnervariable = "Khan"
if winner == Correy: 
    winnervariable = "Correy"
if winner == Li:
    winnervariable = "Li"
if winner == otools: 
    winnervariable = "O'Tooley"  

print(f"Election Results")
print("-------------------------")
print(f"Khan: {round(KhanP)}% ({Khan})")
print(f"Correy: {round(CorreyP)}% ({Correy})")
print(f"Li: {round(LiP)}% ({Li})")
print(f"O'Tooley: {round(otoolsP)}% ({otools})")
print("-------------------------")
print(f"Winner: {winnervariable}")
print("-------------------------")
electionresults = open("Election_Results.txt","w")
electionresults.write(f"Election Results \n ----------------------------- \n Khan: {round(KhanP)}% ({Khan}) \n Correy: {round(CorreyP)}% ({Correy})\n Li: {round(LiP)}% ({Li}) \n O'Tooley: {round(otoolsP)}% ({otools}) \n ----------------------------- \n Winner: {winnervariable}-----------------------------")