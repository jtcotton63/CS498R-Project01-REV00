__author__ = 'Joseph Cotton'
__email__ = 'jtcotton63@gmail.com'

import math

class UnrolledLinkedList(object):

    """ NODE CLASS """

    class Node(object):
        def __init__(self):
            self.array = []
            self.next_node = None

        def get_next_node(self):
            return self.next_node

        def set_next_node(self, next_node):
            self.next_node = next_node

        def get_value_at_index(self, index):
            return self.array[index]

        def set_value_at_index(self, index, value):
            self.array[index] = value

        def __len__(self):
            return len(self.array)

        def __contains__(self, value):
            if value in self.array:
                return True
            else:
                return False

        def is_array_full(self):
            return len(self.array) == UnrolledLinkedList.max_node_capacity



    def __init__(self, max_node_capacity=16):
        self.max_node_capacity = max_node_capacity
        self.head = self.Node()

    """ BASIC """

    def append(self, data):
        """ Add a new object to the end of the list.

        This adds a new object, increasing the overall size of the list by 1.

        RULES FOR APPENDING (paraphrased from Wikipedia):
        To insert a new element, we simply find the node the element should be
        in and insert the element into the elements array, incrementing
        the size of the list. If the array is already full, we first insert a
        new node either preceding or following the current one and move half of
        the elements in the current node into it.

        Usage: `my_list.append(4)`

        Args:
            data: The new object to be added to the list

        Returns:
            nothing

        """
        last_node = self.find_last_node()
        if last_node.is_array_full():
            temp = self.Node()
            # TODO What happens when max_node_capacity is 1 or 2 ???
            if self.max_node_capacity == 1:
                temp.set_value_at_index(self, 0, data)
                # TODO Delete from old array
            elif self.max_node_capacity == 2:
                temp.set_value_at_index(self, 0, data)
                # DO NOT NEED TO DELETE FROM OLD ARRAY
            else:
                middle = math.floor(len(last_node)/2)
                temp.array.extend(last_node.array[middle:])
                # TODO Delete from old array
            last_node.set_next_node(self, temp)
        else:
            last_node.array.append(self, data)

    def __getitem__(self, index):
        """ Access the element at the given index.

        The indexes of an unrolled linked list refers to the total collection
        of the list. i.e. in {[1, 2, 3], [5, 4, 1]}, index @ 1 refers to the
        value 2. Index @ 4 refers to the value 4, even though it is in another
        node.

        This function should support negative indices, which are natural to
        Python. For example, getting at index -1 should return the last
        element, index -2 should be the second-to-last element and so on.

        Usage: `my_list[4]`

        BONUS: Allow this to work with slices. The resulting structure should
        be a new balanced unrolled linked list.
        For example,
        my_list = {[1, 2, 6], [9, 6, 1], [0, 8, 1], [8, 2, 6]}
        then my_list[4:10] should be {[6, 1, 0], [8, 1, 8, 2, 6]}

        Args:
            index: An int value indicating an index in the list.

        Returns:
            The object held at the given `index`.

        Raises:
            TypeError: If index is not an `int` object.
            IndexError: If the index is out of bounds.

        """
        items_node, items_index_in_node_array = self.get_node_with_data_at_index(self.head, index)
        return items_node.array[items_index_in_node_array]
        


        

    def __setitem__(self, index, value):
        """ Sets the item at the given index to a new value

        Usage: `my_list[5] = "my new value"`

        BONUS: Allow this to work with slices. You should *only* be able to
        assign another unrolled linked list. Upon doing so, you should
        rebalance the list. For example, if your node max capacity is 5, and
        your list is:
        my_list = {[1, 2, 6], [9, 6, 1], [0, 8, 1], [8, 2, 6]}
        and you have another list with a different max capacity:
        other_list = {[3, 6], [8, 4]},
        and you use `my_list[0:2] = other_list` the result should be
        {[3, 6, 8, 4, 6], [9, 6, 1], [0, 8, 1], [8, 2, 6]}
        which is acceptable since the max capacity is 5. Node 0 did not go over

        Args:
            index: The index of the list which should be modified.
            value: The new value for the list at the given index.

        Returns:
            none - this is a void function and should mutate the data structure
                in-place.

        Raises:
            TypeError: If index is not an `int` object.
            IndexError: If the index is out of bounds.
        """
        items_node, items_index_in_node_array = self.get_node_with_data_at_index(self.head, index)
        items_node.set_value_at_index(self, items_index_in_node_array, value)

    def __delitem__(self, index):
        """ Deletes an item using the built-in `del` keyword

        This function should support negative indices, which are natural to
        Python. For example, deleting at index -1 should delete the last
        element, index -2 should be the second-to-last element and so on.

        RULES FOR DELETING (paraphrased from Wikipedia):
        To remove an element, we simply find the node it is in and delete it
        from the elements array, decrementing numElements. If this reduces the
        node to less than half-full, then we move elements from the next_node
        to fill it back up above half. If this leaves the next_node less than
        half full, then we move all its remaining elements into the current
        node, then bypass and delete it.

        BONUS: Allow this to delete using slices as well as indices
        (http://stackoverflow.com/questions/12986410/how-to-implement-delitem-to-handle-all-possible-slice-scenarios)

        Usage: `del my_list[4]`

        Args:
            index: An `int` value indicating the index of the item you are
                deleting.

        Returns:
            none - this is a void function that should mutate the data
                structure in-place, not return a new data structure.

        Raises:
            TypeError: If index is not an `int` object.
            IndexError: If the index is out of bounds.
        """
        







    """ HELPER """

    def find_last_node(self):
        if not hasattr(self.head, 'next_node'): # Make sure this syntax is correct
            return self.head
        return self.find_last_node_recur(self.head)

    def find_last_node_recur(self, curr_node):
        if not hasattr(curr_node, 'next_node'):
            return curr_node
        return self.find_last_node_recur(curr_node.next_node)
        pass

    def get_node_with_data_at_index(self, curr_node, index):
        """ This function finds the node with the data at the specified index relative
            the entire list
        
            Ex: Calling get_node_with_data_at_index(head, 3) on this example array 
            {[1,2,3],[5,4,1]} returns a pointer to the second node and the number 0
            (the index of the desired item in the array of the node).
        
            Throws an IndexError if an item with the given index doesn't exist within
            the list """
        has_next_node = hasattr(curr_node, 'next_node')
        if len(curr_node) > index and has_next_node:
            return curr_node, index
        elif has_next_node:
            return self.get_node_with_data_at_index(curr_node.next_node, index - len(curr_node))
        raise IndexError('No item in the list has the following index: ' + index)








    """ EXTENDED """

    def __contains__(self, item):
        """ Returns True/False whether the list contains the given item

        Usage: `5 in my_list`

        Args:
            item: The object for which containment is being checked for.

        Returns:
            True: if `item` is found somewhere in the list
            False: if `item` is not found anywhere in the list
        """
        return self.contains_recur(self.head, item)

    def contains_recur(self, curr_node, item):
        if item in curr_node.array:
            return True
        elif hasattr(curr_node, 'next_node'):
            return self.contains_recur(curr_node.next_node, item)
        else:  # Has reached end of linked list but hasn't found the element
            return False

    def __len__(self):
        """Return the total number of items in the list

        Usage: `len(my_list)`

        Returns:
            An int object indicating the *total* number of items in the list,
            NOT the number of nodes."""

        self.count_num_elements_recur(self.head, 0)

    def count_num_elements_recur(self, curr_node, count):
        curr_node_size = len(curr_node.array)
        if not hasattr(curr_node, 'next_node'):
            return count + curr_node_size
        return self.count_num_elements_recur(curr_node.next_node, count + curr_node_size)
        

    def __str__(self):
        """ Returns a string representation of the list.

        The format for representing an unrolled linked list will be as follows:
            - curly braces indicates an unrolled linked list
            - square brackets indicates a node
            - all values are separated by a comma and a space
        For example:
        {[1, 2, 3], [0, 9, 8], [2, 4, 6]}
        This list has three nodes and each node as three int objects in it.

        Usage: `str(my_list)`

        Returns:
            A string representation of the list."""

        string = '{'
        result = self.string_elements_recur(self.head, string)
        return result + '}'

    def string_elements_recur(self, curr_node, string):
        string += '['
        i = 0
        while i < len(curr_node.array):
            string += curr_node.array[i]
            if i != len(curr_node.array) - 1:
                string += ','
            i += 1
        string += ']'
        if hasattr(curr_node, 'next_node'):
            string += ', '
            return self.string_elements_recur(curr_node.next_node, string)





    """ OPERATORS """

    def __add__(self, other):
        """ Appends two Unrolled Linked Lists end-to-end using `+`

        Usage: `
            list_one = UnrolledLinkedList()
            list_two = UnrolledLinkedList()
            new_list = list_one + list_two
        `

        Args:
            other: Another Unrolled Linked List object. The new ULL should have
                the same max capacity as the current ULL.

        Returns:
            A new unrolled linked list.

        Raises:
            TypeError: If the passed in `other` parameter is not an unrolled
                linked list, raise this error. Users should not be able to
                append anything to an unrolled linked list besides another
                unrolled linked list.
        """
        pass

    def __mul__(self, count):
        """ Repeats (multiplies) the list a given number of times

        Usage: `my_list *= 5` should return a list of itself repeated 5x

        Args:
            count: An integer indicating the number of times the list should
                be repeated.

        Returns:
            The new data structure multiplied however many times indicated

        Raises:
            TypeError: If count is not an int

        """
        pass





    """ ITERATORS """

    def __iter__(self):
        """ Returns an iterable to allow one to iterate the list.

        This dunder function allows you to use this data structure in a loop.

        Usage: `for value in my_list:`

        Returns:
            An iterator that points to each value in the list using the `yield`
                statement.
        """
        pass

    def __reversed__(self):
        """ Works just like __iter__, but starts from the back.

        Usage: `for i in reversed(my_list)`

        Returns:
            An iterator starting from the back of the list
        """
        pass


