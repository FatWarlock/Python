number = 25
chance = 10

while chance > 0:
    guess = int(input("Pls enter positive integer: "))
    if guess < 0:
        print("this is not a positive integer")
        continue
    chance -= 1
    if guess == 0:
        print("zero is a neutral integer dont forgot again")
        continue
    if guess == number:
        print("you founded correct number, nice job!")
        break
    elif number > guess:
        print("up, you have {} more chances use carefully".format(chance))
    elif number < guess:
        print("down, you have {} more chances use carefully".format(chance))
    if chance == 0:
        print("you already use your chances try next time")
