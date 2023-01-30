import re

dateofbirth = "2002"
character = [ "\?","\*","\!","\%","."]

def passcontrol(password):
    if len(password)<8:
        raise Exception("password should have minumum 8 character!!!")
    elif not re.search("[a-z]",password):
        raise Exception("password should have 1 shortcase character!!!")
    elif not re.search("[A-Z]",password):
        raise Exception("password should have 1 uppercase character!!!")
    elif not re.search("[0-9]",password):
        raise Exception("password should have 1 number!!!")
    elif not re.search(str(character),password):
        raise Exception("password should have 1 character('?', '*','!', '%')!!!")
    elif password.startswith(dateofbirth)==True:
        raise Exception("password shouldn't start with your dateofbirth")
    elif password.endswith(dateofbirth)==True:
        raise Exception("password shouldn't end with your dateofbirth")
    else:
        print("Password successfully created...")

while True:
    try:
        password=input("Please create password....: ")
        passcontrol(password)
    except Exception as error:
        print(error)
    else:
        break