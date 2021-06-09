print("Welcome to tic tac toe!")


def exit_game():
    ext = input('Type exit if you want to quit playing: ')
    if ext == 'exit':
        exit()


def win_combo():
    pass


def play():
    while True:
        print("___|___|___ \n"
              "___|___|___\n"
              "   |   |  "
              )

        user1_input = []
        user2_input = []

        user1 = 0
        while not 0 < int(user1) < 10:
            user1 = input("User1, Type a number between 1 and 9: ")
        user1_input = user1_input.append(user1)
        print(user1_input)
        print(user1)

        user2 = 0
        while not 0 < int(user2) < 10:
            user2 = input("User2, type a number between 1 and 9: ")
        user2_input = user2_input.append(user2)
        print(user2_input)


play()
exit_game()
