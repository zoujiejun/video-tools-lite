#!/bin/python3
#!-*- coding: utf-8 -*-

import os


def len_windows(ffmpeg_path, video_path):
    cmd = f'{ffmpeg_path} -i "{video_path}" 2>&1 | findstr "Duration"'
    output = os.popen(cmd).read()
    duration = output.split(',')[0].split(': ')[1]
    return duration

def len_linux(ffmpeg_path, video_path):
    cmd = f'{ffmpeg_path} -i "{video_path}" 2>&1 | grep "Duration"'
    output = os.popen(cmd).read()
    duration = output.split(',')[0].split(': ')[1]
    return duration

def len(ffmpeg_path, video_path):
    if os.name == 'nt': return len_windows(ffmpeg_path, video_path)
    else: return len_linux(ffmpeg_path, video_path)