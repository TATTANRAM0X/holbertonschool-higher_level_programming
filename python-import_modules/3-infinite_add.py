#!/usr/bin/python3
if __name__ == "__main__":
    import sys

    result = 0
    arguments = len(sys.argv)

    if arguments == 1:
        print("{}".format("0"))
    else:
        for i in range(1, arguments):
            result = result + int(sys.argv[i])
        print(result)
