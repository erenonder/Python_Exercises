import random

min_val = 1
max_val = 20

play_str = input(f'I have a number in between {min_val} and {max_val}. Would you like to play (yes/no)?')
guess = -1
if play_str == 'yes':
    num = random.randint(min_val, max_val)

    while num != guess:
        try:
            guess = int(input('What is your guess: '))
        except ValueError:
            print('This is not a number, I quit')
            break
        else:
            if num != guess:
                status = 'higher' if guess > num else 'lower'
                print(f'Your number is {status}')
                print('One more guess')
            else:
                print('That is right')
