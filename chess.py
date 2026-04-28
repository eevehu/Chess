# Would it be better to store the different colored squares as two different arrays/lists?

# Dictionary for h4 = [7, 3]???
# Set up the Dictionary with a nested for loop assigning letters from a string to values
lateral = "ABCDEFGH"


def boardSetUp():
    board = {}
    pieces = ["p", "kn", "b", "r", "q", "k"]
    
    for letter in lateral:
        for number in range(8):
            board[f"{letter}{number+1}"] = []

    for i in [(2, "white"), (7, "black")]:
        for letter in lateral:
            board[f"{letter}{i[0]}"] = [pieces[0], i[1]]
            # print(board[f"{letter}{i[0]}"])

    for side in [[1, "white"], [8, "black"]]:
        for first in [[lateral[0], lateral[7], pieces[3]], 
                    [lateral[1], lateral[6], pieces[1]], 
                    [lateral[2], lateral[5], pieces[2]]]:
            # print(f"Position: {side[0]}\nColor: {side[1]}\nAt Positions: {first[0]}, {first[1]}\nPiece: {first[2]}")
            board[f"{first[0]}{side[0]}"] = [first[2], side[1]]
            board[f"{first[1]}{side[0]}"] = [first[2], side[1]]
            
    board[f"D1"] = [pieces[4], "white"]
    board[f"E1"] = [pieces[5], "white"]
    board[f"D8"] = [pieces[4], "black"]
    board[f"E8"] = [pieces[5], "black"]

    for i in reversed(range(8)):
        for j in lateral:
            square = board[f"{j}{i+1}"]
            if len(square) == 0:
                print("{:>4}".format(f"{square}"), end="")
            else:
                print("{:>4}".format(f"{square[0]}"), end="")
        print(end="\n\n")

    return board


def userMove(board, color):
    # I need to figure out which notation to use to move a piece. I think a coord H4, A4?, 
    # Based on that I can figure out the piece & and if its color matchs the person moving
    # And then if the position they're moving to is a valid one for that piece/isn't filled
    # I.E. A valid move position.

    format_error = "Incorrect Format"
    while (True):
        input_positions = input("Example: H4, A4\n").strip().split(", ")
        new_positions = []
        for position in input_positions:
            try:
                if len(position) != 2:
                    print(format_error)
                    break
                # elif position[0] not in lateral:
                #     print(format_error)
                #     break
                # elif int(position[1]) not in range(1, 9):
                #         print(format_error)
                #         break
                elif position in board:
                    new_positions.append(position)
                else:
                    print(format_error)
                    break
                
            except:
                print(format_error)
                continue
        if len(new_positions) != 2:
            continue
        elif board[f"{new_positions[0]}"] == [] or None:
            print("Square selected to move is empty")
            continue
        elif len(board[f"{new_positions[1]}"]) == 2:
            if board[f"{new_positions[1]}"][1] == color:
                print("Unable to move piece onto your own piece")
                continue
        
        print(f"Moving from {input_positions[0]} to {input_positions[1]}")
        break
                
while (True):
    board = boardSetUp()

    userMove(board, "white")