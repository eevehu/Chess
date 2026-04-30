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

    board["B3"] = ["p", "black"] # for cheking pawn attacking
    board["A7"] = ["p", "white"] # for cheking pawn attacking

    for i in reversed(range(8)):
        print("{:>2}".format(f"{i+1}|"), end="")
        for j in lateral:
            square = board[f"{j}{i+1}"]
            if len(square) == 0:
                print("{:>4}".format(f"{square}"), end="")
            else:
                if square[1] == "white":
                    print("{:>4}".format(f"{square[0].upper()}"), end="")
                else:
                    print("{:>4}".format(f"{square[0]}"), end="")
        if i != 0:
            print(end="\n\n")
        else: 
            print(end="\n")

    print("{:>2}".format(""), end="")
    print("{:>4}".format("_") * 8)
    print("{:>2}".format(""), end="")
    
    for i in range(8):
        print("{:>4}".format(lateral[i]), end="")
    print(end="\n\n")
    return board

def boardUpdate(movedPiece):
    if len(board[f"{movedPiece[1]}"]) == 2:
        print(f"You Took A {board[f"{movedPiece[0]}"][1].upper()}")
    board[f"{movedPiece[1]}"] = board[f"{movedPiece[0]}"]
    board[f"{movedPiece[0]}"] = []
    print("Updated Board!!")

    for i in reversed(range(8)):
        print("{:>2}".format(f"{i+1}|"), end="")
        for j in lateral:
            square = board[f"{j}{i+1}"]
            if len(square) == 0:
                print("{:>4}".format(f"{square}"), end="")
            else:
                if square[1] == "white":
                    print("{:>4}".format(f"{square[0].upper()}"), end="")
                else:
                    print("{:>4}".format(f"{square[0]}"), end="")
        if i != 0:
            print(end="\n\n")
        else: 
            print(end="\n")

    print("{:>2}".format(""), end="")
    print("{:>4}".format("_") * 8)
    print("{:>2}".format(""), end="")
    
    for i in range(8):
        print("{:>4}".format(lateral[i]), end="")
    print(end="\n\n")
    return
    # Change the dictionary of pieces
    # Then, reload the actual board

def pawnMovement(startPoint, endPoint, board, attacking):
    # Work on en-passant later
    piece = board[f"{startPoint}"]
    color = piece[1]
    upgrading = False
    print(f"|{color}|")

    index = lateral.find(startPoint[0]) # Will get the position of the horizontal
    enemyIndex = lateral.find(endPoint[0])

    if color == "white":
        verticalDistance = int(endPoint[1]) - int(startPoint[1])
    else:
        verticalDistance = int(startPoint[1]) - int(endPoint[1])
    if verticalDistance > 2 or verticalDistance < 1:
        return False
    
    if endPoint[1] == "8" or endPoint[1] == "1":
        while (True):
            upgrade = input("Choose a piece to upgrade to: ki, b, r, or q\n").strip().lower()
            if upgrade in pieces:
                upgrading = True
                break
            else:
                upgrading = False
                print("Invalid Upgrade")
                continue
    else:
        upgrading = False
        
    if attacking:
        enemyPiece = board[f"{endPoint}"][0]
        if (verticalDistance != 1 or index == enemyIndex) or (abs(index - enemyIndex) != 1):
            return False
        if upgrading:
            board[f"{startPoint}"] = [upgrade, color]
        boardUpdate([startPoint, endPoint])
        # Implement actually taking a piece and updating the board
    else:
        if startPoint[0] != endPoint[0]:
            return False
        if verticalDistance == 2:
            if (startPoint[1] == "2") and (color == "white") or (startPoint[1] == "7") and (color == "black"):
                if upgrading:
                    board[f"{startPoint}"] = [upgrade, color]
                boardUpdate([startPoint, endPoint])
            else:
                print("Failed here")
                return False
        else:
            boardUpdate([startPoint, endPoint])

def knightMovement(startPoint, endPoint, board):
    possibleMoves = []
    try:
        vertical = int(startPoint[1])
    except:
        print("I genuinely do not understand how you've done this")
    horizontal = lateral.index(startPoint[0])
    
    if vertical + 1 <= 8: # Top right
        if vertical + 2 <= 8:
            if horizontal + 1 < len(lateral): # Vertical High
                possibleMoves.append(f"{lateral.__getitem__(horizontal+1)}{vertical+2}")
        if horizontal + 2 < len(lateral): # Horizontal High
            possibleMoves.append(f"{lateral.__getitem__(horizontal+2)}{vertical+1}")
    if vertical - 1 > 0:
        if vertical - 2 > 0: # Bottom right
            if horizontal + 1 < len(lateral): # Vertical Low
                possibleMoves.append(f"{lateral.__getitem__(horizontal+1)}{vertical-2}")
        if horizontal + 2 < len(lateral): # Horizontal Low
            possibleMoves.append(f"{lateral.__getitem__(horizontal+2)}{vertical-1}")
    if horizontal - 1 >= 0: # Top Left
        if horizontal - 2 >= 0:
            if vertical + 1 <= 8: # Vertical High
                possibleMoves.append(f"{lateral.__getitem__(horizontal-2)}{vertical+1}")
            if vertical - 1 > 0:
                possibleMoves.append(f"{lateral.__getitem__(horizontal-2)}{vertical-1}")
        if vertical + 2 <= 8:
                possibleMoves.append(f"{lateral.__getitem__(horizontal-1)}{vertical+2}")
        if vertical - 2 > 0:
                possibleMoves.append(f"{lateral.__getitem__(horizontal-1)}{vertical-2}")
    
    print(f"The possible moves for a knight to take from the {startPoint} are:")
    for i in range(len(possibleMoves)):
        print(possibleMoves[i])
    
    if endPoint in possibleMoves:
        boardUpdate([startPoint, endPoint])
        return
    else: 
        print("Invalid Knight Move")
        return False
                     

def movement(startPoint, endPoint, board):
    piece = board[f"{startPoint}"]
    color = piece[1]

    index = lateral.find(startPoint[0]) # Will get the position of the horizontal
    enemyIndex = lateral.find(endPoint[0])

    if color == "white":
        verticalDistance = int(endPoint[1]) - int(startPoint[1])
    else:
        verticalDistance = int(startPoint[1]) - int(endPoint[1])
    

def userMove(board, color):
    # I need to figure out which notation to use to move a piece. I think a coord H4, A4?, 
    # Based on that I can figure out the piece & and if its color matchs the person moving
    # And then if the position they're moving to is a valid one for that piece/isn't filled
    # I.E. A valid move position.

    format_error = "Incorrect Format"
    while (True):
        taking = False
        new_positions = []
        input_positions = input().upper().strip().split(", ")
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
        if len(new_positions) != 2 or board[f"{new_positions[0]}"] == [] or None:
            print(format_error)
            continue
        elif len(board[f"{new_positions[1]}"]) == 2:
            if board[f"{new_positions[1]}"][1] == color:
                print("Unable to move piece onto your own piece")
                continue
            taking = True

        if board[f"{new_positions[0]}"][1] != color:
            print("That is not your piece")
            continue
            
        
        # print(f"Moving from {input_positions[0]} to {input_positions[1]}")

    
        piece = board[f"{new_positions[0]}"][0]
        if piece == pieces[0]:
            if pawnMovement(new_positions[0], new_positions[1], board, taking) == False:
                print("Pawn is unable to move to that position")
                continue
            else:
                return
        elif piece == pieces[1]:
            print("Selected square is a Knight")
            if knightMovement(new_positions[0], new_positions[1], board) == False:
                print("Knight is unable to move to that position")
                continue
            else:
                return
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


board = boardSetUp()
players = ["white", "black"]

print("Move with the notation: (Piece's Square), (Square Your Piece Will Move To) I.E -- D2, D4")

while (True):
    for i in range(0, 2):
        print(f"Player: {players[i]}")
        userMove(board, players[i])