
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


## ==========================reapeated word  2 
def correct_repeated_word(string): 
    reg = re.findall('[\w\']+',string.lower()) 
    words = []
    repeated = ""
    for i in reg: 
        if i in words: 
            repeated = i
            break
        words.append(i) 
    return repeated

class RepeatedWord(unittest.TestCase):
    def test_repeated_word1(self):
        excepted = "a"
        string = "Once upon a time, there was a brave princess who..."
        actual = correct_repeated_word(self)
        assert actual == excepted

    def test_repeated_word2(self):
        excepted = "it"
        string = "It was the best of times, it was the worst of times, it was the age of wisdom, it was the age of foolishness, it was the epoch of belief, it was the epoch of incredulity, it was the season of Light, it was the season of Darkness, it was the spring of hope, it was the winter of despair, we had everything before us, we had nothing before us, we were all going direct to Heaven, we were all going direct the other way – in short, the period was so far like the present period, that some of its noisiest authorities insisted on its being received, for good or for evil, in the superlative degree of comparison only..."
        actual = correct_repeated_word(string)
        assert actual == excepted

    def test_repeated_word3(self):
        excepted = "summer" 
        string = "It was a queer, sultry summer, the summer they electrocuted the Rosenbergs, and I didn’t know what I was doing in New York..."
        actual = correct_repeated_word(string)
        assert actual == excepted


## ==========================insertion Sort  3
def correct_insertion_sort(arr):
    for i in range(1, len(arr)):
        current_value = arr[i]
        current_position = i

        while current_position > 0 and arr[current_position - 1] > current_value:
            arr[current_position] = arr[current_position -1]
            current_position = current_position - 1

        arr[current_position] = current_value 

class InsertionSort(unittest.TestCase):
    def test_insertion_sort_integers_values_one(self):
        expected = [4, 8, 15, 16, 23, 42]
        actual = correct_insertion_sort([8,4,23,42,16,15])
        assert actual == expected
    def test_insertion_sort_reverse_sorted(self):
        assert correct_insertion_sort([20,18,12,8,5,-2]) == [-2, 5, 8, 12, 18, 20]

    def test_few_uniques(self):
        assert correct_insertion_sort([5,12,7,5,5,7]) == [5, 5, 5, 7, 7, 12]

 

## ==========================merge Sort  4
def correct_merge_sort(arr):
    n = len(arr)
    if n > 1:
        mid = n//2
        left = arr[0:mid]
        right = arr[mid:n]
        correct_merge_sort(left)
        correct_merge_sort(right)

        i = 0
        j = 0
        k = 0
        while i < len(left) and j < len(right):

            if left[i] <= right[j]:
              arr[k] = left[i]
              i += 1
            else:
                arr[k] = right[j]
                j += 1
            k += 1
        while i < len(left):
            arr[k] = left[i]
            i += 1
            k += 1
 
        while j < len(right):
            arr[k] = right[j]
            j += 1
            k += 1

    return arr

class MergeSortIntegers(unittest.TestCase):
    def test_merge_sort_integers(self):
        expected = [4, 8, 15, 16, 23, 42]
        actual = correct_merge_sort([8,4,23,42,16,15])
        assert actual == expected
        
    def test_empty_list(self):
        array = []
        correct_merge_sort([])
        expected = []
        assert array == expected

    def test_one_item_list(self):

        array = [5]
        correct_merge_sort(array)
        expected = [5]
        assert array == expected

    def test_two_item_list():
        array = [5,2]
        correct_merge_sort(array)
        expected = [2,5]
        assert array == expected

    def test_many_item_list():
        array = [1,5,2,-4,88]
        correct_merge_sort(array)
        expected = [-4, 1, 2, 5, 88]
        assert array == expected

## ========================== binary Search List 5
def correct_binary_search(arr,key):
  mid = 0
  start = 0
  end = 0
  for i in arr:
    end+=1
  if key > arr[end-1]:
    return -1
  else:
    while (start <= end):
        mid = (start + end) // 2
        if key == arr[mid]:
            return mid

        if key < arr[mid]:
            end = mid - 1
        else:
            start = mid + 1
  return -1

class BinarySearch(unittest.TestCase):
    def test_binary1(self):
        actual = correct_binary_search([4,8,15,16,23,42], 15)
        expected = 2
        assert actual == expected
    def test_binary2(self):
        actual = correct_binary_search([11,22,33,44,55,66,77], 90)
        expected = -1
        assert actual == expected
    def test_binary3(self):
        actual = correct_binary_search([1, 2, 3, 5, 6, 7], 4)
        expected = -1
        assert actual == expected

## ========================== Shift List 6
def correctinsertShiftList(arr, int):
  i=0
  for n in arr:
    i+=1
  if i>1:
      new_arr = arr[:i//2] + [int] + arr[i//2:]
  else:
     new_arr = arr + [int]
  return new_arr


class ShiftList(unittest.TestCase):
    def test1(self):
        actual = correctinsertShiftList([1, 2, 3, 4],5)
        expected = [1, 2, 5, 3, 4]
        assert actual == expected

    def test2(self):
        actual = correctinsertShiftList([5, 5, 5, 5, 5, 5], 4)
        expected = [5,5,5,4,5,5,5]
        assert actual == expected

    def test3(self):
        actual = correctinsertShiftList([10, 20, 30],60)
        expected = [10,60,20,30]
        assert actual == expected

    def test4(self):
        actual = correctinsertShiftList([1], 2)
        expected = [1, 2]
        assert actual == expected


"""if __name__ == "__main__":
	unittest.main()"""
