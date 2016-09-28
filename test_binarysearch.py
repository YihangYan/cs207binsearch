import unittest
from pytest import raises
import numpy as np
from binarysearch import binary_search

class MyTest(unittest.TestCase):

	
	# empty_list = []
	# one_element_list = [9]
	# sorted_num_list = list(range(15))
	# unsorted_num_list = [2, 6, 19, 3, 57, 32, -4]
	# combine_list = [3, 6, True, "combine", -2, "list"]
	'''
	Phase 1 - Simple test (interface illustration)
	'''
	def test_found(self):
		sorted_num_list = list(range(15))
		self.assertEqual(binary_search(sorted_num_list, 2), 2)

	def test_found2(self):
		sorted_num_list = list(range(15))
		self.assertEqual(binary_search(sorted_num_list, 6, 2, 7), 6)

	def test_notfound(self):
		sorted_num_list = list(range(15))
		self.assertEqual(binary_search(sorted_num_list, 9.5), -1)

	def test_notfound2(self):
		sorted_num_list = list(range(15))
		self.assertEqual(binary_search(sorted_num_list, 8, 2, 7), -1)

	'''
	Phase 2 - Test different input
	'''
	def test_emptylist(self):
		empty_list = []
		self.assertEqual(binary_search(empty_list, 6), -1)

	def test_oneelement(self):
		one_element_list = [9]
		self.assertEqual(binary_search(one_element_list, 9), 0)
	def test_one_element2(self):
		one_element_list = [9]
		self.assertEqual(binary_search(one_element_list, 2), -1)

	def test_unsorted_list(self):
		unsorted_num_list = [2, 6, 19, 3, 57, 32, -4]
		self.assertEqual(binary_search(unsorted_num_list, 3), 3)

	def test_combine_list(self):
		unsorted_num_list = [2, 6, 19, 3, 57, 32, -4]
		self.assertEqual(binary_search(unsorted_num_list, 6), -1)
	#If it is there multiple times, we will return one of them: it is 
	#not defined which, We are consistent by always returning an int, 
	#choosing one which cannot be an index.

	def test_multiple_same_elements(self):
		multiple_same_elements = [8, 43, 7, 43, 9, 21, 40, 21]
		self.assertEqual(binary_search(multiple_same_elements, 43), 2)
		self.assertEqual(binary_search(multiple_same_elements, 21), 5)



	#if we have a NaN in our array? Infty?
	def test_nan_list(self):
		nan_list = [2, 31, NaN, 7, 10]
		self.assertEqual(binary_search(nan_list, 7), 3)

	# what if da_array was not an array?

	def test_not_array(self):
		not_array = '1 3 e'
		self.assertEqual(binary_search(nan_list, NaN), 2)

	'''
	Phase 3 - Test Needles
	'''
	def test_needle_lessthan(self):
		sorted_num_list = list(range(15))
		self.assertEqual(binary_search(sorted_num_list, 4, 2, 14), 4)
		self.assertEqual(binary_search(sorted_num_list, 1, 2, 14), -1)

	def test_needle_morethan(self):
		sorted_num_list = list(range(15))
		self.assertEqual(binary_search(sorted_num_list, 12, 2, 10), -1)

	'''
	Phase 4 - Integration of previous test
	'''

suite = unittest.TestLoader().loadTestsFromModule(MyTest())
unittest.TextTestRunner().run(suite)