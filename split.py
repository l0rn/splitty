#!/usr/bin/env python3
'''
A script to batch split video files into its chapters using ffmpeg
'''

import subprocess
import argparse
import os
import json

def get_chapter_times(file_path):
    command = [
        'ffprobe', 
        '-v', 'quiet', 
        '-print_format', 'json', 
        '-show_chapters', 
        file_path
    ]
    result = subprocess.run(command, stdout=subprocess.PIPE)
    chapters = json.loads(result.stdout)['chapters']
    return [(float(chapter['start_time']), float(chapter['end_time'])) for chapter in chapters]

def split_video(file_path, chapter_times, merge_first, merge_last):
    base_name = os.path.splitext(os.path.basename(file_path))[0]
    for i in range(len(chapter_times)):
        start, end = chapter_times[i]
        if i < merge_first - 1:
            continue
        elif i == merge_first - 1:
            start = chapter_times[0][0]
        if i >= len(chapter_times) - merge_last:
            end = chapter_times[-1][1]
        output_file = f"{base_name}_chapter_{i+1}.mkv"
        command = [
            'ffmpeg', 
            '-i', file_path, 
            '-ss', str(start), 
            '-to', str(end), 
            '-c', 'copy', 
            output_file
        ]
        subprocess.run(command)

def main():
    parser = argparse.ArgumentParser(description='Split video files into chapters.')
    parser.add_argument('files', metavar='F', type=str, nargs='+', help='The video files to split')
    parser.add_argument('-mf', '--merge-first', type=int, default=0, help='The number of chapters to merge into the first output file')
    parser.add_argument('-ml', '--merge-last', type=int, default=0, help='The number of chapters to merge into the last output file')

    args = parser.parse_args()

    for file_path in args.files:
        chapter_times = get_chapter_times(file_path)
        split_video(file_path, chapter_times, args.merge_first, args.merge_last)

if __name__ == "__main__":
    main()
    
