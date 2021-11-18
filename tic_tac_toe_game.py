print(' '*10 + '*tic tac toe game*' + ' '*10 + '\n\n\n')
num = int(input('Choose the size of the board(1 number) ->'))
print('\n\n')



board = [['_']*(num) for _ in range((num))]
board_new = [['_']*(num) for _ in range((num))]
counter = num**2


def game_try(*args):
    for i in range(num):
        if '_' not in board[i] and len(set(board[i])) == 1:
            return True
        else:
            set1 = []
            for i in range(num):
                for j in range(num):
                    if i == j:
                        set1.append(board[i][j])
            if ('_' not in set1) and (len(set(set1)) == 1):
                return True
            else:
                set2 = []
                for i in range(num):
                    for j in range(num):
                        if j == num - i - 1:
                            set2.append(board[i][num-i-1])
                if '_' not in set2 and len(set(set2)) == 1:
                    return True
                else:
                    set3 = []
                    for j in range(num):
                        for i in range(num):
                            set3.append(board[i][j])
                        if ('_' not in set3) and (len(set(set3)) == 1):
                            return True
                        else:
                            set3 = []
                            continue
 





x_turn = True
o_turn = False
game_on = True

for i in range(num):
        for j in range(num):
            print(board[i][j], end=' ')
        print()



while game_on: 

    print('\n ')
    print('If you want to stop, write "stop" anytime')
    print('\n ')
    if x_turn:
        print("Now it's x's turn:\n")
        column = input('Column number ->') 
        if column.lower() == 'stop':
            game_on = False
            break
        row = input('row number ->') 
        if row.lower() == 'stop':
            game_on = False
            break
        board[int(column) - 1][int(row) - 1] = 'x'
        print('\n')
        for i in range(num):
            for j in range(num):
                print(board[i][j], end=' ')
            print()
        print('\n')
        x_turn = False
        o_turn = True
        counter -= 1
        if game_try():
            game_on = False
            print('X wins!')
            break
        if counter == 0:
            game_on = False
            print('Draw!')

            break
        



    if o_turn:
        print("Now it's o's turn:\n")
        column = input('Column number ->')
        if column.lower() == 'stop':
            game_on = False
            break
        row = input('Row number ->') 
        if row.lower() == 'stop':
            game_on = False
            break
        board[int(column) - 1][int(row) - 1] = 'o'
        print('\n')
        for i in range(num):
            for j in range(num):
                print(board[i][j], end=' ')
            print()
        print('\n')
        o_turn = False
        x_turn = True
        counter -= 1
        if game_try():
            game_on = False
            print('O wins!')
            break
        if counter == 0:
            game_on = False
            print('Draw!')
            break
