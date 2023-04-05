"""
-------------------------------------------------------
Linked version of the Deque ADT.
-------------------------------------------------------
Author:  David Brown
ID:      999999999
Email:   dbrown@wlu.ca
Term:    Winter 2020
__updated__ = "2023-03-07"
-------------------------------------------------------
"""
# Imports
from copy import deepcopy


class _Deque_Node:

    def __init__(self, value, _prev, _next):
        """
        -------------------------------------------------------
        Initializes a deque node.
        Use: node = _Deque_Node(value, _prev, _next)
        -------------------------------------------------------
        Parameters:
            value - value value for node (?)
            _prev - another deque node (_Deque_Node)
            _next - another deque node (_Deque_Node)
        Returns:
            a new _Deque_Node object (_Deque_Node)

        -------------------------------------------------------
        """
        self._value = deepcopy(value)
        self._prev = _prev
        self._next = _next


class Deque:

    def __init__(self):
        """
        -------------------------------------------------------
        Initializes an empty deque.
        Use: d = deque()
        -------------------------------------------------------
        Returns:
            a new Deque object (Deque)
        -------------------------------------------------------
        """
        self._front = None
        self._rear = None
        self._count = 0

    def is_empty(self):
        """
        -------------------------------------------------------
        Determines if the deque is empty.
        Use: b = deque.is_empty()
        -------------------------------------------------------
        Returns:
            True if the deque is empty, False otherwise.
        -------------------------------------------------------
        """
        # your code here
        return self._count == 0

    def __len__(self):
        """
        -------------------------------------------------------
        Returns the size of the deque.
        Use: n = len(deque)
        -------------------------------------------------------
        Returns:
            the number of values in the deque (int)
        -------------------------------------------------------
        """
        # your code here
        return self._count

    def __eq__(self, target):
        """
        ---------------------------------------------------------
        Determines whether two Deques are equal.
        Values in self and target are compared and if all values are equal
        and in the same order, returns True, otherwise returns False.
        Use: equals = source == target
        ---------------
        Parameters:
            target - a deque (Deque)
        Returns:
            equals - True if source contains the same values
                as target in the same order, otherwise False. (boolean)
        -------------------------------------------------------
        """
        # your code here
        equals = True
        cur1 = self._front
        cur2 = target._front
        if self._count == target._count:
            while cur1 is not None:
                if cur1._value != cur2._value:
                    equals = False
                cur1 = cur1._next
                cur2 = cur2._next
        else:
            equals = False
        return equals

    def insert_front(self, value):
        """
        -------------------------------------------------------
        Inserts a copy of value into the front of the deque.
        Use: deque.insert_front(value)
        -------------------------------------------------------
        Parameters:
            value - a data element (?)
        Returns:
            None
        -------------------------------------------------------
        """
        # your code here
        node = _Deque_Node(deepcopy(value), None, self._front)

        if self._front is None:
            self._rear = node
        self._front = node
        self._count += 1
        return

    def insert_rear(self, value):
        """
        -------------------------------------------------------
        Inserts a copy of value into the rear of the deque.
        Use: deque.insert_rear(value)
        -------------------------------------------------------
        Parameters:
            value - a data element (?)
        Returns:
            None
        -------------------------------------------------------
        """
        # your code here
        node = _Deque_Node(deepcopy(value), self._rear, None)

        if self._front is None:
            self._front = node
        else:
            self._rear._next = node

        self._rear = node
        self._count += 1
        return

    def remove_front(self):
        """
        -------------------------------------------------------
        Removes and returns value from the front of the deque.
        Use: v = deque.remove_front()
        -------------------------------------------------------
        Returns:
            value - the value at the front of deque (?)
        -------------------------------------------------------
        """
        assert self._front is not None, "Cannot remove from an empty deque"
        # your code here
        value = deepcopy(self._front._value)
        if self._front._next is None:
            self._front = None
            self._rear = None
        else:
            self._front = self._front._next
            self._front._prev = None

        self._count -= 1
        return value

    def remove_rear(self):
        """
        -------------------------------------------------------
        Removes and returns value from the rear of the deque.
        Use: v = deque.remove_rear()
        -------------------------------------------------------
        Returns:
            value - the value at the rear of deque (?)
        -------------------------------------------------------
        """
        assert self._rear is not None, "Cannot remove from an empty deque"
        # your code here
        value = deepcopy(self._rear._value)
        if self._front._next is None:
            self._front = None
            self._rear = None
        else:
            self._rear = self._rear._prev
            self._rear._next = None

        self._count -= 1
        return value

    def peek_front(self):
        """
        -------------------------------------------------------
        Peeks at the front of deque.
        Use: v = deque.peek_front()
        -------------------------------------------------------
        Returns:
            value - a copy of the value at the front of deque (?)
        -------------------------------------------------------
        """
        assert self._front is not None, "Cannot peek at an empty deque"

        # your code here
        value = deepcopy(self._front._value)
        return value

    def peek_rear(self):
        """
        -------------------------------------------------------
        Peeks at the rear of deque.
        Use: v = deque.peek_rear()
        -------------------------------------------------------
        Returns:
            value - a copy of the value at the rear of deque (?)
        -------------------------------------------------------
        """
        assert self._rear is not None, "Cannot peek at an empty deque"

        # your code here
        value = deepcopy(self._rear._value)
        return value

    def _swap(self, l, r):
        """
        -------------------------------------------------------
        Swaps two nodes within a deque. l has taken the place of r, 
        r has taken the place of l and _front and _rear are updated 
        as appropriate. Data is not moved.
        Use: self._swap(self, l, r):
        -------------------------------------------------------
        Parameters:
            l - a pointer to a deque node (_Deque_Node)
            r - a pointer to a deque node (_Deque_Node)
        Returns:
            None
        -------------------------------------------------------
        """
        assert l is not None and r is not None, "nodes to swap cannot be None"
        # your code here

        if self._front is l:
            self._front = r
        elif self._front is r:
            self._front = l
        if self._rear is l:
            self._rear = r
        elif self._rear is r:
            self._rear = l
        if r._next is l:
            temp_next = l._next
            l._next = r
            l._prev = r._prev
            r._prev = l
            r._next = temp_next
        elif l._next is r:
            temp_next = r._next
            r._next = l
            r._prev = l._prev
            l._prev = r
            l._next = temp_next
        else:
            temp_next = l._next
            temp_prev = l._prev
            l._next = r._next
            l._prev = r._prev
            r._next = temp_next
            r._prev = temp_prev
        if r._prev is not None:
            r._prev._next = r
        if r._next is not None:
            r._next._prev = r
        if l._prev is not None:
            l._prev._next = l
        if l._next is not None:
            l._next._prev = l

        """
        lnext = l._next
        lprev = l._prev
        rnext = r._next
        rprev = r._prev
        lfront = l is self._front
        lrear = l is self._rear
        rfront = r is self._front
        rrear = r is self._rear

        if lnext is r:

            if rprev._prev is not None:
                rprev._prev._next = r
            #rprev = lprev
            if lnext._next is not None:
                lnext._next._prev = l
            #lnext = rnext

            r._prev = lprev
            l._next = rnext

            r._next = l
            l._prev = r

        if rnext is l:
            lnext = r
            rprev = l

            lprev = rprev
            rnext = lnext

        else:
            l._prev = rprev
            l._next = rnext

            r._prev = lprev
            r._next = lnext

            if lprev is not None:
                lprev._next = r
            if lnext is not None:
                lnext._prev = r

            if rprev is not None:
                rprev._next = l
            if rnext is not None:
                rnext._prev = l

        if lfront:
            self._front = r
        elif rfront:
            self._front = l
        if lrear:
            self._rear = r
        elif rrear:
            self._rear = l
        """

        return

    def __iter__(self):
        """
        USE FOR TESTING ONLY
        -------------------------------------------------------
        Generates a Python iterator. Iterates through the deque
        from front to rear.
        Use: for v in d:
        -------------------------------------------------------
        Returns:
            yields
            value - the next value in the deque (?)
        -------------------------------------------------------
        """
        current = self._front

        while current is not None:
            yield current._value
            current = current._next

    def print(self):
        """
        -------------------------------------------------------
        Prints the contents of Queue from front to rear.
        Use: q.print()
        -------------------------------------------------------
        Returns:
            None
        -------------------------------------------------------
        """
        curr = self._front

        while curr is not None:
            print(curr._value)
            curr = curr._next
        return
