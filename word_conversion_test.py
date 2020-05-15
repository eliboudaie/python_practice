from word_conversion import word_check

import unittest

class WordCheckTest(unittest.TestCase):
    def test_same(self):
        self.assertTrue(word_check('abc', 'abc'))

    def test_one_different(self):
        self.assertTrue(word_check('abc', 'abd'))

    def test_wrong_length(self):
        self.assertFalse(word_check('abc', 'ad'))

    def test_wrong(self):
        self.assertFalse(word_check('dad', 'abc'))
    def test_true_repeating(self):
        self.assertTrue(word_check('abc', 'dad'))

if __name__ == '__main__':
    unittest.main()
