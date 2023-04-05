"""
-------------------------------------------------------
Data Strusture Utilities
-------------------------------------------------------
Author:  Muhammad Talal Tariq
ID:      169035539
Email:   tari5539@mylaurier.ca
__updated__ = "2023-02-05"
-------------------------------------------------------
"""
# Imports
from Stack_array import Stack
from Queue_array import Queue
from Priority_Queue_array import Priority_Queue
from List_array import List
from Movie import Movie
# Constants

# lab2


def array_to_stack(stack, source):  # lab2 task2
    """
    -------------------------------------------------------
    Pushes contents of source onto stack. At finish, source is empty.
    Last value in source is at bottom of stack,
    first value in source is on top of stack.
    Use: array_to_stack(stack, source)
    -------------------------------------------------------
    Parameters:
        stack - a Stack object (Stack)
        source - a Python list (list)
    Returns:
        None
    -------------------------------------------------------
    """  # function wants source to be empty
    for i in range(len(source)-1, -1, -1):
        stack.push(source[i])
        del source[i]
    #source = []
    return


def stack_to_array(stack, target):  # lab2 task3
    """
    -------------------------------------------------------
    Pops contents of stack into target. At finish, stack is empty.
    Top value of stack is at end of target,
    bottom value of stack is at beginning of target.
    Use: stack_to_array(stack, target)
    -------------------------------------------------------
    Parameters:
        stack - a Stack object (Stack)
        target - a Python list (list)
    Returns:
        None
    -------------------------------------------------------
    """  # function wants stack values to be empty
    """ old, it was outputing reverse order
    while stack.is_empty() is False:
        target.append(stack.pop())
    """
    list = []
    while stack.is_empty() is False:
        list.append(stack.pop())
    for i in range(len(list)-1, -1, -1):
        target.append(list[i])
    return


def stack_test(source):  # lab2 task4
    """
    -------------------------------------------------------
    Tests the methods of Stack for empty and
    non-empty stacks using the data in source:
    is_empty, push, pop, peek
    (Testing pop and peek while empty throws exceptions)
    Use: stack_test(source)
    -------------------------------------------------------
    Parameters:
        source - list of data (list of ?)
    Returns:
        None
    -------------------------------------------------------
    """
    s = Stack()
    s.is_empty()

    s.push(source[0])
    s.push(source[1])

    s.pop()
    s.peek()
    s.is_empty()
    return
# lab3 task3


def array_to_queue(queue, source):  # lab3 task3
    """
    -------------------------------------------------------
    Inserts contents of source into queue. At finish, source is empty.
    Last value in source is at rear of queue,
    first value in source is at front of queue.
    Use: array_to_queue(queue, source)
    -------------------------------------------------------
    Parameters:
        queue - a Queue object (Queue)
        source - a Python list (list)
    Returns:
        None
    -------------------------------------------------------
    """
    for i in range(0, len(source), 1):
        queue.insert(source[i])
    for i in range(len(source)-1, -1, -1):
        del source[i]
    return


def queue_to_array(queue, target):  # lab3 task3
    """
    -------------------------------------------------------
    Removes contents of queue into target. At finish, queue is empty.
    Front value of queue is at front of target,
    rear value of queue is at end of target.
    Use: queue_to_array(queue, target)
    -------------------------------------------------------
    Parameters:
        queue - a Queue object (Queue)
        target - a Python list (list)
    Returns:
        None
    -------------------------------------------------------
    """
    while len(queue) != 0:
        target.append(queue.remove())
    return


def queue_test(a):  # lab3 task3
    """
    -------------------------------------------------------
    Tests queue implementation.
  Tests the methods of Queue are tested for both empty and
  non-empty queues using the data in a:
        is_empty, insert, remove, peek, len
    Use: queue_test(a)
    -------------------------------------------------------
    Parameters:
        a - list of data (list of ?)
    Returns:
        None
    -------------------------------------------------------
    """
    q = Queue()

    # tests for the queue methods go here
    # print the results of the method calls and verify by hand
    print("is queue empty:", q.is_empty())
    q.insert(a[0])
    print("inserted data")
    q.insert(a[1])
    print("inserted data")
    print("front of queueis:", q.peek())
    print("removed data:", q.remove())

    return
# lab3 task6


def array_to_pq(pq, source):  # lab3 task6
    """
    -------------------------------------------------------
    Inserts contents of source into pq. At finish, source is empty.
    Last value in source is at rear of pq,
    first value in source is at front of pq.
    Use: array_to_pq(pq, source)
    -------------------------------------------------------
    Parameters:
        pq - a Priority_Queue object (Priority_Queue)
        source - a Python list (list)
    Returns:
        None
    -------------------------------------------------------
    """
    for i in range(0, len(source), 1):
        pq.insert(source[i])
    for i in range(len(source)-1, -1, -1):
        del source[i]
    return


def pq_to_array(pq, target):  # lab3 task6
    """
    -------------------------------------------------------
    Removes contents of pq into target. At finish, pq is empty.
    Highest priority value in pq is at front of target,
    lowest priority value in pq is at end of target.
    Use: pq_to_array(pq, target)
    -------------------------------------------------------
    Parameters:
        pq - a Priority_Queue object (Priority_Queue)
        target - a Python list (list)
    Returns:
        None
    -------------------------------------------------------
    """
    while len(pq) != 0:
        target.append(pq.peek())
        pq.remove()

    return


def priority_queue_test(a):  # lab3 task6
    """
    -------------------------------------------------------
    Tests priority queue implementation.
    Test the methods of Priority_Queue are tested for both empty and
    non-empty priority queues using the data in a:
        is_empty, insert, remove, peek
    Use: priority_queue_test(a)
    -------------------------------------------------------
    Parameters:
        a - list of data (list of ?)
    Returns:
        None
    -------------------------------------------------------
    """
    pq = Priority_Queue()
    # tests for the priority queue methods go here
    # print the results of the method calls and verify by hand
    print("is pq empty?", pq.is_empty())
    pq.insert(a[0])
    print("data inserted into pq")
    pq.insert(a[1])
    print("data inserted into pq")
    print("highest priority in pq is: ", pq.peek())
    pq.remove()
    print("data removed from pq")
    return

# lab3 task6


def array_to_list(llist, source):  # lab3 task6
    """
    -------------------------------------------------------
    Appends contests of source to llist. At finish, source is empty.
    Last element in source is at rear of llist,
    first element in source is at front of llist.
    Use: array_to_list(llist, source)
    -------------------------------------------------------
    Parameters:
        llist - a List object (List)
        source - a Python list (list)
    Returns:
        None
    -------------------------------------------------------
    """
    i = len(source) - 1
    while i >= 0:
        llist.insert(0, source[i])
        del source[i]
        i -= 1
    return


def list_to_array(llist, target):  # lab3 task6
    """
    -------------------------------------------------------
    Removes contents of llist into target. At finish, llist is empty.
    Front element of llist is at front of target,
    rear element of llist is at rear of target.
    Use: list_to_array(llist, target)
    -------------------------------------------------------
    Parameters:
        llist - a List object (List)
        target - a Python list (list)
    Returns:
        None
    -------------------------------------------------------
    """
    args = [0]
    while llist.is_empty() is False:
        target.append(llist.pop(args[0]))

    return


def list_test(source):  # lab3 task6
    """
    -------------------------------------------------------
    Tests List implementation.
    The methods of List are tested for both empty and
    non-empty lists using the data in source
    Use: list_test(source)
    -------------------------------------------------------
    Parameters:
        source - list of data (list of ?)
    Returns:
        None
    -------------------------------------------------------
    """
    lst = List()
    # tests for the List methods go here
    # print the results of the method calls and verify by hand
    print("is lst empty?", lst.is_empty())  # should be yes

    lst.append(source[0])
    lst.append(source[1])
    lst.append(source[2])
    lst.append(source[3])
    print("appended first 4 movies")

    lst.insert(0, source[4])
    print("inserted 5th movie at index 1")

    key = Movie('Omega Man, The', 1971, None, None, None)
    print("removed:")
    print(lst.remove(key))

    #key = Movie('Dark City', 1998, "Alex Proyas", 7.2, [3, 4, 5, 8])
    key = Movie('Dark City', 1998, None, None, None)
    print("How many times does dark city appear in the list?", lst.count(key))

    print("index of dark city:", lst.index(key))

    print("lets find dark city, if is in the list:")
    print(lst.find(key))

    print("last movie in list(alphabetically)")
    print(lst.max())

    print("first movie in list(alphabetically)")
    print(lst.min())
    return
