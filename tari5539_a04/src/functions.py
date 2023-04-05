"""
-------------------------------------------------------
[program description]
-------------------------------------------------------
Author:  Muhammad Talal Tariq
ID:      169035539
Email:   tari5539@mylaurier.ca
__updated__ = "2023-02-06"
-------------------------------------------------------
"""
# Imports
from Priority_Queue_array import Priority_Queue
from Queue_array import Queue
# Constants


def pq_split_key(source, key):  # task5
    """
    -------------------------------------------------------
    Splits a priority queue into two depending on an external
    priority key. The source priority queue is empty when the method
    ends.
    Use: target1, target2 = pq_split_key(source, key)
    -------------------------------------------------------
    Parameters:
        source - a priority queue (Priority_Queue)
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

    while source.is_empty() is False:
        if source.peek() < key:
            target1.insert(source.remove())
        else:
            target2.insert(source.remove())
    return target1, target2


def queue_combine(source1, source2):  # task3
    """
    -------------------------------------------------------
    Combines two source queues into the current target queue.
    When finished, the contents of source1 and source2 are interlaced
    into target and source1 and source2 are empty.
    Order of source values is preserved.
    (iterative algorithm)
    Use: target = queue_combine(source1, source2)
    -------------------------------------------------------
    Parameters:
        source1 - a queue (Queue)
        source2 - a queue (Queue)
    Returns:
        target - a queue (Queue)
    -------------------------------------------------------
    """
    target = Queue()
    w = 0
    while not source1.is_empty() or not source2.is_empty():
        if (w % 2 == 0) and not source1.is_empty():
            target.insert(source1.remove())
        elif not source2.is_empty():
            target.insert(source2.remove())
        w += 1

    return target
