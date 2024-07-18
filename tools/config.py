#!/bin/python3
#-*- coding: utf-8 -*-

'''
a function to read json config file
'''
import os
import sys
import json

'''
get config file from command line argument and
loads json file to python dict
'''
def load():
    file = sys_args()['config_file']
    if not os.path.exists(file): raise Exception('config file not exists')
    return json.load(open(file, 'r'))

def sys_args():
    if not sys.argv: raise Exception('no command line argument')
    if len(sys.argv) == 2:
        return {
            'config_file': None,
            'work_file': sys.argv[1],
        }
    if len(sys.argv) == 3:
        return {
            'config_file': sys.argv[1],
            'work_file': sys.argv[2],
        }