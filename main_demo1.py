import math
import os
import random
import re
import sys

if __name__ == '__main__':
    n = int(input('Enter a number').strip())
    if n % 2 != 0: 
        print('Weird')
    elif n % 2 == 0 in range(2, 5):
        print('Not Weird')
    elif n % 2 == 0 in range(6, 20):
        print('Weird') 
    elif n > 20:
        print('Not Weird')
    else:
        print('Not Weird')
    