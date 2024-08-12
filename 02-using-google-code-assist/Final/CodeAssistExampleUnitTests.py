import unittest
import random
import datetime
from CodeAssistExampleProgram import generate_random_list, calculate_age

class TestCodeAssistExampleProgram(unittest.TestCase):

    def test_generate_random_list_length(self):
        """Test if the generated list has the correct length."""
        length = 5
        random_list = generate_random_list(length)
        self.assertEqual(len(random_list), length)

    def test_generate_random_list_range(self):
        """Test if all numbers in the list are within the specified range."""
        length = 10
        random_list = generate_random_list(length)
        for number in random_list:
            self.assertTrue(1 <= number <= 100)

    def test_calculate_age_valid_birthdate(self):
        """Test age calculation with a valid birthdate."""
        birthdate = datetime.date(1990, 1, 1)
        age = calculate_age(birthdate)
        # Assuming current year is 2024 for testing
        expected_age = 2024 - 1990 - ((datetime.date.today().month, datetime.date.today().day) < (1, 1))
        self.assertEqual(age, expected_age)

    def test_calculate_age_future_birthdate(self):
        """Test age calculation with a future birthdate."""
        birthdate = datetime.date(2030, 1, 1)
        age = calculate_age(birthdate)
        self.assertEqual(age, 0)  # Age should be 0 for a future birthdate

if __name__ == '__main__':
    unittest.main()
