#!/bin/python3
#-*- coding: utf-8 -*-

import os
from tools import config

def main():
    root_config = config.load()
    sys_args = config.sys_args()

    merge_config = root_config['merge']
    video_list = get_video_list(sys_args['work_file'], merge_config['extname'])
    video_merge(root_config['ffmpeg_path'],video_list, merge_config['output_path'], merge_config['extname'])

'''
get file list from video directory
return a list of video file path
'''
def get_video_list(video_dir, extname):
    list = []
    for file in os.listdir(video_dir):
        if file.endswith('.' + extname):
            list.append(os.path.join(video_dir, file))

    # sort the list by file name
    list.sort(key=lambda x: int(os.path.splitext(os.path.basename(x))[0]))
    return list

'''
merge video with ffmpeg concat
input: a list of video file path, output path
output: merge the video into one video
'''
def video_merge(ffmpeg_path, video_list, output_path, extname):
    if video_list == []:
        print('No video file found!')
    output_path = os.path.join(output_path, os.path.basename(os.path.dirname(video_list[0])))
    if not os.path.exists(output_path):
        os.makedirs(output_path)

    
    final_video_path = os.path.join(output_path, 'final_video.' + extname)
    video_list_path = os.path.join(output_path, 'video_list.txt')
    
    with open(video_list_path, 'w') as f:
        for video in video_list:
            video = os.path.abspath(video)
            f.write(f'file \'{video}\'\n')

    status = os.system(f'{ffmpeg_path} -f concat -safe 0 -i {video_list_path} -c copy {final_video_path}')
    if status == 0:
        print(f'Video merged successfully! Output file: {final_video_path}')
    else:
        print('Video merge failed!')

if __name__ == '__main__': main()