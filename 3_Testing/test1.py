import unittest
import game1

class TestGame(unittest.TestCase):
    def test_input(self):
        answer=5
        guess=5
        result = game1.run_guess(answer,guess)
        self.assertTrue(result)

    def test_input_wrong_guess(self):
        result = game1.run_guess(5,0 )
        self.assertFalse(result)

    def test_input_wrong_number(self):
        result = game1.run_guess(11, 5)
        self.assertFalse(result)

    def test_input_wrong_type(self):
        result = game1.run_guess(5,'11')
        self.assertFalse(result)

if __name__ == '__main__':
    unittest.main()
    