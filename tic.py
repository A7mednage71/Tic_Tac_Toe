def draw_tic(tic_board):
    for i in range(3):
        for j in range(3):
            print(f"| {tic_board[i][j]} |", end=" ")
        print("\n-----------------")


def equal(x, y, z):
    if x == y == z and x != ' ':
        return True
    return False


def check_for_winner(tic_board):
    #  2: X winner
    # -2: O winner
    #  0: Tie
    #  1: No winner

    for i in range(3):
        if equal(tic_board[i][0], tic_board[i][1], tic_board[i][2]):
            if tic_board[i][0] == 'X':
                return 2
            else:
                return -2

    for i in range(3):
        if equal(tic_board[0][i], tic_board[1][i], tic_board[2][i]):
            if tic_board[0][i] == 'X':
                return 2
            else:
                return -2

    if equal(tic_board[0][0], tic_board[1][1], tic_board[2][2]):
        if tic_board[0][0] == 'X':
            return 2
        else:
            return -2

    if equal(tic_board[0][2], tic_board[1][1], tic_board[2][0]):
        if tic_board[0][2] == 'X':
            return 2
        else:
            return -2

    for row in tic_board:
        if ' ' in row:
            return 1

    return 0


def minmax(tic_board, depth, is_maximizing, first=True):
    res = check_for_winner(tic_board)
    if res != 1 or depth == 0:
        return res

    if is_maximizing:
        final_score = -10
        score_i, score_j = None, None
        for i in range(3):
            for j in range(3):
                if tic_board[i][j] == ' ':
                    tic_board[i][j] = 'X'
                    score = minmax(tic_board, depth - 1, False, False)
                    tic_board[i][j] = ' '
                    if score > final_score:
                        final_score = score
                        score_i = i
                        score_j = j

        if first is True:
            tic_board[score_i][score_j] = 'X'
        return final_score
    else:
        final_score = 10
        score_i, score_j = None, None
        for i in range(3):
            for j in range(3):
                if tic_board[i][j] == ' ':
                    tic_board[i][j] = 'O'
                    score = minmax(tic_board, depth - 1, True, False)
                    tic_board[i][j] = ' '
                    if score < final_score:
                        final_score = score
                        score_i = i
                        score_j = j

                    if first is True:
                        print("Score : ", i, ",", j, " is ", score)

        if first is True:
            tic_board[score_i][score_j] = 'O'
        return final_score


def main():
    tic_board = [[' ' for _ in range(3)] for _ in range(3)]
    there_is_winner = False
    player = 'X'

    while not there_is_winner:
        x, y = map(int, input().split())

        if 0 <= x < 3 and 0 <= y < 3:
            if tic_board[x][y] == ' ':
                tic_board[x][y] = player
                result = minmax(tic_board, 100, False)
                draw_tic(tic_board)
                print(f" Result : {result} ")

                there_is_winner = check_for_winner(tic_board) != 1
            else:
                print('The Field is not empty')
        else:
            print('Invalid input')

    final_result = check_for_winner(tic_board)

    if final_result == 2:
        print('X player wins')
    elif final_result == -2:
        print('Y player wins')
    else:
        print('Tie')


if __name__ == "__main__":
    main()
