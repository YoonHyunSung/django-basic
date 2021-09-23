from dataclasses import dataclass
# Create your models here.
# from django.db import models

class Sorting(object):

    def bubble_sort(self):
        pass

    def merge_sort(self):
        pass

    def quick_sort(self):
        pass


@dataclass
class Palindrome(object):
    input_list : []
    @property
    def input_list(self) -> []: return self.input_list

    @input_list.setter
    def input_list(self, input_list): self.input_list = input_list

    def str_to_list(payload: str) -> []:

        return [i for i in payload if i.isalnum()]

    def isPalindrome(ls: []) -> bool:
        return {"RESULT": False for i in ls if ls.pop(0) != ls.pop()}

    def reverse_string(self):
        pass


@dataclass
class MySum(object):

    start_number: int
    end_number: int

    @property
    def start_number(self)-> int: return self._start_number

    @property
    def end_number(self) -> int: return self._end_number

    @start_number.setter
    def start_number(self, start_number): self._start_number = start_number

    @end_number.setter
    def end_number(self, end_number): self._end_number = end_number

    def one_to_ten_sum_1(self):
        sum = 0
        for i in range(self.start_number, self.end_number):
            sum += i
        return sum

    def one_to_ten_sum_2(self):
        return sum(i for i in range(self.start_number, self.end_number))

    def one_to_ten_sum_3(self):
        return sum(range(self.start_number, self.end_number))