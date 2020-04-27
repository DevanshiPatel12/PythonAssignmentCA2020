def game_input_matrix():
    s = int(input("Enter size of the matrix : "))
    print("Enter matrix rows values with space below and then hit enter for next row")
    for i in range(s):
        v = input().split(" ")
        r = []
        for j in v:
            r.append(int(j))
        m.append(r)
    return m

def matrix_size_guess():
    game_input_matrix()
    for i in m:
        count = 0
        for index in range(len(m)):
            if i[index] == 1:
                count = count + 1
            else:
                count = count
        horizontal.append(count)
    l = 0
    while l < len(m):
        count = 0
        for i in m:
            if i[l] == 1:
                count = count + 1
            else:
                count = count
        vertical.append(count)
        l = l + 1

def matrix_game():
    matrix_size_guess()

    print("Now you have to guess the size of River \n")
    string = input("How do you like to guess the size of River ??   Horizontal or Vertical ? \nEnter here : ")

    H_count = 0
    V_count = 0
    if string == 'Horizontal' or string == 'horizontal':
        values = input("\nEnter size of your guess for each rows : ").split(" ")
        H = []
        for val in values:
            H.append(int(val))

        for i in H:
            if (i in horizontal):
                H_count = H_count + 1
                horizontal.remove(i)
            else:
                H_count = H_count
    else:
        values = input("\nEnter size of your guess for each columns : ").split(" ")
        V = []
        for val in values:
            V.append(int(val))

        for j in V:
            if (j in vertical):
                V_count = V_count + 1
                vertical.remove(j)
            else:
                V_count = V_count

    if H_count == len(m) or V_count == len(m):
        print("\nYAY !!!! \nYou are the winner")
    elif H_count > len(m)/2 or V_count > len(m)/2:
        print("\nNOT BAD !!! \nYou got the second position")
    else:
        print("\nInvest more money on Almonds, then come back :-)")

m = []
horizontal = []
vertical = []