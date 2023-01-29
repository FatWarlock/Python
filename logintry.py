sayac = 2
for i in range(0, 3):
    userName = input("Kullanıcı Adı: ")
    userPassword = input("Kullanıcı Şifresi: ")
    systemUN = "Faith"
    systemUP = "11012002"

    if (userName == systemUN and userPassword == systemUP):
        print("login successful")
        break
    elif (userName != systemUN or userPassword != systemUP) and sayac != 0:
        print("login failed you can try {} more time".format(sayac))
        sayac -= 1
    else:
        print("login failed too much time try again later!!")
