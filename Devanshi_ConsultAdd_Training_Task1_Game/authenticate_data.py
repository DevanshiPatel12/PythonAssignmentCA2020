from read_csv import *
from game_functionality import matrix_game

def Name_Email():
    dict = {}
    for N in Name:
        for E in Email:
            dict[N] = E
            Email.remove(E)
            break
    print(dict)

    for count in range(0,3):
        U_Name = input("Enter your name : ")
        U_Email = input("Enter your email : ")

        if U_Name in dict:
            Value = dict[U_Name]
            if Value == U_Email:
                print("Verified! Let's move forward")
                break
            else:
                print("Sorry! Email is wrong")
        else:
            print("Sorry! Name or Email is wrong")
    return count

def input_try():
    try:
        i = input("Enter P to Play : ")
        if i == 'P' or i == 'p':
            matrix_game()
        else:
            raise Exception
    except Exception:
        print("You entered wrong choice! Enter P to play")
        input_try()

def Main_Program():
    reading_data(Name, Email)
    count = 0
    r_count = Name_Email()
    if r_count == 2:
        print("Sorry, Too many try !! Bye")
    else:
        reading_welcome_note()
        response = input("Enter response : ")
        if response == 'Yes' or response == 'yes':
            print("\nLet's move forward and see the instructions")
            game_instructions()
            input_try()  # function for 'P' to play
        else:
            print("Terminated! Bye")

Main_Program()