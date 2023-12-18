#!/usr/bin/python3

if __name__ == "__main__":
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

                numbers = [2, 3]
                with open(file_path, 'r') as file:
                    content = file.read()

                    m_c = ''
                    average = ''

                    for i in content:
                        if i.isdigit():
                            divisor = None

                            for j in range(1, int(i)):
                                if j > 1:
                                    if int(i) % j == 0:
                                        divisor = j
                                        # print(divisor)
                                        average = round(int(i) / divisor)
                                        print(divisor)

                                # print("{}={}*{}".format(i, factor1, factor2))
                            # else:
                            #     print("{} is a prime number".format(i))
                        else:
                            pass
                    # print("{}={}/2".format(m_c, average))

            else:
                print("argument is not a file path !!!")

        except Exception as e:
            print("No argument returned !!".format(e))
