"""
-------------------------------------------------------
Array version of the Priority Queue ADT.
-------------------------------------------------------
Author:  David Brown
ID:      999999999
Email:   dbrown@wlu.ca
Section: CP164 C
__updated__ = "2023-02-12"
-------------------------------------------------------
"""
from copy import deepcopy


class Priority_Queue:

    def __init__(self):
        """
        -------------------------------------------------------
        Initializes an empty priority queue.
        Use: pq = Priority_Queue()
        -------------------------------------------------------
        Returns:
            a new Priority_Queue object (Priority_Queue)
        -------------------------------------------------------
        """
        self._values = []
        self._first = None

    def is_empty(self):
        """
        -------------------------------------------------------
        Determines if the priority queue is empty.
        Use: b = pq.is_empty()
        -------------------------------------------------------
        Returns:
            True if priority queue is empty, False otherwise.
        -------------------------------------------------------
        """
        return len(self._values) == 0

    def __len__(self):
        """
        -------------------------------------------------------
        Returns the length of the priority queue.
        Use: n = len(pq)
        -------------------------------------------------------
        Returns:
            the number of values in the priority queue.
        -------------------------------------------------------
        """
        return len(self._values)

    def insert(self, value):
        """
        -------------------------------------------------------
        A copy of value is appended to the end of the the priority queue
        Python list, and _first is updated as appropriate to the index of
        value with the highest priority.
        Use: pq.insert(value)
        -------------------------------------------------------
        Parameters:
            value - a data element (?)
        Returns:
            None
        -------------------------------------------------------
        """
        self._values.append(deepcopy(value))
        # your code here
        if len(self) == 1:
            self._first = 0
        elif self._values[-1] < self._values[self._first]:
            self._first = len(self) - 1

        return

    def peek(self):
        """
        -------------------------------------------------------
        Peeks at the highest priority value of the priority queue.
        Use: v = pq.peek()
        -------------------------------------------------------
        Returns:
            value - a copy of the highest priority value in the priority queue -
                the value is not removed from the priority queue. (?)
        -------------------------------------------------------
        """
        assert len(self._values) > 0, "Cannot peek at an empty priority queue"
        # your code here
        value = deepcopy(self._values[self._first])
        return value

    def remove(self):
        """
        -------------------------------------------------------
        Removes and returns the highest priority value from the priority queue.
        Use: value = pq.remove()
        -------------------------------------------------------
        Returns:
            value - the highest priority value in the priority queue -
                the value is removed from the priority queue. (?)
        -------------------------------------------------------
        """
        assert len(self._values) > 0, "Cannot remove from an empty priority queue"
        # your code here
        value = deepcopy(self._values[self._first])
        del self._values[self._first]
        self._set_first()

        return value

    def _set_first(self):
        """
        -------------------------------------------------------
        Private helper function to set the value of _first.
        _first is the index of the value with the highest
        priority in the priority queue. None if queue is empty.
        Use: self._set_first()
        -------------------------------------------------------
        Returns:
            None
        -------------------------------------------------------
        """
        # your code here

        if len(self._values) == 0:
            self._first = None
        else:
            smol = self._values[0]
            smolindex = 0
            for i in range(0, len(self._values), 1):
                if self._values[i] < smol:
                    smol = self._values[i]
                    smolindex = i
            self._first = smolindex
        return

    def __iter__(self):
        """
        FOR TESTING ONLY
        -------------------------------------------------------
        Generates a Python iterator. Iterates through the priority queue
        from front to rear. Not in priority order.
        Use: for value in pq:
        -------------------------------------------------------
        Returns:
            value - the next value in the priority queue (?)
        -------------------------------------------------------
        """
        for value in self._values:
            yield value

    def split_key(self, key):  # ass4 task6
        """
        -------------------------------------------------------
        Splits a priority queue into two depending on an external
        priority key. The source priority queue is empty when the method
        ends. The order of the values from source is preserved.
        Use: target1, target2 = source.split_key(key)
        -------------------------------------------------------
        Parameters:
            key - a data object (?)
        Returns:
            target1 - a priority queue that contains all values
                with priority higher than key (Priority_Queue)
            target2 - priority queue that contains all values with
                priority lower than or equal to key (Priority_Queue)
        -------------------------------------------------------
        """
        target1 = Priority_Queue()
        target2 = Priority_Queue()
        """
        while len(self._values) != 0:  # from is_empty
            if deepcopy(self._values[self._first]) < key:
                value = deepcopy(self._values[self._first])  # from remove
                del self._values[self._first]
                self._set_first()

                target1._values.append(deepcopy(value))  # from insert
                if len(target1) == 1:
                    target1._first = 0
                elif target1._values[-1] < target1._values[target1._first]:
                    target1._first = len(target1) - 1
            else:
                value = deepcopy(self._values[self._first])  # from remove
                del self._values[self._first]
                self._set_first()

                target2._values.append(deepcopy(value))  # from insert
                if len(target2) == 1:
                    target2._first = 0
                elif target2._values[-1] < target2._values[target2._first]:
                    target2._first = len(target2) - 1
        """
        while len(self._values) != 0:  # from is_empty
            if deepcopy(self._values[0]) < key:
                value = deepcopy(self._values[0])  # from remove
                del self._values[0]
                target1._values.append(deepcopy(value))  # from insert
            else:
                value = deepcopy(self._values[0])  # from remove
                del self._values[0]
                target2._values.append(deepcopy(value))  # from insert
        return target1, target2
