class Customer:
    def __init__(self,Name,SurName,CardPassword,AccountBalance,CreditCardDebt,PayDay):
        self.Name = Name
        self.SurName = SurName
        self.CardPassword = CardPassword 
        self.AccountBalance = AccountBalance
        self.CreditCardDebt = CreditCardDebt
        self.PayDay = PayDay
        

FatihHesap=Customer("Faith","Yıldırım","1111",25000,8000,"11/01/2023")
MehmetHesap= Customer("Mehmet","Yılın","2234",15000,4000,"19/06/2023")
CurrentlyUsedCard=FatihHesap

class ATM:
    def __init__(self,atmName):
        self.atmName = atmName
        self.loginCheck()
        self.loop=True

    def loginCheck(self):
        Chance=2
        for i in range(0,3):
            Password=  input("Please enter your 4 digit password: ")
            if Password == CurrentlyUsedCard.CardPassword:
                self.program()
            elif Password != CurrentlyUsedCard.CardPassword and Chance != 0:
                print("Wrong password. You have {} more chance".format(Chance))
                Chance -= 1
            elif Password != CurrentlyUsedCard.CardPassword and Chance== 0:
                print("""You enter wromg Password 3 time. Your Card Blocked.
                Please call customer service.""")
                exit()
    def program(self):
        select=self.menu()
        if select ==1:
            self.balance()
        if select ==2:
            self.creditCardDebt()
        if select ==3:
            self.withdraw()
        if select ==4:
            self.deposit()
        if select ==5:
            self.quit()    
    def menu(self):
        select=int(input("*** Welcome to the {}, {} {}.\n\n Please select a opreation as you wish...\n\n[1] Balance Check \n[2] Credit Card Debt Check \n[3] Withdraw Money \n[4] Deposit Money \n[5] Card Return\n\nSelect:".format(self.atmName,CurrentlyUsedCard.Name,CurrentlyUsedCard.SurName))) 
        while select< 1 or select >5:
            print("\n\n Please Select a valid operation... \nReturning main menu...")
            self.program() 
        return select
    def balance(self):
        print("Account Balance: {} $".format(CurrentlyUsedCard.AccountBalance))
        self.loop=False
        self.returnMenu()
        
    def withdraw(self):
        amount = int(input("Please enter amount you wish to withdraw: "))
        newAmount = CurrentlyUsedCard.AccountBalance-amount
        if amount > CurrentlyUsedCard.AccountBalance:
            print("Insufficient Balance")
            self.returnMenu()
        else:
            print("Please check amount, Account Balance updated to {} $".format(newAmount))
            self.returnMenu()
    def deposit(self):
        amount2= int(input("Please enter amount you wish to deposit: "))
        newAmount2 = CurrentlyUsedCard.AccountBalance+amount2
        print("Deposit operation succesfully finished, Account Balance updated to {} $".format(newAmount2))
        self.returnMenu()
            
    def creditCardDebt(self):
        print("credit Card Debt: {}$ and last Pay Day {}".format(CurrentlyUsedCard.CreditCardDebt,CurrentlyUsedCard.PayDay))
        self.loop=False
        self.returnMenu()
    def quit(self):
        print("Thanks for choosing our bank, have a nice day!... ")
        self.loop = False
        exit()
    def returnMenu(self):
        x = int(input("""For Main Menu press 7.\nFor return to card press 5: """))
        if x ==7:
            self.program()
        elif x==5:
            self.quit()
        else:
            print("Select valid operation...")
        
print("""\t******** Welcome Xbank ********\t
\t     Please Enter Your Card """)
Bank=ATM("XBank")
while Bank.loop:
    Bank.program()
