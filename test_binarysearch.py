import unittest
from pytest import raises
import numpy as np
from binarysearch import binary_search

class MyTest(unittest.TestCase):

	
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
		self.assertEqual(binary_search(multiple_same_elements, 43), 3)
		#self.assertEqual(binary_search(multiple_same_elements, 21), 5)


	def test_nan_list(self):
		nan_list = [2, 3, np.NaN, 7, 10]
		self.assertEqual(binary_search(nan_list, 3), 2)
		#self.assertEqual(binary_search(nan_list, 7,3,4), 3)
		#self.assertEqual(binary_search(nan_list, 7), 2)
		#try:
			#self.assertEqual(binary_search(nan_list, 7), 3)
		#except:
			#print("The array can't contain NaN")
	def test_nan_list2(self):
		nan_list = [2, 3, np.NaN, 7, 10]
		self.assertEqual(binary_search(nan_list, 7,3,4), 3)
		#self.assertEqual(binary_search(nan_list, 7), 2)

	def test_nan_list3(self):
		nan_list = [2, 3, np.NaN, 7, 10]
		self.assertEqual(binary_search(nan_list, 7), 2)

	def test_inifinity(self):
		infty_list = [1, 2, np.inf, 5, 6]
		self.assertEqual(binary_search(infty_list, 2), 1)
		#self.assertEqual(binary_search(infty_list, 5), -1)

	def test_inifinity2(self):
		infty_list = [1, 2, np.inf, 5, 6]
		self.assertEqual(binary_search(infty_list, 5), -1)


	def test_not_array(self):
		not_array = '1 e 3'
		try:
			self.assertEqual(binary_search(not_array, 3), 2)
		except:
			print("Input needs to be an array")

	'''
	Phase 3 - Test Needles
	'''
	def test_needle_lessthan(self):
		sorted_num_list = list(range(15))
		self.assertEqual(binary_search(sorted_num_list, 4, 2, 14), 4)
		self.assertEqual(binary_search(sorted_num_list, 1, 2, 14), -1)

	def test_needle_lessthan2(self):
		sorted_num_list = list(range(15))
		self.assertEqual(binary_search(sorted_num_list, 1, 2, 14), -1)

	def test_needle_morethan(self):
		sorted_num_list = list(range(15))
		self.assertEqual(binary_search(sorted_num_list, 12, 2, 10), -1)

	'''
	Phase 4 - Integration of previous test
	'''

	# What if we have NaN in unsorted list?
	def test_nan_unsorted_list(self):
		nan_list = [3, 2, np.NaN, 7, 10]
		self.assertEqual(binary_search(nan_list, 2), 2)
		#self.assertEqual(binary_search(nan_list, 7,3,4), 3)
		#self.assertEqual(binary_search(nan_list, 7), 2)
		#try:
			#self.assertEqual(binary_search(nan_list, 7), 3)
		#except:
			#print("The array can't contain NaN")

	def test_nan_unsorted_list2(self):
		nan_list = [3, 2, np.NaN, 7, 10]
		self.assertEqual(binary_search(nan_list, 7,3,4), 3)
		#self.assertEqual(binary_search(nan_list, 7), 2)

	def test_nan_unsorted_list3(self):
		nan_list = [3, 2, np.NaN, 7, 10]
		self.assertEqual(binary_search(nan_list, 7), 2)

	#def 

suite = unittest.TestLoader().loadTestsFromModule(MyTest())
unittest.TextTestRunner().run(suite)