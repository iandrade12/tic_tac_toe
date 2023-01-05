from tic_tac_toe import draw_board, check_turn, check_for_win
import os

spots = {1 : '1', 2: '2', 3 : '3', 4 : '4', 5 : '5', 
        6 : '6', 7 : '7', 8 : '8', 9 : '9'}

playing = True
complete = False
turn = 0
prev_turn = -1

while playing:
    #reset the screen
    os.system('cls' if os.name == 'nt' else 'clear')
    draw_board(spots)
    #If an invalid turn occurred, let the player know
    if prev_turn == turn:
        print("Numero invalido, selecione outro ")
    prev_turn = turn
    print("\nJogador " + str((turn % 2) +1 ) + " Sua vez ")

    #get Input from the player
    choice = input()
    if choice == 'q':
        playing = False
    
    #check if the player gave a number from 1 - 9
    elif str.isdigit(choice) and int (choice) in spots:
        
        # check if the spot has already ben taken
        if not spots[int(choice)] in {"X", "O"}:
            
            # Valid input, update the board
            turn += 1
            spots[int(choice)] = check_turn(turn)

    #check if the game is ended
    if check_for_win(spots): playing, complete = False, True
    if turn > 8: playing = False




