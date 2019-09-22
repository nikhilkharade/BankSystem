import csv
selfadd=0
selfremove=0
transfermoney=0
nameOfFile=raw_input("Enter the name of user")
idOfFile=raw_input("Enter the id of user")
fileName=str(nameOfFile)+"_"+str(idOfFile)+".csv"
#print fileName
with open(fileName,"r") as csv_file:
    csv_reader=csv.reader(csv_file,delimiter=",")
    next(csv_reader)
    for line in csv_reader:
        if(line[3]=="Self Add"):
            selfadd+=1
        elif(line[3]=="Self Remove"):
            selfremove+=1
        elif(line[3]=="Transfer Money"):
            transfermoney+=1
print str(selfadd)+"\t"+str(selfremove)+"\t"+str(transfermoney)
