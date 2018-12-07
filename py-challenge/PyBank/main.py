#import os and csv modules
import os
import csv

#pull in csv file
pullcsvfile = os.path.join("pythonhomework1.csv")

# Open and read csv
with open(pullcsvfile, newline="") as csvfile:

    #create csv reader
    readthecsvfile = csv.reader(csvfile, delimiter=",")
    
    # Read the header row first (skip this part if there is no header)
    topheader = next(csvfile)
    print(f"Financial Analysis")
    print("----------------------------")
    #{topheader}")

    # Read through each row of data after the header
    countmonths = 0
    totalprofit = 0
    averagechangelist = []
    averagechange = 0
    averagechangetotal = 0
    maxprofit = 0
    minprofit = 0
    decmaxprofit = 0
    decminprofit = 0
    firstlist = []
    secondlist = []
    firstmonth = []

    for row in readthecsvfile:

        countmonths += 1

        totalprofit += int(row[1])

        averagechangelist.append(float(row[1]))
        
        #greatest increase
        if int(row[1]) < minprofit:
            minprofit = int(row[1])

        if int(row[1]) > maxprofit:
            
            maxprofit = int(row[1]) - (minprofit)
            monthrow = str(row[0])

        #greatest decrease
        firstlist.append(int(row[1]))
        firstmonth.append(row[0])


        if countmonths > 2:
            
            secondlist.append((firstlist[-1] - firstlist[-2]))

            averagechange += (averagechangelist[-1] - averagechangelist[-2])

        if countmonths > 3:

            if (secondlist[-2] < secondlist[-1]):

                del secondlist[-1]
                del firstmonth[-1]
                
                decminprofit = secondlist[-1]
                monthrow2 = firstmonth[-1]
    

    averagechangetotal = (averagechangelist[-1] - averagechangelist[0]) / (countmonths -1)

    averagechangetotal = round(averagechangetotal, 2)

    print(f"Total Months: {countmonths}")
    print(f"Total: ${totalprofit}")
    print(f"Average Change: ${averagechangetotal}")
    print(f"Greatest Increase in Profits: {monthrow} (${maxprofit})")
    print(f"Greatest Decrease in Profits: {monthrow2} (${decminprofit})")

    with open("winnerfile.txt", "w") as winnerfile:
        print(f"Total Months: {countmonths}", file=winnerfile)
        print(f"Total: ${totalprofit}", file=winnerfile)
        print(f"Average Change: ${averagechangetotal}", file=winnerfile)
        print(f"Greatest Increase in Profits: {monthrow} (${maxprofit})", file=winnerfile)
        print(f"Greatest Decrease in Profits: {monthrow2} (${decminprofit})", file=winnerfile)