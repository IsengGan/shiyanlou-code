#!/usr/bin/env python3

import sys

def Hours(m):
    if m < 0:
        raise ValueError("Input number cannot be negative")
    else:
        print("{} H, {} M".format(int(m / 60), m % 60))

try:
    Hours(int(sys.argv[1]))
except:
    print("Parameter Error")
