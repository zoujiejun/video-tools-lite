#!/bin/python3
#!-*- coding: utf-8 -*-

import os


def rename_all_files_in_folder(folder_path):
    for file in os.listdir(folder_path):
        rename_file_name(os.path.join(folder_path, file))

'''
a function rename file name (1).mp4 to 1.mp4
'''
def rename_file_name(file_path):
    file_names = os.path.basename(file_path).split('.')
    new_file_name = file_names[0].strip().lstrip('(').rstrip(')')
    full_name = os.path.join(os.path.dirname(file_path), new_file_name + '.' + file_names[1])
    return os.rename(file_path, full_name)