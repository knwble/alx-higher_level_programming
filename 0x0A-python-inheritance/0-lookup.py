#!/usr/bin/python3
"""Defines an object attribute lookup function."""


def lookup(obj):
    """This functions looks out for all attributes and methods of an object"""
    return (dir(obj))
