import random

def init_game():
    print("Hello Welcome to Tic Tac Toe Game")
    User_choice = input("Choose which one you want 'X' or 'O': ").upper()
    return User_choice

def print_board(game_board):
    for i in range(9):
        print(f" {game_board[i]} ", end="")

        if i % 3 != 2:
            print("|", end="")
        else:
            print()
            if i != 8:
                print("-----------")

def check_draw(game_board):
    if ' ' not in game_board:
        return True
    return False       

def check_win(game_board , user):
    win_conditions = [
        [0, 1, 2], [3, 4, 5], [6, 7, 8], # Horizontal
        [0, 3, 6], [1, 4, 7], [2, 5, 8], # Vertical
        [0, 4, 8], [2, 4, 6]             # Diagonal
    ]

    for condition in win_conditions:
        # Check if all three indices in a condition match the user
        if game_board[condition[0]] == game_board[condition[1]] == game_board[condition[2]] == user:
            return True
            
    return False


def update_game(user_posi , game_board , user_choice):
    game_board[user_posi] = user_choice
    return game_board




user_choice = init_game()
if user_choice == 'X':
    bot_choice = 'O'
else:
    bot_choice = 'X'
game_board = [' ',' ',' ',' ',' ',' ',' ',' ',' ']
print_board(game_board)
current_choice = user_choice
while True:
    if current_choice == user_choice:
        user_posi = int(input("Enter the position you want to choose: "))
        if 1<=user_posi<=9 and game_board[user_posi - 1] == ' ':
            game_board = update_game(user_posi - 1 , game_board , user_choice)
            print_board(game_board)
        else:
            print("Please enter a correct Position")
            continue
        is_draw = check_draw(game_board)
        is_win = check_win(game_board , current_choice)

        if is_win == True:
            print("It's a Lose Sorry Bot wins!!")
            break
        elif is_draw == True:
            print("It's a Draw!!!")
            break
        
        else:
            current_choice = bot_choice
    else:
        print("\n\nBOT turn")
        bot_posi = random.randint(1,9)
        while game_board[bot_posi-1] != ' ':
            bot_posi = random.randint(1,9)
        game_board = update_game(bot_posi - 1 , game_board , current_choice)
        print_board(game_board)
        is_draw = check_draw(game_board)
        is_win = check_win(game_board , current_choice)

        if is_win == True:
            print("It's a Lose Sorry Bot wins!!")
            break
        elif is_draw == True:
            print("It's a Draw!!!")
            break
        
        else:
            current_choice = user_choice



    







    

    

    
        
