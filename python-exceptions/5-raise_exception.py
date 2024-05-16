#!/usr/bin/python3
def raise_exception():
    try:
        raise TypeError("An exception occurred")
    except TypeError as te:
        raise te


if __name__ == "__main__":
    try:
        raise_exception()
    except TypeError as te:
        print("Exception raised")
