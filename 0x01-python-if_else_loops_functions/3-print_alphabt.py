#!/usr/bin/python3
for letter in range(ord("a"), ord("z") + 1):
        if chr(letter) != 'q' and chr(letter) != 'e':
                print("{:s}".format(chr(letter)), end="")
