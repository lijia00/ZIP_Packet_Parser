import os
from util import dict_create

cur_dir = os.path.abspath(os.path.curdir)
fname = os.path.join(cur_dir, 'ZW_classcmd.py')
cmdclass_dict = dict_create.create_dict_from_variable_list(fname)


def main():
    print_header()
    user_input = 'EMPTY'

    while user_input != 'Q' and user_input:
        user_input = input('enter the bytes to parse separated by spaces 01 02 03:, Q to exit ').upper().strip()
        # create a list containing each byte based on user input string, separated by a space
        if len(user_input) != 0:
            byte_list = []
            n = 3
            [byte_list.append(user_input[i:i + n].strip()) for i in range(0, len(user_input), n)]
            parse_input(byte_list)

        else:
            print("Sorry we couldn't parse that")


def print_header():
    print()
    print('-------------------------------------')
    print('---------ZIP PACKET PARSER APP-------')
    print('-------------------------------------')
    print()


def parse_input(byte_list):
    for each in byte_list:
        try:
            print(cmdclass_dict[each])
        except Exception as x:
            print("got except error: {}".format(x))


if __name__ == "__main__":
    main()
