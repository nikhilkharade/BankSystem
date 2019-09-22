import mysql.connector as con
import datetime
import csv
db = con.connect(host="localhost",user="root",password="root",database="mydb")
cursor=db.cursor()
class transaction:
    def createTransaction(self,id,money,type,totalMoney,toAccount):
        list=[0,id,toAccount,type,money,totalMoney]
        print list
        queryAfterLoginTransaction = "insert into bankooptransaction(id,fromAccount,toAccount,type,Amount,balance,dateOfTran) values(%s,%s,%s,%s,%s,%s,%s)"
        date = datetime.datetime.now()
        date = date.strftime("%dth,%y")
        list.append(date)
        cursor.execute(queryAfterLoginTransaction, list)
        db.commit()
        
    def getTransaction(self,id):
        query = "select * from bankooptransaction where fromAccount="+str(id)
        cursor.execute(query)
        dataOfUser = cursor.fetchall()
        listOfTransaction=[]
        for i in dataOfUser:
            dataOfTransactionAfterGetTran="from account: " + str(i[1]) + " to account: " + str(i[2]) + " type of transaction: " + str(i[3]) + " balance: " + str(i[4]) + " date: " + str(i[6])
            listOfTransaction.append(dataOfTransactionAfterGetTran)
        return listOfTransaction
    def printTransaction(self,id,name):
        query = "select * from bankooptransaction where fromAccount="+str(id)
        cursor.execute(query)
        dataOfUser = cursor.fetchall()
        print dataOfUser
        with open(str(name)+"_"+str(id)+".csv","w") as csv_file:
            fieldNames=["id","fromAccount","toAccount","type of transaction","amount","balance","date"]
            csv_writer=csv.DictWriter(csv_file,fieldnames=fieldNames,delimiter=",")
            csv_writer.writeheader()
            for i in dataOfUser:
                            csv_writer.writerow({"id":i[0],"fromAccount":i[1],"toAccount":i[2],"type of transaction":i[3],"amount":i[4],"balance":i[5],"date":i[6].replace(",","  ")})


class addTypeOfSA:
    def add(self,list):
        list[5]="Saving Account"
        list[3]=5000
        return list
class addTypeOfCA:
    def add(self,list):
        list[5]="Current Account"
        return list
class createAccount(addTypeOfSA,addTypeOfCA):
    def addAccount(self,list):
        sa=addTypeOfSA()
        ca=addTypeOfCA()
        if(list[5]==1):
            list=sa.add(list)
        if(list[5]==2):
            list=ca.add(list)
        query="insert into bankoopclass(name,email,password,balance,id,typeOfAccount) values(%s,%s,%s,%s,%s,%s)"
        cursor.execute(query, list)
        db.commit()

class userAccount(transaction):
    def getAccount(self,email):
        query = "select * from bankoopclass where email='" + str(email) + "'"
        cursor.execute(query)
        dataOfUser=[]
        for i in cursor:
            dataOfUser=i
        return dataOfUser
        
    def addMoney(self,id,money):
        transactionOb=transaction()
        query = "select * from bankoopclass where id='" + str(id) + "'"
        cursor.execute(query)
        for i in cursor:
            moneyToAdd=money
            money=int(i[3])+int(money)
        queryAfterLogin = "update bankoopclass set balance='" + str(money) + "' where id=" + str(id)
        cursor.execute(queryAfterLogin)
        db.commit()
        transactionOb.createTransaction(id,moneyToAdd,"Self Add",money,id)
        return money
    def removeMoney(self,id,money,type,toAccount):
        transactionOb=transaction()
        query = "select * from bankoopclass where id='" + str(id) + "'"
        cursor.execute(query)
        for i in cursor:
            totalMoney=int(i[3])
        if totalMoney>=int(money):
            totalMoney-=int(money)
            queryAfterLogin = "update bankoopclass set balance='" + str(totalMoney) + "' where id=" + str(id)
            cursor.execute(queryAfterLogin)
            transactionOb.createTransaction(id,money,type,totalMoney,toAccount)
            db.commit()
    def printTran(self,id):
        transactionOb=transaction()
        query = "select * from bankooptransaction where id='" + str(id) + "'"
        cursor.execute(query)
        for i in cursor:
            nameOfUser=i[0]
        transactionOb.printTransaction(id,nameOfUser)
        
   
