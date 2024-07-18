#!/bin/python3
#-*- coding: utf-8 -*-

from tools import file
from tools import config

'''
a tools for rename all files in a folder, like (1).mp4 to 1.mp4
it only tested on windows

一个工具函数，用于重命名文件夹中的所有文件，例如将(1).mp4重命名为1.mp4
只在windows上测试过
'''

def main():
    sys_args = config.sys_args()
    file.rename_all_files_in_folder(sys_args['work_file'])

if __name__ == '__main__':
    main()