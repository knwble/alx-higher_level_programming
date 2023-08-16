#!/usr/bin/python3

def uniq_add(my_list=[]):
    number = 0
    for x in set(my_list):
        number += x
        return (number)
