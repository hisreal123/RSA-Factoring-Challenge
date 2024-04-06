#!/usr/bin/python3

def factorize():
    """ A function to search file and factorize the given set of numbers into two prime numbers """
    import sys
    import os

    # print('Working with RSA')
    if len(sys.argv) != 2:
        print("Usage: python script.py <file_path>")
        sys.exit(1)

    # accessing the file path
    else:
        try:
            file_path = sys.argv[1]
            if os.path.isfile(file_path):
                with open(file_path, 'r') as f:
                    for line in f:
                        num = int(line)
                        if num % 2 == 0:
                            print("{}={}*{}".format(num, num // 2, 2))
                            continue
                        i = 3
                        while i < num // 2:
                            if num % i == 0:
                                print("{}={}*{}".format(num, num // i, i))
                                break
                            i = i + 2
                        if i == (num // 2) + 1:
                            print("{}={}*{}".format(num, num, 1))
            else:
                print("argument is not a file path !!!")
        except Exception as e:
            print("No argument returned !!".format(e))


if __name__ == "__main__":
    factorize()
