#!/usr/bin/env python3ve

#################################
#           LIBRARIES           #
#################################
import os
from os import remove
import sys
import tkinter as tk
import tkinter.ttk as ttk
from tkinter import filedialog
import asyncio
import pytube
import moviepy.editor as mp
import argparse
import threading



#Path of the program used for the icon
filePath = __file__[:-12]
iconPath = filePath + "icon.png"


##################################
#          FUNCTIONS             #
##################################

def download_engine():
    url = Window.videoUrl
    video = Window.video
    title = video.title
    convert = Window.format_box.get()
    title = video.title
    title = title.replace(",","")
    title = title.replace("'","")
    if convert == ".mp3" or convert == ".wav":
        #Download video in actual directory
        video.streams.first().download()
        #Name of the downloaded video
        dwn_video = title + ".mp4"
        #get the Video
        to_convert = mp.VideoFileClip(dwn_video)
        if convert == ".mp3":
            to_convert.audio.write_audiofile(Window.path + title + ".mp3")
            remove(dwn_video)
        else:
            to_convert.audio.write_audiofile(Window.path + title + ".wav")
            remove(dwn_video)
    else: #.mp4
        video.streams.first().download(Window.path)

#check periodically
def schedule_check(t):
    Window.window.after(1000, check_if_done, t)

def check_if_done(t):
    # if the new thread has finished...
    if not t.is_alive():
        #Restart button
        Window.downloading.configure(background='#f0f0f0', font='{FreeSans} 14 {}', foreground='#00d800', text='Downloaded!!')
        Window.downloading.place(anchor='nw', width='200', x='150', y='380')
        Window.download_button["state"] = "normal"
        Window.progressbar.stop()
    else:
        #check again
        schedule_check(t)


###################################
#       INTERFACE CLASS           #
###################################

class user_interface:
    def __init__(self, master=None):
        # build ui
        self.window = tk.Tk() if master is None else tk.Toplevel(master)
        self.frame_1 = tk.Frame(self.window)
        self.url_label = tk.Label(self.frame_1)
        self.url_label.configure(background='#f0f0f0', font='{Liberation Serif} 14 {}', text='URL:')
        self.url_label.place(anchor='nw', x='25', y='80')
        self.url_input = tk.Entry(self.frame_1)
        self.url_input.place(anchor='nw', height='35', width='300', x='15', y='120')
        self.url_error = tk.Label(self.frame_1)
        self.dir_label = tk.Label(self.frame_1)
        self.dir_label.configure(background='#f0f0f0', font='{Liberation Serif} 14 {}', text='Directory:')
        self.dir_label.place(anchor='nw', x='25', y='180')
        self.dir_input = tk.Entry(self.frame_1)
        self.dir_input.place(anchor='nw', height='35', width='300', x='15', y='220')
        self.format_label = ttk.Label(self.frame_1)
        self.format_label.configure(background='#f0f0f0', font='{C059} 14 {}', text='Format:')
        self.format_label.place(anchor='nw', x='70', y='280')
        self.format_box = ttk.Combobox(self.frame_1)
        self.format_box = ttk.Combobox(self.frame_1)
        self.format_box.configure(values='"Video" ".mp3" ".wav"')
        self.format_box.place(anchor='nw', height='35', width='120', x='60', y='320')
        self.progressbar = ttk.Progressbar(self.frame_1)
        self.progressbar.configure(length='100', mode='indeterminate', orient='horizontal')
        self.progressbar.place(anchor='nw', height='35', width='400', x='40', y='420')
        self.download_button = tk.Button(self.frame_1)
        self.download_button.configure(activebackground='#3c90eb', activeforeground='#ffffff', background='#3c90eb', foreground='#ffffff')
        self.download_button.configure(highlightbackground='#1489ff', highlightcolor='#00a0ff', text='Download!')
        self.download_button.place(anchor='nw', height='35', width='130', x='310', y='320')
        self.download_button.configure(command=self.download)
        self.dir_button = tk.Button(self.frame_1)
        self.dir_button.configure(activebackground='#3c90eb', activeforeground='#ffffff', background='#3c90eb', foreground='#ffffff')
        self.dir_button.configure(highlightbackground='#1489ff', highlightcolor='#00a0ff', text='Browse')
        self.dir_button.place(anchor='nw', width='80', x='350', y='222')
        self.dir_button.configure(command=self.browse_files)
        self.paste_button = tk.Button(self.frame_1)
        self.paste_button.configure(activebackground='#3c90eb', activeforeground='#ffffff', background='#3c90eb', foreground='#ffffff')
        self.paste_button.configure(highlightbackground='#1489ff', highlightcolor='#00a0ff', text='Paste')
        self.paste_button.place(anchor='nw', width='80', x='350', y='122')
        self.paste_button.configure(command=self.paste)
        self.label_5 = tk.Label(self.frame_1)
        self.label_5.configure(background='#ff0000', font='{Ubuntu Condensed} 14 {bold}', foreground='#ffffff', text='TUBE')
        self.label_5.place(anchor='nw', x='223', y='20')
        self.tittle_down = tk.Label(self.frame_1)
        self.tittle_down.configure(background='#f0f0f0', font='{Noto Sans Mono CJK TC} 14 {}', text='DOWNLOADER')
        self.tittle_down.place(anchor='nw', x='184', y='46')
        self.frame_1.configure(background='#f0f0f0', height='500', width='500')
        self.frame_1.place(anchor='nw', x='0', y='0')
        self.title = tk.Label(self.window)
        self.title.configure(background='#f0f0f0', font='{Ubuntu Condensed} 14 {}', foreground='#000000', text='YOU')
        self.title.place(anchor='nw', x='190', y='20')
        self.downloading = tk.Label(self.window)
        self.window.configure(background='#f0f0f0', height='500', width='500')
        self.window.resizable(False, False)
        self.icon_png = tk.PhotoImage(file=iconPath)
        self.window.iconphoto(True, self.icon_png)
        self.window.title('Youtube-Downloader')

        # Main widget
        self.mainwindow = self.window

    def browse_files(self): #Browse button
        path = filedialog.askdirectory() #ask dir
        _text_ = path
        self.dir_input.insert('0', _text_)
        self.path = path + "/"

    def paste(self): #Function for paste button
        self.url_input.delete('0', 'end')
        paste = self.window.clipboard_get()
        self.url_input.insert('0', paste)

    def download(self): #function for download button
            self.videoUrl = self.url_input.get()
            self.video = pytube.YouTube(self.videoUrl)
            self.videoTitle = self.video.title
            #Execute download_engine function in a new thread
            t = threading.Thread(target=download_engine)
            t.start()
            #check
            schedule_check(t)
            self.progressbar.start()
            self.download_button["state"] = "disabled"
            self.downloading.configure(background='#f0f0f0', font='{FreeSans} 14 {}', foreground='#000000', text='Downloading '+self.videoTitle)
            self.downloading.place(anchor='nw', width='400', x='40', y='380')


    def run(self):
        self.mainwindow.mainloop()


#################################
#           MAIN                #
#################################
if __name__ == '__main__':
    Window = user_interface()
    Window.run()
