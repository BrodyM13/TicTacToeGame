def board():
    # Game Board

    print('   |   |  ')
    print(' ' + test_board[7] + ' | ' + test_board[8] + ' | ' + test_board[9])
    print('   |   |  ')
    print('-----------')
    print('   |   |  ')
    print(' ' + test_board[4] + ' | ' + test_board[5] + ' | ' + test_board[6])
    print('   |   |  ')
    print('-----------')
    print('   |   |  ')
    print(' ' + test_board[1] + ' | ' + test_board[2] + ' | ' + test_board[3])
    print('   |   |  ')


def example_board():
    #Example Board and how to play
    print('   |   |   ')
    print('7  | 8 |  9')
    print('   |   |   ')
    print('------------')
    print('   |   |   ')
    print('4  | 5 |  6')
    print('   |   |   ')
    print('------------')
    print('   |   |   ')
    print('1  | 2 |  3')
    print('   |   |   ')
    print('Welcome to Tik Tak Toe')
    print()
    print('How to play: ')
    print()
    print('Enter a number between 1-9')
    print()


def choice():

    #Asks user if they want to be X's or O's and return result
    while True:
        print()
        player1 = input('Player 1: Do you want to be X or O: ')

        if player1.upper() == 'X' or player1.upper() == 'O':
            break
        else:
            print('Input invalid')
            print()
    return player1  # Returns X or O


def intro():
    #Asks user if they are ready to play return Boolean game_start
    while True:
        print()
        print('Player 1 will go first')
        print()
        answer = input('Are you ready to play? Enter Yes or No: ')
        if answer.lower() == 'yes':
            return True
        elif answer.lower() == 'no':
            return False
        else:
            print('\n'*100)
            print('Incorrect answer, try again: ')


def game_win1():
    #Sorts the p1 Dictionary in order to compare to the winning_pairs
    for z in p1win.keys():
        p1win[z].sort()
    #Compares Dictionaries
    for x in p1win.keys():
        if p1win[x] == winning_pairs[x]:
            board()
            #returns 1 if they do match
            return 1


def game_win2():
    #Sorts p2 Dictionary before comparing
    for z in p2win.keys():
        p2win[z].sort()
    #Compares both dictionaries to each oteher to find a winner
    for x in p2win.keys():
        if p2win[x] == winning_pairs[x]:
            board()
            #returns 1 if they do match
            return 1


def player_one():

    board()

    while game_start:

        #If user enters a non int answer will be -1 and won't pass the first if statement
        try:
            answer = int(input('Player 1: Enter next position 1-9'))
        except:
            answer = -1

        #Has to be inbetween 1-9
        if answer >= 10 or answer <= 0:
            print()
            print('Value not valid')
            print()

        #Checks to see if there is already a X or O in that index
        elif test_board[answer] == 'O' or test_board[answer] == 'X':
            print('Player already in that position')
            print('')
        elif answer == 1:
            test_board[1] = player1.upper()
            p1win['1'].append(int(answer))
            p1win['4'].append(int(answer))
            p1win['7'].append(int(answer))
            print('\n' * 100)
            break
        elif answer == 2:
            test_board[2] = player1.upper()
            p1win['1'].append(int(answer))
            p1win['5'].append(int(answer))
            print('\n' * 100)
            break
        elif answer == 3:
            test_board[3] = player1.upper()
            p1win['1'].append(int(answer))
            p1win['6'].append(int(answer))
            p1win['8'].append(int(answer))
            print('\n' * 100)
            break
        elif answer == 4:
            test_board[4] = player1.upper()
            p1win['2'].append(int(answer))
            p1win['4'].append(int(answer))
            print('\n' * 100)
            break
        elif answer == 5:
            test_board[5] = player1.upper()
            p1win['2'].append(int(answer))
            p1win['5'].append(int(answer))
            p1win['7'].append(int(answer))
            p1win['8'].append(int(answer))
            print('\n' * 100)
            break
        elif answer == 6:
            test_board[6] = player1.upper()
            p1win['2'].append(int(answer))
            p1win['6'].append(int(answer))
            print('\n' * 100)
            break
        elif answer == 7:
            test_board[7] = player1.upper()
            p1win['3'].append(int(answer))
            p1win['4'].append(int(answer))
            p1win['8'].append(int(answer))
            print('\n' * 100)
            break
        elif answer == 8:
            test_board[8] = player1.upper()
            p1win['3'].append(int(answer))
            p1win['5'].append(int(answer))
            p1win['8'].append(int(answer))
            print('\n' * 100)
            break
        elif answer == 9:
            test_board[9] = player1.upper()
            p1win['3'].append(int(answer))
            p1win['6'].append(int(answer))
            p1win['7'].append(int(answer))
            print('\n' * 100)
            break


def player_two():

    player2 = ''

    if player1.lower() == 'x':
        player2 = 'O'
    elif player1.lower() == 'o':
        player2 = 'X'

    board()

    while game_start:
        # If user enters a non int answer will be -1 and won't pass the first if statement
        try:
            answer = int(input('Player 1: Enter next position 1-9'))
        except:
            answer = -1

        # Has to be in between 1-9
        if answer >= 10 or answer <= 0:
            print('')
            print('Value not valid')
            print('')
        # Checks to see if there is already a X or O in that index
        elif test_board[answer] == 'O' or test_board[answer] == 'X':
            print('Player already in that position')
            print('')
        elif answer == 1:
            test_board[1] = player2.upper()
            p2win['1'].append(int(answer))
            p2win['4'].append(int(answer))
            p2win['7'].append(int(answer))
            print('\n' * 100)
            break
        elif answer == 2:
            test_board[2] = player2.upper()
            p2win['1'].append(int(answer))
            p2win['5'].append(int(answer))
            print('\n' * 100)
            break
        elif answer == 3:
            test_board[3] = player2.upper()
            p2win['1'].append(int(answer))
            p2win['6'].append(int(answer))
            p2win['8'].append(int(answer))
            print('\n' * 100)
            break
        elif answer == 4:
            test_board[4] = player2.upper()
            p2win['2'].append(int(answer))
            p2win['4'].append(int(answer))
            print('\n' * 100)
            break
        elif answer == 5:
            test_board[5] = player2.upper()
            p2win['2'].append(int(answer))
            p2win['5'].append(int(answer))
            p2win['7'].append(int(answer))
            p2win['8'].append(int(answer))
            print('\n' * 100)
            break
        elif answer == 6:
            test_board[6] = player2.upper()
            p2win['2'].append(int(answer))
            p2win['6'].append(int(answer))
            print('\n' * 100)
            break
        elif answer == 7:
            test_board[7] = player2.upper()
            p2win['3'].append(int(answer))
            p2win['4'].append(int(answer))
            p2win['8'].append(int(answer))
            print('\n' * 100)
            break
        elif answer == 8:
            test_board[8] = player2.upper()
            p2win['3'].append(int(answer))
            p2win['5'].append(int(answer))
            p2win['8'].append(int(answer))
            print('\n' * 100)
            break
        elif answer == 9:
            test_board[9] = player2.upper()
            p2win['3'].append(int(answer))
            p2win['6'].append(int(answer))
            p2win['7'].append(int(answer))
            print('\n' * 100)
            break


def play():

    winner_place = ''
    while game_start:
        player_one()  # Player 1's move
        rand1 = game_win1()
        #game_win1 returns 1 if winning_board[x] == p1win[x]
        if rand1 == 1:
            winner_place = 'p1'
            break
        player_two()  # Player 2's move
        rand2 = game_win2()
        # game_win2 returns 1 if winning_board[x] == p2win[x]
        if rand2 == 1:
            winner_place = 'p2'
            break
    #returns who won
    return winner_place


def replay_ask(true_winner):
    #Shows who won the game
    if true_winner == 'p1':
        print()
        print('Player 1 is the winner!!')
    elif true_winner == 'p2':
        print()
        print('Player 2 is the winner!!')

    #Asks user if they want to play again
    while game_start:
        print()
        answer = input('Would you like to play again?')
        if answer.lower() == 'yes':
            return True
        elif answer.lower() == 'no':
            return False
        else:
            print('Wrong input')
            print()


def reset():

    #resets both dictionaries for next game
    for x in p1win.keys():
        p1win[x].clear()
    for z in p2win.keys():
        p2win[z].clear()


test_board = [' '] * 10  # Empty Array for board

winning_pairs = {'1': [1, 2, 3], '2': [4, 5, 6], '3': [7, 8, 9], '4': [1, 4, 7], '5': [2, 5, 8], '6': [3, 6, 9],
                 '7': [1, 5, 9], '8': [3, 5, 7]}  #all winning combo's

#Empty dictionary that compares to winning_pairs as the user enters position
p1win = {'1': [], '2': [], '3': [], '4': [], '5': [], '6': [], '7': [], '8': []}

p2win = {'1': [], '2': [], '3': [], '4': [], '5': [], '6': [], '7': [], '8': []}

game_start = True

example_board()

while game_start:

    reset()

#Resets the board for replay's
    test_board = [' '] * 10

    player1 = choice()  # X or O

    game_start = intro()  # Asks if ready

    winner = play()

    game_start = replay_ask(winner)
