#!/usr/bin/python3
def canUnlockAll(boxes):
    """
    Returns True if all boxes can be unlocked, False otherwise.

    Parameters:
    boxes (list of lists of int): The graph of lock boxes, where each sublist
                                  contains the indices of the boxes that can be
                                  unlocked using the key for the given box.
    """
    if not boxes:
        return False

    n = len(boxes)
    keys = set([0])
    unlocked = set()

    while keys:

        box = keys.pop()
        unlocked.add(box)
        keys.update(set(boxes[box]) - unlocked)

    return len(unlocked) == n
