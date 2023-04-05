"""
-------------------------------------------------------
Array version of the Stack ADT.
-------------------------------------------------------
Author:  David Brown
ID:      999999999
Email:   dbrown@wlu.ca
Section: CP164 A
__updated__ = "2023-01-30"
-------------------------------------------------------
"""
from copy import deepcopy


class Stack:

    def __init__(self):
        """
        -------------------------------------------------------
        Initializes an is_empty stack. Data is stored in a Python list.
        Use: s = Stack()
        -------------------------------------------------------
        Returns:
            a new Stack object (Stack)
        -------------------------------------------------------
        """
        self._values = []

    def is_empty(self):
        """
        -------------------------------------------------------
        Determines if the stack is empty.
        Use: b = s.is_empty()
        -------------------------------------------------------
        Returns:
            True if the stack is empty, False otherwise
        -------------------------------------------------------
        """
        # Your code here
        isempty = False
        if self._values == []:
            isempty = True

        return isempty

    def push(self, value):
        """
        -------------------------------------------------------
        Pushes a copy of value onto the top of the stack.
        Use: s.push(value)
        -------------------------------------------------------
        Parameters:
            value - a data element (?)
        Returns:
            None
        -------------------------------------------------------
        """
        # Your code here
        copiedval = deepcopy(value)  # deepcopied the value
        self._values.append(copiedval)  # putting the deepcopied val into stack

        return

    def pop(self):
        """
        -------------------------------------------------------
        Pops and returns the top of stack. The value is removed
        from the stack. Attempting to pop from an empty stack
        throws an exception.
        Use: value = s.pop()
        -------------------------------------------------------
        Returns:
            value - the value at the top of the stack (?)
        -------------------------------------------------------
        """
        assert len(self._values) > 0, "Cannot pop from an empty stack"
        # Your code here
        value = self._values[-1]
        del self._values[-1]

        return value

    def peek(self):
        """
        -------------------------------------------------------
        Returns a copy of the value at the top of the stack.
        Attempting to peek at an empty stack throws an exception.
        Use: value = s.peek()
        -------------------------------------------------------
        Returns:
            value - a copy of the value at the top of the stack (?)
        -------------------------------------------------------
        """
        assert len(self._values) > 0, "Cannot peek at an empty stack"
        # Your code here
        stack = deepcopy(self)  # redundantly deepcopying the stack
        value = stack._values[-1]  # and then finding the last element normally

        return value

    def __iter__(self):
        """
        FOR TESTING ONLY
        -------------------------------------------------------
        Generates a Python iterator. Iterates through the stack
        from top to bottom.
        Use: for v in s:
        -------------------------------------------------------
        Returns:
            value - the next value in the stack (?)
        -------------------------------------------------------
        """
        for value in self._values[::-1]:
            yield value

    def split_alt(self):  # ass3 task2
        """
        -------------------------------------------------------
        Splits the source stack into separate target stacks with values
        alternating into the targets. At finish source stack is empty.
        Use: target1, target2 = source.split_alt()
        -------------------------------------------------------
        Returns:
            target1 - contains alternating values from source (Stack)
            target2 - contains other alternating values from source (Stack)
        -------------------------------------------------------
        """
        target1 = Stack()
        target2 = Stack()
        i = 1
        isempty = False
        while isempty is False:
            if i % 2 != 0:
                # copied push code and putting pop code as the "Value"

                assert len(self._values) > 0, "Cannot pop from an empty stack"
                copiedval = deepcopy(self._values[-1])  # from push(pop())
                target1._values.append(copiedval)  # from push()
                del self._values[-1]  # from pop()
            else:
                # from pop()
                assert len(self._values) > 0, "Cannot pop from an empty stack"
                copiedval = deepcopy(self._values[-1])  # from push(pop())
                target2._values.append(copiedval)  # from push()
                del self._values[-1]  # from pop()
            i += 1
            # from is_empty()
            if self._values == []:
                isempty = True
        return target1, target2
