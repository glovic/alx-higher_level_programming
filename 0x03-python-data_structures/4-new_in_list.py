#!/usr/bin/python3


def new_in_list(my_list, idx, element):

    dup_list = my_list.copy()

    if not (0 <= idx < len(dup_list)):
        return dup_list

    for i in range(len(dup_list)):
        if i == idx:
            dup_list[i] = element
            return dup_list
