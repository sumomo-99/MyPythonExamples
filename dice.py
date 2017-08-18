#!/usr/bin/env python3
"""
random.randint()を利用したサイコロ
MINからMAXまでの整数をランダムに表示します。
"""

import random

MIN = 1
MAX = 6

retry = 'yes'

print('このサイコロの最小値は{}、最大値は{}です。'.format(MIN, MAX))

while retry in ['yes', 'YES', 'Yes', 'y', 'Y']:
    print(random.randint(MIN, MAX))
    retry = input('もう1回？yes or no: ')
