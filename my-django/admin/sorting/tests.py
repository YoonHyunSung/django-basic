from django.test import TestCase
import unittest
# Create your tests here.
# import sys
# sys.path.append('/admin/sorting')
from admin.sorting.models import MySum, Palindrome


class TestMySum(unittest.TestCase):

    def test_one_to_ten_sum_1(self):
        instance = MySum()
        instance.start_number = 1
        instance.end_number = 11
        res = instance.one_to_ten_sum_2()
        print(f'My Expected Value is {res}')
        self.assertEqual(res, 55)

class TestPalindrome(unittest.TestCase):

    def test_str_to_list(self):
        print(f'{Palindrome.str_to_list("A man, a plan, a canal: Panama")}')
        Palindrome.input_list = Palindrome.str_to_list("A man, a plan, a canal: Panama")
        plist = Palindrome.input_list
        self.assertEqual(plist[0], 'A')
    def test_isPalindrome(self):
        Palindrome.input_list = Palindrome.str_to_list("A man, a plan, a canal: Panama")
        dict = Palindrome.isPalindrome(Palindrome.input_list)
        print(f'test_isPalindrome : {dict["RESULT"]}')
if __name__ == '__main__':
    unittest.main()

