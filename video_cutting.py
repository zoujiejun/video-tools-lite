#!/bin/python3
#  -*- coding: utf-8 -*-

import os
from tools import config
from tools import video

def main():
    root_config = config.load()
    sys_args = config.sys_args()
    cutting_config = root_config['cutting']
    cutting(root_config['ffmpeg_path'], sys_args['work_file'], cutting_config['output_path'], cutting_config['duration'])

'''
Use the FFmpeg tool to cut the video into multiple segments, each segment lasting duration seconds.
'''
def cutting(ffmpeg_path, video_path, output_path, duration=60):
    output_path = os.path.join(output_path, os.path.basename(video_path).split('.')[0])
    if not os.path.exists(output_path): os.makedirs(output_path)

    video_length = video.len(ffmpeg_path, video_path)
    video_seconds = int(video_length.split(':')[0]) * 3600 + int(video_length.split(':')[1]) * 60 + int(float(video_length.split(':')[2]))
    for i in range(0, video_seconds, duration): os.system(f'{ffmpeg_path} -i "{video_path}" -ss {i} -t {duration} -c copy "{output_path}\\{i // duration}.mp4"')
    print(f'Cutting video "{video_path}" into {video_seconds // duration} segments, each segment lasting {duration} seconds.')


if __name__ == "__main__": main()
