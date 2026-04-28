# Would it be better to store the different colored squares as two different arrays/lists?

# Dictionary for h4 = [7, 3]???
# Set up the Dictionary with a nested for loop assigning letters from a string to values
lateral = "ABCDEFGH"
pieces = ["p", "kn", "b", "r", "q", "k"]

def boardSetUp():
    board = {}
    
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

    # for i in reversed(range(8)):
    #     for j in lateral:
    #         square = board[f"{j}{i+1}"]
    #         if len(square) == 0:
    #             print("{:>4}".format(f"{square}"), end="")
    #         else:
    #             print("{:>4}".format(f"{square[0]}"), end="")
    #     print(end="\n\n")

    return board

def pawnMovement(startPoint, endPoint, board, attacking):
    # Work on en-passant later

    piece = board[f"{endPoint}"]
    if attacking:
        if int(endPoint[1]) - int(startPoint[1])!= 1:
            return False
        index = lateral.find(startPoint[0])
        print(index)
        # Implement checking for that the attacks are in range!!! 
        # Also, probably move this code to a different function that each of the pieces make use of
        # It increases coupling... Maybe don't idk


def userMove(board, color):
    # I need to figure out which notation to use to move a piece. I think a coord H4, A4?, 
    # Based on that I can figure out the piece & and if its color matchs the person moving
    # And then if the position they're moving to is a valid one for that piece/isn't filled
    # I.E. A valid move position.
    board[f"B3"] = ["p", "black"] # for cheking pawn attacking

    format_error = "Incorrect Format"
    new_positions = []
    while (True):
        taking = False
        input_positions = input("Example: H4, A4\n").strip().split(", ")
        for position in input_positions:
            try:
                if len(position) != 2:
                    print(format_error)
                    break
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
            taking = True
            if board[f"{new_positions[1]}"][1] == color:
                print("Unable to move piece onto your own piece")
                continue
        
        print(f"Moving from {input_positions[0]} to {input_positions[1]}")

    
        piece = board[f"{new_positions[0]}"][0]
        if piece == pieces[0]:
            print("Selected square is a Pawn")
            if pawnMovement(new_positions[0], new_positions[1], board, taking) == False:
                print("Pawn is unable to move to that position")
                continue
            else:
                return
        elif piece == pieces[1]:
            print("Selected square is a Knight")
        elif piece == pieces[2]:
            print("Selected square is a Bishop")
        elif piece == pieces[3]:
            print("Selected square is a Rook")
        elif piece == pieces[4]:
            print("Selected square is a Queen")
        elif piece == pieces[5]:
            print("Selected square is a King")
        else:
            print("Somehow the selected piece is.... Not a piece? Weird, huh")


while (True):
    board = boardSetUp()

    userMove(board, "white")