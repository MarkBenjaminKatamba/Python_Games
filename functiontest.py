# -*- coding: utf-8 -*-
"""
Created on Thu Jun 18 21:59:31 2020

@author: kmark
"""


# pass_len = input("Enter the desired password length:\n")
# for pass_len in range (1,6):
#     if pass_len < 6:
#         print("Password cannot be less than 6 characters!")
    # break

def pass_len():
    length = input("Enter the desired password length:\n")
    # for length in range(1,6):
    if int(length) < 6:
            print("Password cannot be less than 6 characters!")
            return pass_len()
pass_len()