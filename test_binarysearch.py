import unittest
from pytest import raises
import numpy as np
from binarysearch import binary_search

class MyTest(unittest.TestCase):

	def testcase(self):
		self.empty_list = []
		self.one_element_list = [9]
		self.sorted_num_list = list(range(15))
		self.unsorted_num_list = [2, 6, 19, 3, 57, 32, -4]
		self.combine_list = [3, 6, True, "combine", -2, "list"]
	'''
	Phase 1 - Simple test (interface illustration)
	'''
	def test_found(self):
		self.assertEqual(binary_search(self.sorted_num_list, 2), 2)

	def test_found2(self):
		self.assertEqual(binary_search(self.sorted_num_list, 6, 2, 7), 6)

	def test_notfound(self):
		self.assertEqual(binary_search(self.sorted_num_list, 9.5), -1)

	def test_notfound2(self):
		self.assertEqual(binary_search(self.sorted_num_list, 8, 2, 7), -1)

	'''
	Phase 2 - Test different input
	'''
	def emptylist():
		self.assertEqual(binary_search(empty_list, 6), -1)

	def oneelement():
		self.assertEqual(binary_search(one_element_list, 9), 0)
	def oneelement2():
		self.assertEqual(binary_search(one_element_list, 2), -1)

	def unsortedlist():
		self.assertEqual(binary_search(unsorted_num_list, 3), -1)

	def combinelist():
		self.assertEqual(binary_search(unsorted_num_list, 6), -1)

	'''
	Phase 3 - Test Needles
	'''
	def needlelessthan():
		self.assertEqual(binary_search(sorted_num_list, 4, 2, 14), 2)
		self.assertEqual(binary_search(sorted_num_list, 1, 2, 14), -1)

	def needlemorethan():
		self.assertEqual(binary_search(sorted_num_list, 12, 2, 10), -1)

	'''
	Phase 4 - Integration of previous test
	'''

suite = unittest.TestLoader().loadTestsFromModule(MyTest())
unittest.TextTestRunner().run(suite)