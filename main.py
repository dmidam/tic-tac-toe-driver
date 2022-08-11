turn = 0

print('''Welcome to Tic Tac Toe game, have fun
     |     |     
  1  |  2  |  3  
_____|_____|_____
     |     |     
  4  |  5  |  6  
_____|_____|_____
     |     |     
  7  |  8  |  9  
     |     |      ''')
# choice = input("Welcome to Tik Tac Toe game. Do you choose O or X?:").upper()

k = '''
     |     |     
     |     |     
_____|_____|_____
     |     |     
     |     |     
_____|_____|_____
     |     |     
     |     |     
     |     |     '''


new = list(k)
player_one_name = input("Player 1, enter your name: ").title()
player_two_name = input("Player 2, enter your name: ").title()
while True:
    turn += 1

    print(turn)

    player_one = input(f"{player_one_name}: where do you want to draw (position 1-9)? ")
    if turn >= 9:
        print("It's a draw!!")
        break

    if player_one == "1":
        new[21] = "O"
        print("".join(new))
    elif player_one == "2":
        new[27] = "O"
        print("".join(new))
    elif player_one == "3":
        new[33] = "O"
        print("".join(new))
    elif player_one == "4":
        new[75] = "O"
        print("".join(new))
    elif player_one == "5":
        new[81] = "O"
        print("".join(new))
    elif player_one == "6":
        new[87] = "O"
        print("".join(new))
    elif player_one == "7":
        new[129] = "O"
        print("".join(new))
    elif player_one == "8":
        new[135] = "O"
        print("".join(new))
    elif player_one == "9":
        new[141] = "O"
        print("".join(new))

    if new[21] == "O" and new[27] == "O" and new[33] == "O":
        print(f"{player_one_name} won!")
        break
    elif new[75] == "O" and new[81] == "O" and new[87] == "O":
        print(f"{player_one_name} won!")
        break
    elif new[129] == "O" and new[135] == "O" and new[141] == "O":
        print(f"{player_one_name} won!")
        break
    elif new[21] == "O" and new[75] == "O" and new[129] == "O":
        print(f"{player_one_name} won!")
        break
    elif new[27] == "O" and new[81] == "O" and new[135] == "O":
        print(f"{player_one_name} won!")
        break
    elif new[33] == "O" and new[87] == "O" and new[141] == "O":
        print(f"{player_one_name} won!")
        break
    elif new[21] == "O" and new[81] == "O" and new[141] == "O":
        print(f"{player_one_name} won!")
        break
    elif new[33] == "O" and new[81] == "O" and new[129] == "O":
        print(f"{player_one_name} won!")
        break

    player_two = input(f"{player_two_name}: where do you want to draw (position 1-9)? ")
    turn += 1

    if player_two == "1":
        new[21] = "X"
        print("".join(new))
    elif player_two == "2":
        new[27] = "X"
        print("".join(new))
    elif player_two == "3":
        new[33] = "X"
        print("".join(new))
    elif player_two == "4":
        new[75] = "X"
        print("".join(new))
    elif player_two == "5":
        new[81] = "X"
        print("".join(new))
    elif player_two == "6":
        new[87] = "X"
        print("".join(new))
    elif player_two == "7":
        new[129] = "X"
        print("".join(new))
    elif player_two == "8":
        new[135] = "X"
        print("".join(new))
    elif player_two == "9":
        new[141] = "X"
        print("".join(new))

    if new[21] == "X" and new[27] == "X" and new[33] == "X":
        print(f"{player_two_name} won!")
        break
    elif new[75] == "X" and new[81] == "X" and new[87] == "X":
        print(f"{player_two_name} won!")
        break
    elif new[129] == "X" and new[135] == "X" and new[141] == "X":
        print(f"{player_two_name} won!")
        break
    elif new[21] == "X" and new[75] == "X" and new[129] == "X":
        print(f"{player_two_name} won!")
        break
    elif new[27] == "X" and new[81] == "X" and new[135] == "X":
        print(f"{player_two_name} won!")
        break
    elif new[33] == "X" and new[87] == "X" and new[141] == "X":
        print(f"{player_two_name} won!")
        break
    elif new[21] == "X" and new[81] == "X" and new[141] == "X":
        print(f"{player_two_name} won!")
        break
    elif new[33] == "X" and new[81] == "X" and new[129] == "X":
        print(f"{player_two_name} won!")
        break
