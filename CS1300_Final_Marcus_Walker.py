# -----------------------------
# Problem 1: Compound Interest Calculator
# -----------------------------

principal = float(input("Principal: "))
rate = float(input("Rate (%): "))
years = int(input("Years: "))

balance = principal

for year in range(1, years + 1):
    balance = balance * (1 + rate / 100)
    print(f"Year {year}: ${balance:.2f}")

interest = balance - principal
print(f"Total interest earned: ${interest:.2f}")

# -----------------------------
# Problem 2: Caesar Cipher Encoder
# -----------------------------

def caesar_encode(text, shift):
    result = ""

    for ch in text:
        if ch.isalpha():
            if ch.islower():
                new_char = chr((ord(ch) - 97 + shift) % 26 + 97)
            else:
                new_char = chr((ord(ch) - 65 + shift) % 26 + 65)
            result += new_char
        else:
            result += ch

    return result


print(caesar_encode("Hello, World!", 3))
print(caesar_encode("abc xyz", 2))
print(caesar_encode("Python 3", 5))



# -----------------------------
# Problem 4: Tic-Tac-Toe Winner Checker
# -----------------------------

def check_winner(board):
    # check rows
    for row in board:
        if row[0] == row[1] == row[2] != " ":
            return row[0]

    # check columns
    for col in range(3):
        if board[0][col] == board[1][col] == board[2][col] != " ":
            return board[0][col]

    # check diagonals
    if board[0][0] == board[1][1] == board[2][2] != " ":
        return board[0][0]

    if board[0][2] == board[1][1] == board[2][0] != " ":
        return board[0][2]

    # check if board is full
    full = True
    for row in board:
        if " " in row:
            full = False

    if full:
        return "Draw"

    return "Ongoing"


# -----------------------------
# Test Cases
# -----------------------------

board1 = [["X", "X", "X"],
          ["O", "O", " "],
          [" ", " ", " "]]
print(check_winner(board1))  # X

board2 = [["X", "O", "X"],
          ["X", "O", " "],
          [" ", "O", "X"]]
print(check_winner(board2))  # O

board3 = [["X", "O", "X"],
          ["X", "O", "O"],
          ["O", "X", "X"]]
print(check_winner(board3))  # Draw

board4 = [["X", "O", " "],
          [" ", "X", " "],
          [" ", " ", " "]]
print(check_winner(board4))  # Ongoing