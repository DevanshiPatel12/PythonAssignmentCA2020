class PasswordError(Exception):
    pass
class LoginFail(Exception):
    pass
UserEmail, Password = "Devanshi", "1234"
count = 0
def LoginPage():
    U = input("Enter your UserEmail : ")
    P1 = input("Enter your Password : ")
    P2 = input("Enter your Password again : ")

    try:
        if U == UserEmail and P1 == Password and P2 == P1:
            print("Successful Login. Welcome !!")
        elif P1 != P2 or P1 != Password:
            raise PasswordError
        elif U != UserEmail:
            raise LoginFail
    except PasswordError:
        print("Password is wrong")
        global count
        if count < 2:
            count = count + 1
            LoginPage()
        else:
            print("Too many try. Sorry !!")
    except LoginFail:
        print("UserEmail is wrong")
        LoginPage()

LoginPage()
