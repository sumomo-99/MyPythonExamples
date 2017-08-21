#!/usr/bin/env python3
"""
enumetateを利用したfor文のサンプルです。
"""

def main():
    study_time = [2, 4, 1, 2, 3, 1, 5]
    sum_time = 0

    print('今週の勉強時間')

    # enumerate関数のstart=1を指定して、1からカウントさせる。
    for day, s_time in enumerate(study_time, start=1):
        print('{}日は{}時間勉強しました。'.format(day, s_time))
        sum_time += s_time

    print('今週は合計{}時間、勉強しました。'.format(sum_time))

if __name__ == '__main__':
    main()
