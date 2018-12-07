#import os and csv modules
import os
import csv

#pull in csv file
pullcsvfile = os.path.join("election_data.csv")

# Open and read csv
with open(pullcsvfile, newline="") as csvfile:

    #create csv reader
    readthecsvfile = csv.reader(csvfile, delimiter=",")
    
    # Read the header row first (skip this part if there is no header)
    topheader = next(csvfile)
    print(f"Election Results")
    print("----------------------------")
    #{topheader}")
    # Read through each row of data after the header

    totalvotes = 0
    candidates = []
    listvotes = {}
    votes = 0
    rows_d = {}
    tally = []
    khanvotes = 0
    correyvotes = 0
    livotes = 0
    tooleyvotes = 0

    for row in readthecsvfile:

        #find total amount of votes
        totalvotes += 1

        #if new name then add to list
        if str(row[2]) not in candidates:
            listvotes[votes] = str(row[2])
            candidates.append(str(row[2]))
            
        if str(row[2]) == "Khan":
            khanvotes += 1
        
        if str(row[2]) == "Correy":
            correyvotes += 1

        if str(row[2]) == "Li":
            livotes += 1

        if str(row[2]) == "O'Tooley":
            tooleyvotes += 1


    #count votes for each candidate
    tally.append(khanvotes)
    tally.append(correyvotes)
    tally.append(livotes)
    tally.append(tooleyvotes)

    #print(f"Total Votes: {totalvotes}")
    #print(f"{candidates}")

    #find percentage votes for each candidate and round
    khanperc = round((tally[0] / totalvotes) * 100, 2)
    correyperc = round((tally[1] / totalvotes) * 100, 2)
    liperc = round((tally[2] / totalvotes) * 100, 2)
    tooleyperc = round((tally[3] / totalvotes) * 100, 2)
    
    #find winner
    if tally[0] > tally[1] and tally[0] > tally[2] and tally[0] > tally[3]:
        winner = candidates[0]
    elif tally[1] > tally[0] and tally[1] > tally[2] and tally[1] > tally[3]:
        winner = candidates[1]
    elif tally[2] > tally[0] and tally[2] > tally[1] and tally[2] > tally[3]:
        winner = candidates[2]
    else:
        winner = candidates[3]

    #print results

print(f"Total Votes: {totalvotes}")
print("------------------------------")
print(str(candidates[0]) + ": " + str(khanperc) + "% " + "(" + str(tally[0]) + ")")
print(str(candidates[1]) + ": " + str(correyperc) + "% " + "(" + str(tally[1]) + ")")
print(str(candidates[2]) + ": " + str(liperc) + "% " + "(" + str(tally[2]) + ")")
print(str(candidates[3]) + ": " + str(tooleyperc) + "% " + "(" + str(tally[3]) + ")")
print("------------------------------")
print("Winner: " + str(winner))
print("------------------------------")

with open("electtionresults.txt", "w") as electionresults:
    print(f"Total Votes: {totalvotes}", file=electionresults)
    print("------------------------------", file=electionresults)
    print(str(candidates[0]) + ": " + str(khanperc) + "% " + "(" + str(tally[0]) + ")", file=electionresults)
    print(str(candidates[1]) + ": " + str(correyperc) + "% " + "(" + str(tally[1]) + ")", file=electionresults)
    print(str(candidates[2]) + ": " + str(liperc) + "% " + "(" + str(tally[2]) + ")", file=electionresults)
    print(str(candidates[3]) + ": " + str(tooleyperc) + "% " + "(" + str(tally[3]) + ")", file=electionresults)
    print("------------------------------", file=electionresults)
    print("Winner: " + str(winner), file=electionresults)
    print("------------------------------", file=electionresults)