#!/usr/bin/python3

def search_replace(my_list, search, replace):
    # Create a new list where each occurrence of 'search' in 'my_list' is replaced by 'replace'
    new_replace = [replace if element == search else element for element in my_list]
    # Return the new list
    return new_replace

