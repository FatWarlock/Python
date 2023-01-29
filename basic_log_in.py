User_Name = input("pls enter user name: ")
User_Password = input("pls enter user password: ")

SystemUN = "Faith"
SystemPW = "908080"

if User_Name == SystemUN and User_Password == SystemPW:
    print("Hello {}, Welcome!!".format(User_Name))
elif User_Name != SystemUN and User_Password != SystemPW:
    print("Hello, User Name and Password are wrong!!")
elif User_Name != SystemUN and User_Password == SystemPW:
    print("Hello, User Name is wrong!!")
elif User_Name == SystemUN and User_Password != SystemPW:
    print("Hello {}, User Password is wrong!!".format(User_Name))
