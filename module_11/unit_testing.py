# Unit Testing M11 Activity

from functions import *
import unittest

class TestRemoveVowels(unittest.TestCase):
    def test_remove_vowels(self):
        self.assertEqual(remove_vowels("HAI"), "H")
        self.assertEqual(remove_vowels("hello"), "hll")
        self.assertEqual(remove_vowels("Pikachu"),"Pkch")
        self.assertEqual(remove_vowels("gigi"), "gg")
        self.assertEqual(remove_vowels("123"), "123")
        self.assertEqual(remove_vowels("try"), "try")

class TestPrime(unittest.TestCase):
    def test_is_prime(self):
        # negative numbers are NOT prime
        self.assertFalse(is_prime(1))
        self.assertFalse(is_prime(-3))
        self.assertTrue(is_prime(5))
        self.assertTrue(is_prime(17))
        self.assertFalse(is_prime(-21))
        self.assertFalse(is_prime(20))
        self.assertTrue(is_prime(23))


if __name__ == '__main__':
    unittest.main()
