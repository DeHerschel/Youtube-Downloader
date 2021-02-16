#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import pytube
import sys
import moviepy.editor as mp
import os
from os import remove
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("URL", help="Video URL")
parser.add_argument("--mp3", help="Convert video to mp3", action="store_true")
parser.add_argument("--wav", help="Convert video to wav", action="store_true")
parser.add_argument("-dir", "--directory", help="Directory to save the download (Default ~/Downloads)")
arg = parser.parse_args()

#Directory to save the download
dir = os.path.expanduser("~/")
url = arg.URL
if arg.mp3:
    print("Convert to mp3")
if arg.directory:
    dir = arg.directory+"/"

try:
    video=pytube.YouTube(url)
except:
    print("Error: "+url+" is ot a valid URL")
    sys.exit(1)

title=video.title
title = title.replace(",","")
title = title.replace("'","")
#Doenload the video in the actual directory
video.streams.first().download(dir)
#Name of the downloaded video
dwn_video = dir+title + ".mp4"

#Get the video
to_convert = mp.VideoFileClip(dwn_video)
#Convert to audio
if arg.mp3:
    to_convert.audio.write_audiofile(dir + title + ".mp3")
    #remove downloaded video
    remove(dwn_video)
if arg.wav:
    to_convert.audio.write_audiofile(dir + title + ".wav")
    #remove downloaded video
    remove(dwn_video)
