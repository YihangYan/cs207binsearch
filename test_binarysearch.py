import unitest
from pytest import raises
import numpy as np
from binarysearch import binary_search

def test_simple():
	assert binary_search([1,2,np.inf], 2) == 1