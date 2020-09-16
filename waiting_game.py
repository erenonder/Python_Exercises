import time
import random


def waiting_game():

    wait_time = random.randint(2, 5)
    print(f'\nYour target wait time is {wait_time} seconds')
    pressed_button = None
    play = True
    while pressed_button != '' and play:
        pressed_button = input('---Press Enter to Begin (x to exit)---\n\n')
        if pressed_button == 'x':
            play = False

    if play:
        start_time = time.time()
        pressed_button = input(f'...Press Enter again after {wait_time} seconds...')
        if pressed_button == '':
            end_time = time.time()
            elapsed_time = end_time - start_time
            if elapsed_time > wait_time - 0.1 and elapsed_time < wait_time + 0.1:
                print(f'You won you pressed at {elapsed_time:.2f}')
            else:
                if elapsed_time < wait_time:
                    print(f'You were too fast {elapsed_time:.2f}')
                else:
                    print(f'You were too slow {elapsed_time:.2f}')
        else:
            print(f'You pressed a wrong button {pressed_button}')

        waiting_game()


if __name__ == '__main__':
    waiting_game()
