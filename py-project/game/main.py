import random

options = ('rock', 'paper', 'scissors')

computer_score = 0
user_score = 0

rounds = 1

print()
print('Welcome to the rock, paper, scissors game!')
print('The first player to reach 5 points wins the game.')
print('Ready? Let\'s play!')


while True:
    print()
    print('*' * 8)
    print('ROUND', rounds)
    print('*' * 8)
    print()

    print('SCORES:')
    print('computer score: ', computer_score)
    print('your score: ', user_score)
    print('-' * 8)
      
    
    user_option = input('Rock, paper or scissors => ')
    user_option = user_option.lower()

    rounds += 1

    if not user_option in options:
      print('This is not a valid option, please try it again.')
      continue

    computer_option = random.choice(options)

    print('Your option => ', user_option)
    print('Computer option => ', computer_option)
    print()

    if user_option == computer_option:
      print('It\'s a tie! 😬')
    elif user_option == 'rock':
      if computer_option == 'scissors':
        print('Rock crushes scissors')
        print('You won!')
        user_score += 1
      else:
        print('Paper covers rock')
        print('Computer won!')
        computer_score += 1
    elif user_option == 'paper':
      if computer_option == 'rock':
        print('Paper covers rock')
        print('You won!')
        user_score += 1
      else:
        print('Scissors cuts paper')
        print('Computer won!')
        computer_score += 1
    elif user_option == 'scissors':
      if computer_option == 'paper':
        print('Scissors cuts paper')
        print('You won!')
        user_score += 1
      else: 
        print('Rock crushes scissors')
        print('Computer won!')
        computer_score += 1

    if computer_score == 5:
      print()
      print('Computer got 5 points and won the game! 🤖')
      print()
      break
  
    if user_score == 5:
      print()
      print('Congratulations! You got 5 points and won the game! 🎉')
      print()
      break
    
    