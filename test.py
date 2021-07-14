from solution import *
import re
import unittest
import random
def correct_fib(n):
	"""correct implementation for this test"""
	if n == 2:
		return 1
	elif n == 1:
		return 0
	else:
		return correct_fib(n-1) + correct_fib(n-2)
### help function for the nth
def random_num(n):
	return random.choice([i for i in range(n+1)])
def random_str(n):
	ans = ""
	for i in range(n):
		ans += random.choice(string.ascii_letters)
	return ans
class NthFib(unittest.TestCase):
	def test_1(self):
		"""Test for fib when n = 2"""
		assert 1 == nth_fib(2)
	def test_2(self):
		"""Test for fib when n = 6"""
		assert 5 == nth_fib(6)
	def test_3(self):
		num = random_num(15)
		"""random test 1, expected {num}, actual {nth_fib(num)}"""
		assert correct_fib(num) == nth_fib(num)
	def test_4(self):
		num = random_num(15)
		"""random test 2, expected {num}, actual {nth_fib(num)}"""
		assert correct_fib(num) == nth_fib(num)
	def test_5(self):
		num = random_num(15)
		"""random test 3, expected {num}, actual {nth_fib(num)}"""
		assert correct_fib(num) == nth_fib(num)
	def test_6(self):
		num = random_num(15)
		"""random test 4, expected {num}, actual {nth_fib(num)}"""
		assert correct_fib(num) == correct_fib(num)
	def test_7(self):
		num = random_num(15)
		"""random test 5, expected {num}, actual {nth_fib(num)}"""
		assert correct_fib(num) == nth_fib(num)