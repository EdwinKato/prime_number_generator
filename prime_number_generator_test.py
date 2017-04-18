import unittest
import prime_number_generator as prime_numbers

class PrimeTest(unittest.TestCase):
    """Class to test the prime number generator function"""
    
    def setUp(self):
        self.result = prime_numbers.generate_prime_numbers(10)

    def test_correct_result(self):
        self.assertEqual(self.result, [2, 3, 5, 7])

    def test_negative_numbers(self):
        for number in self.result:
            self.assertGreater(number, 0)

    def test_that_return_type_is_list(self):
        self.assertIsInstance(self.result, list)


if __name__ == '__main__':
    unittest.main()