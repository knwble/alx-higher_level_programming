#!/usr/bin/python3
import sys

def safe_function(fct, *args):
    try:
        return fct(*args)
    except Exception as exe:
        print("Exception: {}".format(exe), file=sys.stderr)
        return (None)

