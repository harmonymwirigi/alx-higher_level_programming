#!/usr/bin/python3
#1-my_list.py
""" class of that inherits from a list """

class MyList(list):

    def print_sorted(self):
        l = self.sort()
        print(l)
