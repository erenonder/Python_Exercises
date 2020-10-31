import time
import random


class Game:

    def __init__(self):
        self.start_game()

    @staticmethod
    def read_random_sentence():

        with open('sentence_file.txt', 'r') as f:
            file_content = f.read()
            # print(file_content)

        sentence_list = file_content.split('\n')

        random_sentence = ''
        while random_sentence == '':
            sentence_index = random.randint(0, len(sentence_list) - 1)
            random_sentence = sentence_list[sentence_index]

        return random_sentence

    @staticmethod
    def calculate_accuracy(input_text, output_text):
        points = 0
        input_words = input_text.split()
        output_words = output_text.split()

        for word in input_words:
            if word in output_words:
                points += 1
            else:
                pass

        accuracy = points / len(input_words) * 100
        return accuracy

    @staticmethod
    def calculate_wpm(output_text, duration):

        word_count = 0
        for word in output_text.split():
            word_count += 1

        wpm = (60 / duration) * word_count

        return int(wpm)

    def start_game(self):

        string_to_type = Game.read_random_sentence()
        start_time = time.time()
        typed_text = input(f'Type this: {string_to_type}\n')
        end_time = time.time()
        duration = end_time - start_time

        accuracy_percentage = Game.calculate_accuracy(
            string_to_type, typed_text)

        print(
            f'Typed in {duration:.3f} seconds and with %{accuracy_percentage:.2f} accuracy')

        wpm = Game.calculate_wpm(typed_text, duration)
        print(f'You type {wpm} words per minute')


if __name__ == '__main__':
    game = Game()
