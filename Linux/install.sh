#! /usr/bin/env bash

if [ "$EUID" -ne 0 ]; then
        echo "Error. Execute as root"
        exit 1
fi

if [ $(which pip3 | wc -l) -eq 0 ]; then
	apt-get install python3 pip3
	pip3 install moviepy
	pip3 install argparse
	pip3 install pytube
else
	if [ $(pip3 list | grep moviepy | wc -l) -eq 0 ]; then
		pip3 install moviepy
        fi
	if [ $(pip3 list | grep argparse | wc -l) -eq 0 ]; then
                pip3 install argparse
        fi
	if [ $(pip3 list | grep pytube | wc -l) -eq 0 ]; then
                pip3 install pytube
        fi

fi
path=$(readlink -f $0);
path=$(dirname $path);
desk="~/.local/share/applications/yt-downloader.desktop"

echo "[Desktop Entry]" >> "$desk"
echo "Version=1.0" >> "$desk"
echo "Name=Youtube Downloader" >> "$desk"
echo "Comment=Simple GUI Youtube Dowloader by Emile DeHerschel" >> "$desk"
echo "Exec=python3 '$path/GUI/yt-downloader.py'" >> "$desk"
echo "Icon=$path/GUI/icon.png" >> "$desk"
echo "Terminal=false" >> "$desk"
echo "Type=Application" >> "$desk"
echo "Categories=Application;"  >> "$desk"
