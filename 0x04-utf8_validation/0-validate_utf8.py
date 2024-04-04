#!/usr/bin/python3
"""UTF-8 Validation"""


def validUTF8(data):
    """
    method that determines if a given data set
    represents a valid UTF-8 encoding
    """
    nbytes = 0

    byte1 = 1 << 7
    byte2 = 1 << 6

    for n in data:
        x = 1 << 7
        if nbytes == 0:
            while x & n:
                nbytes += 1
                x = x >> 1
            if nbytes == 0:
                continue
            if nbytes == 1 or nbytes > 4:
                return False
        else:
            if not (n & byte1 and not (n & byte2)):
                return False
        nbytes -= 1
    return nbytes == 0
