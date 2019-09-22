from Tkinter import *
import bankoopmain
bankByClassCreateAccountOb=bankoopmain.createAccount()
bankByClassUserAccountOb=bankoopmain.userAccount()
bankByClassTransactionOb=bankoopmain.transaction()
root = Tk()
root.title("Main Screen")
root.geometry("1366x768")
root.configure(background = "light cyan")
dataOfUser=[]
moneyAfterTran=0
def register():
    screen1 = Toplevel()
    screen1.geometry("1366x768")
    screen1.configure(background = "light cyan")
    v=IntVar()
    
    Label(screen1,text = "" , height = 1, width = 10, fg = "black" , bg = "light cyan").pack()
    l1 = Label(screen1, text="Name",height = 2, width = 20, fg = "black" , bg = "RoyalBlue" , font = ("Arial",12))
    l1.pack()
    Label(screen1,text = "" , height = 1, width = 10, fg = "black" , bg = "light cyan").pack()
    name = Entry(screen1)
    name.pack()
    
    Label(screen1,text = "" , height = 1, width = 10, fg = "black" , bg = "light cyan").pack()
    l2 = Label(screen1, text="Email",height = 2, width = 20, fg = "black" , bg = "RoyalBlue" , font = ("Arial",12))
    l2.pack()
    Label(screen1,text = "" , height = 1, width = 10, fg = "black" , bg = "light cyan").pack()
    email = Entry(screen1)
    email.pack()
    
    Label(screen1,text = "" , height = 1, width = 10, fg = "black" , bg = "light cyan").pack()
    l3 = Label(screen1, text="Password",height = 2, width = 20, fg = "black" , bg = "RoyalBlue" , font = ("Arial",12))
    l3.pack()
    Label(screen1,text = "" , height = 1, width = 10, fg = "black" , bg = "light cyan").pack()
    password = Entry(screen1)
    password.pack()
    Label(screen1,text = "" , height = 1, width = 10, fg = "black" , bg = "light cyan").pack()
    
    r1=Radiobutton(screen1,text="Saving Account",variable=v,value=1,height = 2, width = 20, fg = "black" , bg = "RoyalBlue" , font = ("Arial",12))
    r1.pack(anchor=CENTER)
    Label(screen1,text = "" , height = 1, width = 10, fg = "black" , bg = "light cyan").pack()
    r2=Radiobutton(screen1,text="Current Account",variable=v,value=2,height = 2, width = 20, fg = "black" , bg = "RoyalBlue" , font = ("Arial",12))
    r2.pack(anchor=CENTER)
    Label(screen1,text = "" , height = 1, width = 10, fg = "black" , bg = "light cyan").pack()
    b1 = Button(screen1, text="Submit", command=lambda: connect(name.get(),email.get(),password.get(),v.get()),height = 2, width = 20, fg = "black" , bg = "RoyalBlue" , font = ("Arial",12))
    b1.pack()
    Label(screen1,text = "" , height = 1, width = 10, fg = "black" , bg = "light cyan").pack()
    Button(screen1,text="Exit",height = 2, width = 20, fg = "black" , bg = "RoyalBlue" , font = ("Arial",12),command = screen1.destroy).pack()
    Label(screen1,text = "" , height = 1, width = 10, fg = "black" , bg = "light cyan").pack()
    screen1.mainloop()


def connect(nameInput,emailInput,passInput,type):

    list = [] 
    list = [nameInput, emailInput, passInput, 0, 0, type]
    print list
    bankByClassCreateAccountOb.addAccount(list)


def loginConnect(loginEmailInput,loginPassInput):
    list = []
    print loginEmailInput
    print loginPassInput
    dataOfUser=bankByClassUserAccountOb.getAccount(loginEmailInput)
    print dataOfUser
    if dataOfUser>0:
        if loginEmailInput == dataOfUser[1]:
            if loginPassInput == dataOfUser[2]:
                screen1 = Toplevel()
                screen1.geometry("1366x768")
                screen1.configure(background = "light cyan")
                global l1
               
                
                l2 = Label(screen1, text="Total Amount",height = 2, width = 20, fg = "black" , bg = "RoyalBlue" , font = ("Arial",12))
                l2.pack()
                l1 = Label(screen1, text="Rs. " + str(dataOfUser[3]),height = 2, width = 20, fg = "black" , bg = "RoyalBlue" , font = ("Arial",12))
                Label(screen1,text = "" , height = 1, width = 10, fg = "black" , bg = "light cyan").pack()
                l1.pack()
                Label(screen1,text = "" , height = 1, width = 10, fg = "black" , bg = "light cyan").pack()
                global addAmountEntry, passButton, removeMoney, transactionAccount, transactionMoney
                
                addButton = Button(screen1, text="Add Amount", command=lambda:addMoney(dataOfUser,addAmountEntry.get()),height = 2, width = 20, fg = "black" , bg = "RoyalBlue" , font = ("Arial",12))
                addButton.pack()
                Label(screen1,text = "" , height = 1, width = 10, fg = "black" , bg = "light cyan").pack()
                addAmountEntry = Entry(screen1)
                addAmountEntry.pack()
                Label(screen1,text = "" , height = 1, width = 10, fg = "black" , bg = "light cyan").pack()
                removeMoneyButton = Button(screen1, text="Remove money", command=lambda:removeMoneyFun(dataOfUser,removeMoney.get()),height = 2, width = 20, fg = "black" , bg = "RoyalBlue" , font = ("Arial",12))
                removeMoneyButton.pack()
                Label(screen1,text = "" , height = 1, width = 10, fg = "black" , bg = "light cyan").pack()
                removeMoney = Entry(screen1)
                removeMoney.pack()
                Label(screen1,text = "" , height = 1, width = 10, fg = "black" , bg = "light cyan").pack()
                Label(screen1, text="Transfer to Account",height = 2, width = 30, fg = "black" , bg = "RoyalBlue" , font = ("Arial",12)).pack()
                Label(screen1,text = "" , height = 1, width = 10, fg = "black" , bg = "light cyan").pack()
                transactionAccount = Entry(screen1)
                transactionAccount.pack()
                Label(screen1,text = "" , height = 1, width = 10, fg = "black" , bg = "light cyan").pack()
                transactionAccountButton = Button(screen1, text="Transaction Amount", command=lambda:transaction(dataOfUser,transactionMoney.get()),height = 2, width = 20, fg = "black" , bg = "RoyalBlue" , font = ("Arial",12))
                transactionAccountButton.pack()
                Label(screen1,text = "" , height = 1, width = 10, fg = "black" , bg = "light cyan").pack()
                transactionMoney = Entry(screen1)
                transactionMoney.pack()
                Label(screen1,text = "" , height = 1, width = 10, fg = "black" , bg = "light cyan").pack()
                passButton = Button(screen1, text="Passbook", command=lambda:passbook(dataOfUser),height = 2, width = 20, fg = "black" , bg = "RoyalBlue" , font = ("Arial",12))
                passButton.pack()
                Label(screen1,text = "" , height = 1, width = 10, fg = "black" , bg = "light cyan").pack()
                passButtonPrint = Button(screen1, text="Print Passbook", command=lambda:bankByClassUserAccountOb.printTran(dataOfUser[4]),height = 2, width = 20, fg = "black" , bg = "RoyalBlue" , font = ("Arial",12))
                passButtonPrint.pack()
                screen1.mainloop()
def addMoney(dataOfUser,addAmountEntryTotal): 
    print "****"
    print dataOfUser[4]
    print addAmountEntryTotal
    if int(addAmountEntryTotal) > 0:
        moneyAfterTran=bankByClassUserAccountOb.addMoney(dataOfUser[4],addAmountEntryTotal)
        l1.configure(text="Rs. "+str(moneyAfterTran))

def removeMoneyFun(dataOfUser,removeMoneyTotal): 
    print "1****"
    print "2****"
    print removeMoneyTotal
    if int(removeMoneyTotal) > 0:
        moneyAfterTran=bankByClassUserAccountOb.removeMoney(dataOfUser[4],removeMoneyTotal,"self remove",dataOfUser[4])
        l1.configure(text="Rs. "+str(moneyAfterTran))


def transaction(dataOfUser,transactionMoneyFun): 
    print "****"
    print transactionMoneyFun
    toAccountFun=transactionAccount.get()
    if int(transactionMoneyFun) > 0:
        moneyAfterTran=bankByClassUserAccountOb.removeMoney(dataOfUser[4],transactionMoneyFun,"Transferred Money",toAccountFun)
        l1.configure(text="Rs. "+str(moneyAfterTran))


def passbook(dataOfUser):
    listOfTransaction=bankByClassTransactionOb.getTransaction(dataOfUser[4])
    screen1 = Toplevel()
    screen1.geometry("1366x768")
    Lb1 = Listbox(screen1, width=150)
    count = 1
    for i in listOfTransaction:
        Lb1.insert(count,i)
        count += 1
    Lb1.pack()
    passButtonPrint = Button(screen1, text="Print Passbook", command=lambda:bankByClassUserAccountOb.printTran(dataOfUser[4]))
    passButtonPrint.pack()
    screen1.mainloop()


def login():
    screen1 = Toplevel()
    screen1.geometry("1366x768")
    screen1.configure(background = "light cyan")
    Label(screen1,text = "" , height = 1, width = 10, fg = "black" , bg = "light cyan").pack()
    l2 = Label(screen1, text="email",height = 2, width = 20, fg = "black" , bg = "RoyalBlue" , font = ("Arial",12))
    l2.pack()
    Label(screen1,text = "" , height = 1, width = 10, fg = "black" , bg = "light cyan").pack()
    loginEmail = Entry(screen1)
    loginEmail.pack()
   
    Label(screen1,text = "" , height = 1, width = 10, fg = "black" , bg = "light cyan").pack()
    l3 = Label(screen1, text="password",height = 2, width = 20, fg = "black" , bg = "RoyalBlue" , font = ("Arial",12))
    l3.pack()
    Label(screen1,text = "" , height = 1, width = 10, fg = "black" , bg = "light cyan").pack()
    loginPass = Entry(screen1)
    loginPass.pack()
    Label(screen1,text = "" , height = 1, width = 10, fg = "black" , bg = "light cyan").pack()
    b1 = Button(screen1, text="submit", command=lambda:loginConnect(loginEmail.get(),loginPass.get()),height = 2, width = 20, fg = "black" , bg = "RoyalBlue" , font = ("Arial",12))
    b1.pack()
    Label(screen1,text = "" , height = 1, width = 10, fg = "black" , bg = "light cyan").pack()
    Button(screen1, text="Exit", command=screen1.destroy,height = 2, width = 20, fg = "black" , bg = "RoyalBlue" , font = ("Arial",12)).pack()
    Label(screen1,text = "" , height = 1, width = 10, fg = "black" , bg = "light cyan").pack()

    screen1.mainloop()


Button(root, text="WELCOME  TO IMPERIAL BANK",height = 2, width = 155, fg = "black" , bg = "RoyalBlue" , font = ("Arial",20)).pack()
Label(root,text = "" , height = 1, width = 10, fg = "black" , bg = "light cyan").pack()
Button(root, text="Registor", command=register,height = 2, width = 20, fg = "black" , bg = "RoyalBlue" , font = ("Arial",12)).pack()
Label(root,text = "" , height = 1, width = 10, fg = "black" , bg = "light cyan").pack()
Button(root, text="Login", command=login,height = 2, width = 20, fg = "black" , bg = "RoyalBlue" , font = ("Arial",12)).pack()
Label(root,text = "" , height = 1, width = 10, fg = "black" , bg = "light cyan").pack()
Button(root, text="Exit", command=root.destroy,height = 2, width = 20, fg = "black" , bg = "RoyalBlue" , font = ("Arial",12)).pack()
Label(root,text = "" , height = 1, width = 10, fg = "black" , bg = "light cyan").pack()
root.mainloop()
