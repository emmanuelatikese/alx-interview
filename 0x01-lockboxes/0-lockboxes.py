#!/usr/bin/python3
'''This all about the lockboxes algo'''


def canUnlockAll(boxes):
    '''This is the lockboxes algorithm'''
    num_box, open_box = len(boxes), set([0])
    keys = set(boxes[0])
    while keys:
        key = keys.pop()
        if key < num_box and key not in open_box:
            open_box.add(key)
            keys.update(boxes[key])
    return len(open_box) == num_box
