#!/usr/bin/env python

# dependencies - sox, mp3 library for sox

import os
import configparser
from datetime import datetime
import calendar
import time

TIME = datetime.now()


def get_hour():
    hour = TIME.hour
    return hour

def get_minute():
    minute = TIME.minute
    return minute

def get_day():
    day = calendar.weekday(TIME.year, TIME  .month, TIME.day)
    switcher = {
        0: 'Monday',
        1: 'Tuesday',
        2: 'Wednesday',
        3: "Thursday",
        4: 'Friday',
        5: 'Saturday',
        6: 'Sunday'
    }
    return switcher.get(day, "error")

def main():
    config = configparser.ConfigParser()
    config.read('config.ini')

    day = get_day()
    hour = get_hour()
    minute = get_minute()

    mwf_alarm = [
        config['MWF']['1_ALARM'],
        config['MWF']['2_ALARM'],
        config['MWF']['3_ALARM'],
        config['MWF']['4_ALARM'],
        config['MWF']['5_ALARM'],
        config['MWF']['6_ALARM'],
        config['MWF']['7_ALARM'],
        config['MWF']['8_ALARM'],
        config['MWF']['9_ALARM'],
        config['MWF']['10_ALARM'],
        config['MWF']['11_ALARM'],
        config['MWF']['12_ALARM'],
        config['MWF']['13_ALARM'],
        config['MWF']['14_ALARM']
    ]

    tth_alarm = [
        config['TTH']['1_ALARM'],
        config['TTH']['2_ALARM'],
        config['TTH']['3_ALARM'],
        config['TTH']['4_ALARM'],
        config['TTH']['5_ALARM'],
        config['TTH']['6_ALARM'],
        config['TTH']['7_ALARM'],
        config['TTH']['8_ALARM'],
        config['TTH']['9_ALARM'],
        config['TTH']['10_ALARM']
    ]

    sys_alarm = str(hour) + ":" + str(minute)

    if day in ['Monday', 'Wednesday', 'Friday']:
        if sys_alarm in mwf_alarm:
            path = ('alarm-sound.mp3')
            os.system('play ' + path + ' reverse trim 0 15 reverse')
    else:
        if sys_alarm in tth_alarm:
            path = ('alarm-sound.mp3' +  ' reverse trim 0 15 reverse')
            os.system('play ' + path) 
main()
