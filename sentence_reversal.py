import unittest

def reverse_sentence(given_sentence):

    word_list = given_sentence.split()

    word_list.reverse()

    return " ".join(word_list)


class TestSentenceReverse(unittest.TestCase):
    def test_sentence_reverse(self):
        self.assertEqual(reverse_sentence('    space before'), 'before space')
        self.assertEqual(reverse_sentence('space after     '), 'after space')
        self.assertEqual(reverse_sentence('   Hello John    how are you   '), 'you are how John Hello')


if __name__ == "__main__":
    unittest.main()
