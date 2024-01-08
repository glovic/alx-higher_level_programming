#!/usr/bin/python3


def replace_in_list(my_list, idx, element):

    # check for invalid index positions, if found, don't modify the list
    if not (0 <= idx < len(my_list)):
        return my_list

    for i in range(len(my_list)):
        if i == idx:
            # update the list with the replacement's value
            my_list[i] = element

            return my_list
