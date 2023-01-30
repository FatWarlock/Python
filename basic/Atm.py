print("""\t******** Welcome Xbank ********
\t\t Please Enter Your Card """)

Veritabanı = {
    "Fatih Hesap": {
        "Name": "Fatih",
        "SurName": "Yıldırım",
        "CardPassword": "1111",
        "AccountBalance": 25000,
        "CreditCardDebt": 10000,
        "CreditCardDebtDate": "11/01/2023"},
    "Ahmet Hesap": {
        "Name": "Ahmet",
        "SurName": "Yıldır",
        "CardPassword": "2222",
        "AccountBalance": 20000,
        "CreditCardDebt": 6000,
        "CreditCardDebtDate": "18/06/2023"},
}

currentlyUsedCard = dict(Veritabanı["Fatih Hesap"])

Chance = 2
for i in range(0, 3):
    passWord = input("Please enter 4 digit Card Password: ")
    if passWord == currentlyUsedCard.get("CardPassword"):
        print("""Welcome back {} {}
        Please choose a operation..."""
              .format(currentlyUsedCard.get("Name"), currentlyUsedCard.get("SurName")))
        Choose = input("""
        [1] Balance Check
        [2] Credit Card Debt Check
        [3] Money Withdraw
        [4] Money Deposit
        [Q] Card Return\n""")
        break
    elif passWord != currentlyUsedCard.get("CardPassword") and Chance != 0:
        print("Wrong Password, you can try {} more time".format(Chance))
        Chance -= 1
    elif passWord != currentlyUsedCard.get("CardPassword") and Chance == 0:
        print("You enter wromg Password 3 time. Your Card Blocked, Please call customer service.")
        exit()

if Choose == "1":
    print("""Account Balance {} $""".format(
        currentlyUsedCard.get("AccountBalance")))
elif Choose == "2":
    print("""Credit Card Debt {} $ \n And Last Pay Day {} """
          .format(currentlyUsedCard.get("CreditCardDebt"),
                  currentlyUsedCard.get("CreditCardDebtDate")))
elif Choose == "3":
    amount1 = int(
        input("Please Enter the amount of money you wish to withdraw from Account: "))
    if currentlyUsedCard.get("AccountBalance") < amount1:
        print("Insufficient Balance")
    else:
        print("Please check the money when you withdraw")
        newAmount1 = currentlyUsedCard.get("AccountBalance") - amount1
        print("Account Balance updated to {} $".format(newAmount1))
elif Choose == "4":
    amount2 = int(
        input("Please Enter the amount of money you wish to deposit into Account: "))
    print("Amount of money deposited to Account. ")
    newAmount2 = currentlyUsedCard.get("AccountBalance") + amount2
    print("Acount balance updated to {} $ ".format(newAmount2))
elif Choose == "Q" or Choose == "q":
    print("Dont forgot the card, have a nice day...")
    exit()
else:
    print("Please choose a valid operation...")
