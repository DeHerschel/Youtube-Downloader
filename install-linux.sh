#! /usr/bin/env bash
USER_HOME=$(eval echo ~${SUDO_USER})
if [ "$EUID" -ne 0 ]; then
        echo "Error. Execute as root"
        exit 1
fi
echo "Installing python3-pil python3-pil.imaget...."
apt-get install python3-pil python3-pil.imagetk > /dev/null
echo "Checking python3 and pip3..."
if [ $(which pip3 | wc -l) -eq 0 ]; then
	echo "inatalling python3 and pip3"
	apt-get install python3 pip3
	"Installing pip module moviepy..."
	pip3 install moviepy
	"Installing pip module argparse..."
	pip3 install argparse
	"Installing pip module pytube..."
	pip3 install pytube
else
	"Checking pip modules..."
	if [ $(pip3 list | grep moviepy | wc -l) -eq 0 ]; then
		"Installing pip module moviepy..."
		pip3 install moviepy
        fi
	if [ $(pip3 list | grep argparse | wc -l) -eq 0 ]; then
		"Installing pip module argparse..."
                pip3 install argparse
        fi
	if [ $(pip3 list | grep pytube | wc -l) -eq 0 ]; then
		"Installing pip module pytube..."
                pip3 install pytube
        fi

fi

path=$(readlink -f $0);
path=$(dirname $path);
desk="$USER_HOME/.local/share/applications/yt-downloader.desktop"
cp -r $path/Linux $USER_HOME/.local/yt-downloader
mv $USER_HOME/.local/yt-downloader/Console/yt-downloader.py $USER_HOME/.local/yt-downloader/Console/yt-downloader
ln -s $USER_HOME/.local/yt-downloader/Console/yt-downloader /usr/local/bin/yt-downloader

echo "[Desktop Entry]" >> "$desk"
echo "Version=1.0" >> "$desk"
echo "Name=Youtube Downloader" >> "$desk"
echo "Comment=Simple GUI Youtube Dowloader by Emile DeHerschel" >> "$desk"
echo "Exec=python3 '$USER_HOME/.local/yt-downloader/GUI/yt-downloader.py'" >> "$desk"
echo "Icon=$USER_HOME/.local/yt-downloader/GUI/icon.png" >> "$desk"
echo "Terminal=false" >> "$desk"
echo "Type=Application" >> "$desk"
echo "Categories=Application;"  >> "$desk"
PATH=$PATH
