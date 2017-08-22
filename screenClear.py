#!/usr/bin/env python3
"""
スクリーン(コンソール画面)をクリアするサンプルです。
"""

import subprocess
import time

# 画面に文字を表示します。
for i in range(10):
    print('abcdefghijklmnopqrstuvwxyz')
    time.sleep(1)

# subprocessモジュールで画面をクリアします。
subprocess.run(["clear"])
