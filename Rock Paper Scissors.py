from random import randint

t = ('Rock','Paper','Scissors')

computer = t[randint(0,2)]

player = False

x = 0

y = ('You win this round')

print('Welcome to the game')

print('Its first to three points')

print('Enter Rock, Paper or Scissors to make your move!')

while player == False:

    player = input('Rock,Paper,Scissors?')

    print('computer plays...')
    
    print(computer)
    
    if player == computer:
        print('Its a tie!')
        
    elif player == 'Rock' and computer == 'Scissors':
        print(y)
        x = x + 1
        
    elif player == 'Paper' and computer == 'Rock':
        print(y)
        x = x + 1
        
    elif player == 'Scissors' and computer == 'Paper':
        print(y)
        x = x + 1
        
    else:
        print('You lose this round')
        x = x - 1

    print('The score is...')

    print(x)

    if x == 3:
        print('Nice one, you won the game!')
        
    if x == -3:
        print('Unlucky, you lost the game')

    player = False

    computer = t[randint(0,2)]
