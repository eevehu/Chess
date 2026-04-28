# Would it be better to store the different colored squares as two different arrays/lists?

# Dictionary for h4 = [7, 3]???
# Set up the Dictionary with a nested for loop assigning letters from a string to values



def boardSetUp():
    board = {}
    pieces = ["p ", "kn", "b", "r", "q", "k"]

    lateral = "ABCDEFGH"
    for letter in lateral:
        for number in range(8):
            board[f"{letter}{number+1}"] = []

    for i in [(2, "white"), (7, "black")]:
        for letter in lateral:
            board[f"{letter}{i[0]}"] = [pieces[0], i[1]]
            print(board[f"{letter}{i[0]}"])

    for side in [[8, "white"], [1, "black"]]:
        for first in [[lateral[0], lateral[7], pieces[3]], 
                    [lateral[1], lateral[6], pieces[1]], 
                    [lateral[2], lateral[5], pieces[2]]]:
            print(f"Position: {side[0]}\nColor: {side[1]}\nAt Positions: {first[0]}, {first[1]}\nPiece: {first[2]}")
            
    return board


lateral = "ABCDEFGH"
board = boardSetUp()

for i in reversed(range(8)):
    for j in lateral:
        square = board[f"{j}{i+1}"]
        if len(square) == 0:
            print("{:>4}".format(f"{square}"), end="")
        else:
            print("{:>4}".format(f"{square[0]}"), end="")
    print(end="\n\n")