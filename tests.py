import unittest
from unrolled_linked_list import UnrolledLinkedList

__author__ = 'Joseph Cotton'
__email__ = 'jtcotton63@gmail.com'

'''
> Implement your tests here

To run your tests, just run `python tests.py`
'''


class Test(unittest.TestCase):
    """ Demonstrates how the unittest framework works """

    def test_smoke_single_list(self):
        # Test modifying max_node_capacity parameter
        test_list = UnrolledLinkedList(3)

        # Test append
        test_list.append(0)
        test_list.append(1)
        test_list.append(2)
        test_list.append(3)
        test_list.append(4)
        test_list.append(5)

        # Test __contains__
        assert 0 in test_list
        assert 1 in test_list
        assert 2 in test_list
        assert 3 in test_list
        assert 4 in test_list
        assert 5 in test_list
        assert 6 not in test_list

        # Test __get__
        assert test_list[0] == 0
        assert test_list[1] == 1
        assert test_list[2] == 2
        assert test_list[3] == 3
        assert test_list[4] == 4
        assert test_list[5] == 5

        # Test __get__ negative index
        assert test_list[-1] == 5
        assert test_list[-2] == 4
        assert test_list[-3] == 3
        assert test_list[-4] == 2
        assert test_list[-5] == 1
        assert test_list[-6] == 0

        error_thrown1 = False
        try:
            assert test_list[-7]
        except IndexError:
            error_thrown1 = True
        assert error_thrown1 is True

        # Test __str__
        assert str(test_list) == "{[0], [1], [2], [3,4,5]}"

        # Test __set__
        test_list[-6] = 10
        test_list[1] = 11
        test_list[2] = 12
        test_list[3] = 13
        test_list[4] = 14
        test_list[5] = 15
        assert test_list[0] == 10
        assert test_list[1] == 11
        assert test_list[2] == 12
        assert test_list[3] == 13
        assert test_list[4] == 14
        assert test_list[5] == 15

        # Test error raising for __get__ function
        error_thrown1 = False
        try:
            temp = test_list['a']
        except TypeError:
            error_thrown1 = True
        assert error_thrown1 is True

        error_thrown1 = False
        try:
            temp = test_list[5000]
        except IndexError:
            error_thrown1 = True
        assert error_thrown1 is True

        # Test error raising for __set__ function
        error_thrown1 = False
        try:
            test_list['a'] == 350
        except TypeError:
            error_thrown1 = True
        assert error_thrown1 is True

        error_thrown1 = False
        try:
            test_list[5000] = -1
        except IndexError:
            error_thrown1 = True
        assert error_thrown1 is True

        # Test __len__
        assert len(test_list) is 6

        # Test delete
        del test_list[0]
        assert str(test_list) == "{[11], [12], [13,14,15]}"
        test_list.append(16)
        del test_list[1]
        # Make sure a middle node gets removed correctly
        assert str(test_list) == "{[11], [13], [14,15,16]}"
        del test_list[2]
        assert str(test_list) == "{[11], [13], [15,16]}"
        test_list.append(17)
        del test_list[4]
        assert str(test_list) == "{[11], [13], [15,16]}"
        del test_list[3]
        assert str(test_list) == "{[11], [13], [15]}"
        # Make sure the end node gets deleted
        del test_list[2]
        assert str(test_list) == "{[11], [13]}"

        # Test for arrays being de-allocated correctly
        assert len(test_list.head.next_node) == 1

        # Test deleting from end using negative indices
        del test_list[-2]
        assert str(test_list) == "{[13]}"
        del test_list[-1]
        assert str(test_list) == "{[]}"

        # Test error raising for __del__
        error_thrown1 = False
        try:
            del test_list['a']
        except TypeError:
            error_thrown1 = True
        assert error_thrown1 is True

        error_thrown1 = False
        try:
            temp = test_list[5000]
        except IndexError:
            error_thrown1 = True
        assert error_thrown1 is True

        # Test getting when the list is empty
        error_thrown1 = False
        try:
            temp = test_list[0]
        except IndexError:
            error_thrown1 = True
        assert error_thrown1 is True

    # def test_smoke_add_lists(self):
    #     one = UnrolledLinkedList(5)
    #     two = UnrolledLinkedList(5)
    #
    #     one.append(0)
    #     one.append(1)
    #     one.append(2)
    #     one.append(3)
    #     one.append(4)
    #     one.append(5)
    #
    #     two.append(10)
    #     two.append(11)
    #     two.append(12)
    #     two.append(13)
    #     two.append(14)
    #     two.append(15)
    #
    #     one += two
    #     assert str(one) == "{[0,1], [2,3], [4,5], [10,11], [12,13,14,15]}"
    #
    #     # Test error raising for __add__
    #
    #     print "Tests are finished"
    #
    # def test_smoke_mult(self):
    #     one = UnrolledLinkedList(5)
    #     one.append(0)
    #     one.append(1)
    #     one.append(2)
    #     one.append(3)
    #     one.append(4)
    #     one.append(5)
    #
    #     one *= 1
    #     assert str(one) == "{[0,1], [2,3,4,5]}"
    #
    #     one *= 4
    #     assert str(one) == "{[0,1], [2,3], [4,5], [0,1], [2,3], [4,5], [0,1], [2,3], [4,5], [0,1], [2,3,4,5]}"

    def test_smoke_iters(self):
        test_list = UnrolledLinkedList(16)
        for i in xrange(0, 16):
            test_list.append(i)

        # Forwards
        counter = 0
        for item in test_list:
            assert item == counter
            counter += 1

        # Reverse
        counter = 15
        for item in reversed(test_list):
            assert item == counter
            counter -= 1



















if __name__ == '__main__':
    unittest.main()

