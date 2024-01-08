#!/usr/bin/python3


def delete_at(my_list=[], idx=0):

    # handle out of range indexes and empty list
    if not (0 <= idx < len(my_list)) or not my_list:
        return my_list

    # perform the deletion and return the updated the list
    del my_list[idx]
    return (my_list)
