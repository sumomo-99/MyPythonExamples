#!/usr/bin/env python3
"""
このスクリプトを実行したマシンのパブリックIPアドレスを表示します。
実行のためにrequestsモジュールが必要です。
$ pip install requests
"""

import requests

URL = 'http://ipecho.net/plain'

def getPublicIp():
    """パブリックIPアドレスを返す。"""
    response = requests.get(URL)

    if response.status_code == 200:
        return response.text
    else:
        return 'IPアドレスを取得できませんでした。'


def main():
    print(getPublicIp())


if __name__ == "__main__":
    main()

