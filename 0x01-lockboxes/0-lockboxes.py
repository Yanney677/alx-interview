#!/usr/bin/python3

"""
Script that determines if all the boxes can be opened
"""


def canUnlockAll(boxes):
    number_boxes = len(boxes)
    unlocked_boxes = [False] * number_boxes
    unlocked_boxes[0] = True

    """Use "s" to check for the boxes to be explore"""
    s = [0]

    """Depth-first search to unlock boxes"""
    while s:
        cur_box = s.pop()

        """Checks all the keys in the cur_box"""
        for key in boxes[cur_box]:
            if key < number_boxes and not unlocked_boxes[key]:
                """Unlock the box if it hasn't been unlocked before"""
                unlocked_boxes[key] = True
                s.append(key)

    """Check if all boxes have been unlocked"""
    return all(unlocked_boxes)
