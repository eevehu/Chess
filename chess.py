import sys
import unicodedata
# Would it be better to store the different colored squares as two different arrays/lists?

# Dictionary for h4 = [7, 3]???
# Set up the Dictionary with a nested for loop assigning letters from a string to values
lateral = "ABCDEFGH"
# pieces = ["p", "kn", "b", "r", "q", "k"]
whitePieces = ['\u2659', '\u2658', '\u2657', '\u2656', '\u2655', '\u2654']
blackPieces = ['\u265F', '\u265E', '\u265D', '\u265C', '\u265B', '\u265A']

white_to_black = {w: b for w, b in zip(whitePieces, blackPieces)}

def boardSetUp():
    board = {}
    
    for letter in lateral:
        for number in range(8):
            board[f"{letter}{number+1}"] = ["\u25A1"]

    for i in [(2, "white"), (7, "black")]:
        for letter in lateral:
            board[f"{letter}{i[0]}"] = [whitePieces[0], i[1]]
            # print(board[f"{letter}{i[0]}"])

    for side in [[1, "white"], [8, "black"]]:
        for first in [[lateral[0], lateral[7], whitePieces[3]], 
                    [lateral[1], lateral[6], whitePieces[1]], 
                    [lateral[2], lateral[5], whitePieces[2]]]:
            # print(f"Position: {side[0]}\nColor: {side[1]}\nAt Positions: {first[0]}, {first[1]}\nPiece: {first[2]}")
            board[f"{first[0]}{side[0]}"] = [first[2], side[1]]
            board[f"{first[1]}{side[0]}"] = [first[2], side[1]]
            
    board[f"D1"] = [whitePieces[4], "white"]
    board[f"E1"] = [whitePieces[5], "white"]
    board[f"D8"] = [whitePieces[4], "black"]
    board[f"E8"] = [whitePieces[5], "black"]

    # board["B3"] = ["p", "black"] # for cheking pawn attacking
    # board["A7"] = ["p", "white"] # for cheking pawn attacking

    for i in reversed(range(8)):
        print("{:>2}".format(f"{i+1}|"), end="")
        for j in lateral:
            square = board[f"{j}{i+1}"]
            if len(square) < 2:
                print("{:>4}".format(f"{square[0]}"), end="")
            else:
                if square[1] == "white":
                    print("{:>4}".format(f"{square[0]}"), end="")
                else:
                    print("{:>4}".format(f"{white_to_black.get(square[0])}"), end="")
                    # print("{:>4}".format(f"{square[0]}"), end="")
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
    hasWon = None
    if len(board[f"{movedPiece[1]}"]) == 2:
        print(f"You Took A {board[f"{movedPiece[0]}"][1].upper()}")
        if board[f"{movedPiece[1]}"][0] == whitePieces[5]:
            print("Check Mate!")
            hasWon = board[f"{movedPiece[0]}"][1]
            
    board[f"{movedPiece[1]}"] = board[f"{movedPiece[0]}"]
    board[f"{movedPiece[0]}"] = ["\u25A1"]
    print("Updated Board!!")

    for i in reversed(range(8)):
        print("{:>2}".format(f"{i+1}|"), end="")
        for j in lateral:
            square = board[f"{j}{i+1}"]
            if len(square) < 2:
                print("{:>4}".format(f"{square[0]}"), end="")
            else:
                if square[1] == "white":
                    print("{:>4}".format(f"{square[0]}"), end="")
                else:
                    print("{:>4}".format(f"{white_to_black.get(square[0])}"), end="")
                    # print("{:>4}".format(f"{square[0]}"), end="")
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
    
    if hasWon != None:
        print(f"Well done {hasWon}!")
        sys.exit()
        
    return

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
            if upgrade in whitePieces:
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
                if (len(board[f"{startPoint[0]}{int(startPoint[1])+1}"]) == 2 and color == "white"
                    ) or (len(board[f"{startPoint[0]}{int(startPoint[1])-1}"]) == 2 and color == "black"):
                    
                    print(f"Cannot jump past piece: {board[f"{startPoint[0]}{int(startPoint[1])+1}"]}")
                    return False
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
     
def diagonalMovement(startPoint, endPoint, board):
    possibleMoves = []
    piece = board[f"{startPoint[0]}{startPoint[1]}"]
    color = piece[1]
    
    # Create a for loop with the distances from out start to our end
    startingLateral = lateral.index(startPoint[0])
    isRight = startingLateral < lateral.index(endPoint[0])
    length = int(endPoint[1]) - int(startPoint[1])
    if length == 0:
        print("Must move vertically")
        return False
    
    incremental = 0
    for i in range(1, abs(length)+1):
        # would be by saying plus or minus from the start point each time throug the loop
        if length < 0:
            incremental -= 1
        else:
            incremental += 1
        if (int(startPoint[1]) + incremental > 8) or (int(startPoint[1]) + incremental < 1):
            break
        
        if isRight:
            if startingLateral >= 7:
                break
            startingLateral += 1
        else:
            if startingLateral <= 0:
                break
            startingLateral -= 1
        print(f"Making new square as position {lateral[startingLateral].upper()}{int(startPoint[1])+incremental}")
        square = board[f"{lateral[startingLateral]}{int(startPoint[1])+incremental}"]
        print(f"Checking out {square}")
        if len(square) == 2:
            if square[1] == color:
                print("Cannot move through your own piece")
                break
            else:
                possibleMoves.append(f"{lateral[startingLateral]}{int(startPoint[1])+incremental}")
                break
        possibleMoves.append(f"{lateral[startingLateral]}{int(startPoint[1])+incremental}")
    return possibleMoves
        # for j in range(lateral.index(startPoint[0]), lateral.index(endPoint[0])):    
                     
def bishopMovement(startPoint, endPoint, board):
    possibleMoves = diagonalMovement(startPoint, endPoint, board)
    if possibleMoves == False:
        return False
    if endPoint in possibleMoves:
        boardUpdate([startPoint, endPoint])
        return
    else:
        return False

def horizontalMovement(startPoint, endPoint, board):
    color = board[f"{startPoint}"][1]
    
    startChar = startPoint[0]
    startIndex = lateral.index(startChar)
    endChar = endPoint[0]
    endIndex = lateral.index(endChar)
    startInt = int(startPoint[1])
    endInt = int(endPoint[1])
    
    differenceChar = endIndex - startIndex
    differenceInt = endInt - startInt
    
    possibleMoves = []
    counter = 0
    if startChar == endChar:
        for i in range(1, abs(differenceInt)+1):
            if differenceInt < 0:
                counter -= 1
            else:
                counter += 1
            if (startInt + counter < 1) or (startInt + counter > 8):
                print("IT@S BROKENNN")
                print(f"This is the current broken counter {counter}")
                break
            square = board[f"{startChar}{startInt+counter}"]
            if len(square) == 2:
                if square[1] == color:
                    print("Cannot move into your own color")
                    return False
                else:
                    possibleMoves.append(f"{startChar}{startInt+counter}")
                    break
            possibleMoves.append(f"{startChar}{startInt+counter}")
            
    elif startInt == endInt:
        for i in range(0, abs(differenceChar)):
            if differenceChar < 0:
                counter -= 1
            else:
                counter += 1
            square = board[f"{lateral.__getitem__(startIndex+counter)}{startInt}"]
            if len(square) == 2:
                if square[1] == color:
                    print("Cannot move into your own color")
                    return False
                else:
                    possibleMoves.append(f"{lateral.__getitem__(startIndex+counter)}{startInt}")
                    break
            possibleMoves.append(f"{lateral.__getitem__(startIndex+counter)}{startInt}")
    else:
        print("Unable to move none horizontally for a Rook")
        return False
        
    return possibleMoves
            
def queenMovement(startPoint, endPoint, board):
    startChar = startPoint[0]
    startIndex = lateral.index(startChar)
    endChar = endPoint[0]
    endIndex = lateral.index(endChar)
    startInt = int(startPoint[1])
    endInt = int(endPoint[1])
    
    if (startInt == endInt) or (startChar == endChar):
        possibleMoves = horizontalMovement(startPoint, endPoint, board)
    else:
        possibleMoves = diagonalMovement(startPoint, endPoint, board)
    # possibleHorizontalMoves = horizontalMovement(startPoint, endPoint, board)
    # possibleDiagonalMoves = diagonalMovement(startPoint, endPoint, board)
    # if (possibleHorizontalMoves == False) or (possibleHorizontalMoves == False):
    #     return False
    if possibleMoves == False:
        return False
    
    for move in possibleMoves:
        print(move)
    
    if endPoint in possibleMoves:
        boardUpdate([startPoint, endPoint])
        return
    else:
        print("Not a valid Queen move")
        return False  
        
def kingMovement(startPoint, endPoint, board):
    startChar = startPoint[0]
    startIndex = lateral.index(startChar)
    endChar = endPoint[0]
    endIndex = lateral.index(endChar)
    startInt = int(startPoint[1])
    endInt = int(endPoint[1])
    
    differenceChar = endIndex - startIndex
    differenceInt = endInt - startInt
    
    if (abs(differenceInt) > 1) or (abs(differenceChar) > 1):
        return False
    
    boardUpdate([startPoint, endPoint])
    

def rookMovement(startPoint, endPoint, board):
    possibleMoves = horizontalMovement(startPoint, endPoint, board)
    if possibleMoves == False:
        return False
    if endPoint in possibleMoves:
        boardUpdate([startPoint, endPoint])
        return 
    else:
        return False

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
        if piece == whitePieces[0]:
            if pawnMovement(new_positions[0], new_positions[1], board, taking) == False:
                print("Pawn is unable to move to that position")
                continue
            else:
                return
        elif piece == whitePieces[1]:
            if knightMovement(new_positions[0], new_positions[1], board) == False:
                print("Knight is unable to move to that position")
                continue
            else:
                return
        elif piece == whitePieces[2]:
            if bishopMovement(new_positions[0], new_positions[1], board) == False:
                print("Bishop is unable to move to that position")
                continue
            else:
                return
        elif piece == whitePieces[3]:
            if rookMovement(new_positions[0], new_positions[1], board) == False:
                print("Rook is unable to move to that position")    
                continue  
            else:
                return      
        elif piece == whitePieces[4]:
           if queenMovement(new_positions[0], new_positions[1], board) == False:
                print("Queen is unable to move to that position")    
                continue
           else:
               return
        elif piece == whitePieces[5]:
            if kingMovement(new_positions[0], new_positions[1], board) == False:
                print("Queen is unable to move to that position")    
                continue
            else:
               return
        else:
            print("Somehow the selected piece is.... Not a piece? Weird, huh")


board = boardSetUp()
players = ["white", "black"]

print("Move with the notation: (Piece's Square), (Square Your Piece Will Move To) I.E -- D2, D4")

while (True):
    for i in range(0, 2):
        print(f"Player: {players[i]}")
        userMove(board, players[i])