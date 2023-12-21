#!/usr/bin/env python

import sys

def capitalise_name(name):
    return name.upper()

def marina(times):
    for i in range(times):
        print(capitalise_name("Hello Marina time %d!" % i))

def main():
    marina(20)

if __name__ == '__main__':
    main()