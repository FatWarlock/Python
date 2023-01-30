print(""" Hesap Makinesi / Calculator

[1] Toplama / Sum
[2] Çıkarma / Extraction
[3] Çarpma / Multiplication
[4] Bölme / Divide
[5] Üs Alma / Exponentiation
[Q] Çıkış
""")

operation = input("Pls choose operation: ")

if (operation == "q" or operation == "Q"):
    print("Quitting...")
elif (operation == "1"):
    number1 = float(input("Pls write number1: "))
    number2 = float(input("Pls write number2: "))
    print("Sum operation result: {}".format(number1+number2))
elif (operation == "2"):
    number1 = float(input("Pls write number1: "))
    number2 = float(input("Pls write number2: "))
    print("Extraction operation result: {}".format(number1-number2))
elif (operation == "3"):
    number1 = float(input("Pls write number1: "))
    number2 = float(input("Pls write number2: "))
    print("Multiplication operation result: {}".format(number1*number2))
elif (operation == "4"):
    number1 = float(input("Pls write number1: "))
    number2 = float(input("Pls write number2: "))
    print("Divide operation result: {}".format(number1/number2))
elif (operation == "5"):
    number = float(input("Pls write number: "))
    exponent = float(input("Pls write exponent: "))
    print("Exponent operation result: {}".format(number**exponent))
