def get_winner(player_one_move, player_two_move):
    
    winner = ''
    if player_one_move == player_two_move:
        winner = 'anyone. It was a tie'
    elif player_one_move == 'rock' and player_two_move == 'paper':
        winner = 'player two'
    elif player_one_move == 'rock' and player_two_move == 'scissor':
        winner = 'player one'
    if player_one_move == 'scissor' and player_two_move == 'paper':
        winner = 'player one'
    elif player_one_move == 'scissor' and player_two_move == 'rock':
        winner = 'player two'
    elif player_one_move == 'paper' and player_two_move == 'scissor':
        winner = 'player two'
    elif player_one_move == 'paper' and player_two_move == 'rock':
        winner = 'player one'

    return winner

def main():

    moves = ['paper', 'rock', 'scissor']

    while True:

        player_one_move = str(input('Player one, make your move \n'))
        if player_one_move not in moves:
            print('Invalid move. Use paper, rock or scissor. Try again! \n')
            continue

        player_two_move = str(input('Player two, Please make your move \n'))
        if player_two_move not in moves:
            print('Invalid move. Use paper, rock or scissor. Try again! \n')
            continue

        break
    
    print('the winner is: {}'.format(get_winner(player_one_move, player_two_move)))

if __name__ == '__main__':
    main()


    

        

        

