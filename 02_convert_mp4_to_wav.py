#!/usr/bin/env python

"""
Convierte archivos a formato wav
"""
import os

__author__ = 'ma0'

mp4_path = "output_folder"
convert_path = "wav"
so_path_separator = "/"


def recursive_convert(path, root_dir):
    new_path = os.path.join(root_dir, path)
    convert_new_path = os.path.join(convert_path, new_path)
    print(new_path)
    if os.path.isdir(new_path):
        if not os.path.exists(convert_new_path):
            os.makedirs(convert_new_path)
        dirs = os.listdir(new_path)
        for directory in dirs:
            recursive_convert(directory, os.path.join(root_dir, path))
    else:
        # if (root_dir+so_path_separator+path).endswith(".wav"):
        #     os.popen("rm %s" % root_dir+so_path_separator+path)
        print(new_path)
        if "3gp" in path:
            if not os.path.exists(convert_new_path.replace(".3gp", "_3gp.wav")):
                os.popen(
                    "ffmpeg -i %s -qscale 0 -ab 64k -ar 16000 %s" %
                    (
                        new_path,
                        convert_new_path.replace(".3gp", "_3gp.wav")
                    )
                )
            else:
                print("File already converted")
        elif "mp4" in path:
            if not os.path.exists(convert_new_path.replace(".mp4", ".wav")):
                os.popen(
                    "ffmpeg -i %s -qscale 0 -ab 64k -ar 16000 %s" %
                    (
                        new_path,
                        convert_new_path.replace(".mp4", ".wav")
                    )
                )
            else:
                print("File already converted")


recursive_convert("", mp4_path)
