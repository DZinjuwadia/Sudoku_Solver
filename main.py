"""
Learned how to...
- use recursive functions (in solve() function)
- become more fluent with matrices and imbedded matricies
- become more fluent in for loops
"""


def empty_check(example):
    for r in range(9):
        for c in range(9):
            if example[r][c] == 0:
                return r, c   # if there is an empty space, retun the row and column of that space

    return None, None   # if there are no empty spaces, return None

# ___________________________________________________________________________________________________


def validity_check(guess, example, r, c):

    row_val = example[int(r)]
    column_val = [
        example[0][int(c)],
        example[1][int(c)],
        example[2][int(c)],
        example[3][int(c)],
        example[4][int(c)],
        example[5][int(c)],
        example[6][int(c)],
        example[7][int(c)],
        example[8][int(c)]
    ]
    top_left_r_value = (int(r) // 3) * 3
    top_left_c_value = (int(c) // 3) * 3

    # checking validity in square
    for square_r_val in range(top_left_r_value, top_left_r_value + 3):
        for square_c_val in range(top_left_c_value, top_left_c_value + 3):
            if example[square_r_val][square_c_val] == guess:
                return False

    # checking validity in row, column
    if guess in row_val or guess in column_val:
        return False

    return True

# ___________________________________________________________________________________________________


def solve(example):
    row, col = empty_check(example)

    # if there isn't an empty row, col
    if row is None:
        return True

    """
    if there is an empty row & col, guess a random number from 1-9 
    and validity_check it. then recursively run the solve func and 
    if the whole example is solved, then you are done
    """
    for guess in range(1, 10):
        # if guess is valid, then that slot is filled with guess
        if validity_check(guess, example, row, col):
            example[row][col] = guess
            if solve(example):   # if the whole example is solved correctly, return True (means that you are done); otherwise start from top of function again and find new empty slot
                return True
        else:
            # if the guess is not valid, then set the value as 0 (or not determined)
            example[row][col] = 0
    else:
        # if none of the numbers work, then return False (means example is unsolvable)
        return False

# ___________________________________________________________________________________________________


if __name__ == "__main__":
    example = [
        [0, 0, 0, 2, 6, 0, 7, 0, 1],
        [6, 8, 0, 0, 7, 0, 0, 9, 0],
        [1, 9, 0, 0, 0, 4, 5, 0, 0],

        [0, 2, 0, 1, 0, 0, 0, 4, 0],
        [0, 0, 4, 6, 0, 2, 9, 0, 0],
        [0, 0, 0, 0, 0, 3, 0, 2, 8],

        [0, 0, 9, 3, 0, 0, 0, 7, 4],
        [0, 4, 0, 0, 5, 0, 0, 3, 0],
        [7, 0, 3, 0, 1, 0, 0, 0, 0]
    ]

    level = max = attempt = 0
    print(solve(example))
    print(example[0])
    print(example[1])
    print(example[2])
    print(example[3])
    print(example[4])
    print(example[5])
    print(example[6])
    print(example[7])
    print(example[8])
