print("Hello, welocme to Body Mass Index calculator application")

Height = int(input("Pls enter your height (cm): "))
Weight = int(input("Pls enter your weight (kg): "))

Index = round((Weight/((Height/100)**2)), 2)

if Index <= 18.5:
    print("calculated Body Mass Index : {} , you are underWeight ".format(Index))
elif Index <= 24.9 and Index >= 18.6:
    print("calculated Body Mass Index : {} , you are normalWeight ".format(Index))
elif Index <= 29.9 and Index >= 25:
    print("calculated Body Mass Index : {} , you are overWeight ".format(Index))
else:
    print("calculated Body Mass Index : {} , you are Obesity".format(Index))
