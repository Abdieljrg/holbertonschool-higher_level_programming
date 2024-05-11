#!/usr/bin/python3
if __name__ == "__main__":
    import sys

    count = len(sys.argv) - 1
    if count == 0:
        print("0 arguments.")
    if count == 1:
        print("1 argument:")
        print(f"1: {sys.argv[1]}")
    else:
        print(f"{count} arguments:")
        for i in range(1, count + 1):
            print(f"{1}: {sys.argv[1]}")
