
"""Challenges
Implement these classic iterative sorting functions using sorting starter code:
is_sorted(items) - return a boolean indicating whether all items are in ascending order
bubble_sort(items) - swap adjacent items that are out of order, repeat until all items are sorted
selection_sort(items) - find minimum item in unsorted items, swap it with first unsorted item, repeat until all items are sorted
insertion_sort(items) - take first unsorted item, insert it in sorted order in front of items, repeat until all items are sorted
Run python sorting.py to test sorting algorithms on a small random sample:
$ python sorting.py bubble_sort 10 20
Initial items: [3, 15, 4, 7, 20, 6, 18, 11, 9, 7]
Sorting items with bubble_sort(items)
Sorted items:  [3, 4, 6, 7, 7, 9, 11, 15, 18, 20]
Annotate functions with complexity analysis of running time (operations) and space (memory usage)
Write a thorough suite of sorting unit tests to ensure your sorting algorithms are robust
Write tests in a way that lets you add new sorting functions without needing to write more tests
Include a variety of test cases that cover many different input types, orderings, distributions, and edge cases
Run pytest sorting_test.py to run the sorting unit tests and fix any failures"""





def is_sorted(items):
    """Return a boolean indicating whether given items are in sorted order.
    TODO: Running time: ??? Why and under what conditions?
    TODO: Memory usage: ??? Why and under what conditions?"""
    # TODO: Check that all adjacent items are in order, return early if so


def bubble_sort(items):
    """Sort given items by swapping adjacent items that are out of order, and
    repeating until all items are in sorted order.
    TODO: Running time: ??? Why and under what conditions?
    TODO: Memory usage: ??? Why and under what conditions?"""
    # TODO: Repeat until all items are in sorted order
    # TODO: Swap adjacent items that are out of order


def selection_sort(items):
    """Sort given items by finding minimum item, swapping it with first
    unsorted item, and repeating until all items are in sorted order.
    TODO: Running time: ??? Why and under what conditions?
    TODO: Memory usage: ??? Why and under what conditions?"""
    # TODO: Repeat until all items are in sorted order
    # TODO: Find minimum item in unsorted items
    # TODO: Swap it with first unsorted item


def insertion_sort(items):
    """Sort given items by taking first unsorted item, inserting it in sorted
    order in front of items, and repeating until all items are in order.
    TODO: Running time: ??? Why and under what conditions?
    TODO: Memory usage: ??? Why and under what conditions?"""
    # TODO: Repeat until all items are in sorted order
    # TODO: Take first unsorted item
    # TODO: Insert it in sorted order in front of items