#import unitest
from pytest import raises
import numpy as np
from binarysearch import binary_search

empty_list = []
sorted_num_list = list(range(15))
combine_list = [3, 6, True, "combine", -2, "list"]
'''
Phase 1 - Simple test (interface illustration)
'''
def test_found():
	assert binary_search(sorted_num_list, 2) == 2

def test_found2():
	assert binary_search(sorted_num_list, 6, 2, 7) == 6

def test_notfound():
	assert binary_search(sorted_num_list, 9.5) == -1

def test_notfound2():
	assert binary_search(sorted_num_list, 8, 2, 7) == -1

'''
Phase 2 - Test different input
'''


'''
Phase 3 - Test Needles
'''


'''
Phase 4 - Integration of previous test
'''