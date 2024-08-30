import unittest
from MyFirstCodeAssist import generate_random_list

class TestGenerateRandomList(unittest.TestCase):

    def test_list_length(self):
        """Verify that the function returns a list of the correct length."""
        n = 10
        numbers = generate_random_list(n)
        self.assertEqual(len(numbers), n)

    def test_elements_within_range(self):
        """Verify that all elements in the list are within the specified range."""
        n = 15
        min_val = 1
        max_val = 100
        numbers = generate_random_list(n)
        for number in numbers:
            self.assertTrue(min_val <= number <= max_val)

if __name__ == '__main__':
    unittest.main()
