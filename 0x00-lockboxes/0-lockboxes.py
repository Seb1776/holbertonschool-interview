#!/usr/bin/python3
'''Lockbox Class'''


def canUnlockAll(boxes):
    '''Unlock Box Method'''
    if type(boxes) is list:
        keys = [0]

        for k in keys:
            for x in boxes[k]:
                if x not in keys and x < len(boxes):
                    keys.append(x)

        if len(keys) == len(boxes):
            return True

        else:
            return False
