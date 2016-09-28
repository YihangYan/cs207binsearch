#import unitest
from pytest import raises
import numpy as np
from binarysearch import binary_search

empty_list = []
one_element_list = [9]
sorted_num_list = list(range(15))
unsorted_num_list = [2, 6, 19, 3, 57, 32, -4]
combine_list = [3, 6, True, "combine", -2, "list"]
'''
Phase 1 - Simple test (interface illustration)
'''
def test_found():
	assert binary_search(sorted_num_list, 2) == 2

def test_found2():
	assert binary_search(sorted_num_list, 6, 2, 7) == 5

def test_notfound():
	assert binary_search(sorted_num_list, 9.5) == -1

def test_notfound2():
	assert binary_search(sorted_num_list, 8, 2, 7) == -1

'''
Phase 2 - Test different input
'''
def emptylist():
	assert binary_search(empty_list, 6) == -1

def oneelement():
	assert binary_search(one_element_list, 9) == 0
def oneelement2():
	assert binary_search(one_element_list, 2) == -1

def unsortedlist():
	assert binary_search(unsorted_num_list, 3) == -1

def combinelist():
	assert binary_search(unsorted_num_list, 6) == -1

'''
Phase 3 - Test Needles
'''
def needlelessthan():
	assert binary_search(sorted_num_list, 4, 2, 14) == 2
	assert binary_search(sorted_num_list, 1, 2, 14) == -1

def needlemorethan():
	assert binary_search(sorted_num_list, 12, 2, 10) == -1

'''
Phase 4 - Integration of previous test
'''