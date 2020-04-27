import csv

Name = []      # Name
Email = []      # Email

def reading_data(N, E):
    with open('Task_Training_Data .csv', mode ='r') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter = ',')
        for row in csv_reader:
            N.append(row[0])
            E.append(row[1])
        return N, E

def reading_welcome_note():
    my_file = open('welcome_note.txt','r')
    my_str = my_file.read()
    print(my_str)
    my_file.close()

def game_instructions():
    my_file = open('game_instruction.txt','r')
    my_str = my_file.read()
    print(my_str)
    my_file.close()