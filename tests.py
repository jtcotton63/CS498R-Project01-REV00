__author__ = 'Joseph Cotton'
__email__ = 'jtcotton63@gmail.com'

import unittest
from unrolled_linked_list import UnrolledLinkedList

'''
> Implement your tests here

To run your tests, just run `python tests.py`
'''


class Test(unittest.TestCase):
    """ Demonstrates how the unittest framework works """

    def test_example(self):
        # new_list = UnrolledLinkedList()
        # self.assertIsNotNone(new_list)
        pass

    def test_append(self):
    	test_list = UnrolledLinkedList(3)
    	test_list.append(0)
    	test_list.append(1)
    	test_list.append(2)
    	test_list.append(3)
    	test_list.append(4)
    	test_list.append(5)
    	assert 0 in test_list
    	assert 1 in test_list
    	assert 2 in test_list
    	assert 3 in test_list
    	assert 4 in test_list
    	assert 5 in test_list
    	assert 6 not in test_list
    	assert str(test_list) == "{[0,1,2], [3,4,5]}"



if __name__ == '__main__':
    unittest.main()

