player1 = input("player 1 what is your name: ")
player2 = input("player 2 what is your name: ")
while True:

    player1 = input((player1) + ", please choose Rock, Paper or Scissors (r/p/s): ")
    player2 = input((player2) + ", please choose Rock, Paper or Scissors (r/p/s): ")
    if player1 == 'r' and player2 == 's' or player1 == 's' and player2== 'p' or player1 == 'p' and player2 == 'r':
        print("congratulations to the winner player1"+player1)
    elif player2 == 'r' and player1 == 's' or player2 == 's' and player1 == 'p' or player2 == 'p' and player1 == 'r':
        print("congratulations to the winner player2"+player2)
    elif player2 == 'r' and player1 == 'r' or player2 == 'p' and player1 == 'p' or player2 == 's' and player1 == 's':
        print("Draw")
    else:
        print("you have picked a wrong choice")
    playgame = input("want to start a new game?(Y/N)")
    if playgame != "Yes":
        break
