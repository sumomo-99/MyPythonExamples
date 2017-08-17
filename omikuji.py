#!/usr/bin/env python3
"""
おみくじ
random.choice()を利用して、ランダムにおみくじを表示します。
"""

import random

omikuji = ['大吉', '吉', '中吉', '小吉', '凶']
print(random.choice(omikuji))
