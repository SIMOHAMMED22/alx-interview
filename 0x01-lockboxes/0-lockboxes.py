#!/usr/bin/python3


def canUnlockAll(boxes):
    """
    Returns True if all boxes can be unlocked, False otherwise.

    Parameters:
    boxes (list of lists of int): The graph of lock boxes, where each sublist
                                  contains the indices of the boxes that can be
                                  unlocked using the key for the given box.
    """

    box_set = set(boxes[0])

    i = 0
    while i < len(boxes[0]):
        n = boxes[0][i]
        if n < len(boxes):
            box_set.update(boxes[n])
        i += 1

    j = 1
    while j < len(boxes):
        if j in box_set:
            box_set.update(boxes[j])
        else:
            return False
        j += 1

    return True
