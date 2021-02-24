def chess_jumper(size):

    def generate_board(size):
        board = []
        for _ in range(size):
            row = [0 for _ in range(size)]
            board.append(row)
        return board


    def print_board(board):
        for row in board:
            print(row)


    # wszystkie możliwe ruchy skoczka
    steps = ((-2, 1), (-1, 2), (1, 2), (2, 1), (2, -1), (1, -2), (-1, -2), (-2, -1))


    def jump(row, col, count = 1):
        nonlocal size
        board[row][col] = count
        if count == size ** 2:
            print_board(board)
            return True
        else:
            for step in steps:
                in_scope = lambda x: x < size and x >= 0 
                next_row, next_col = row + step[0], col + step[1]
                if in_scope(next_row) and in_scope(next_col): # sprawdzanie, czy wychodzę poza tablicę
                    if board[next_row][next_col] == 0: # sprawdzanie, czy skoczek był już na tym polu
                        if jump(next_row, next_col, count+1): # jeśli znajdę rozwiązanie, to nie będę szukał dalej
                            return True
            
            # gdy skończą mi się możliwe ruchy, czyszczę ostatnie pole i się cofam
            # jak skończą mi się ruchy dla startowego pola, cała funkcja zwraca fałsz
            board[row][col] = 0 
            return False


    # sprawdzam, czy dla któregoś startowego pola znajdę rozwiązanie
    for row in range(size):
        for col in range(size):
            board = generate_board(size)
            if jump(row, col):
                return True
    
    return False


print(chess_jumper(8))