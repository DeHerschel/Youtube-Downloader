#!/usr/bin/env python3ve

#import PySimpleGUI as sg
#
#
#class int:
#    def __init__(self):
#        sg.theme('LightGrey1')
#        layout = [
#
#                [sg.Text(" ", justification='center')],
#                [sg.Text("Youtube Downloader", size=(70, 2), justification='center')],
#                [sg.Text("URL:       "), sg.InputText(key="url", size=(50,10))],
#                [sg.Text(" ", size=(50, 1), justification='center')],
#                [sg.Text("Directory: "), sg.InputText(key="dir", size=(50,1)),  sg.FolderBrowse()],
#                [sg.Text(" ", size=(50, 1), justification='center')],
#                [sg.Text("Formato:  "), sg.InputCombo(("Video", ".mp3", ".wav"), size=(40, 1)), sg.OK()],
#                ]
#
#        self.window = sg.Window("Youtube Downloader", default_element_size=(40, 1), grab_anywhere=False)
#        self.window.Layout(layout).Finalize()
#        event, value = self.window.read()
#gui = int()

#################################################
import tkinter as tk
import tkinter.ttk as ttk
from tkinter import filedialog
import pytube
import sys
import os
import moviepy.editor as mp
from os import remove
import argparse




class GraphApp:
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
        self.format_label.configure(background='#f0f0f0', font='{Liberation Serif} 14 {}', text='Format:')
        self.format_label.place(anchor='nw', x='25', y='280')
        self.format_box = ttk.Combobox(self.frame_1)
        self.format_box.configure(values='"Video" ".mp3" ".wav"')
        self.format_box.place(anchor='nw', height='35', x='15', y='320')
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
        self.window.configure(background='#f0f0f0', height='500', width='500')
        self.window.resizable(False, False)

        # Main widget
        self.mainwindow = self.window

    def browse_files(self):
        self.path = filedialog.askdirectory()
        _text_ = self.path
        self.dir_input.insert('0', _text_)

    def paste(self):
        pass

    def download(self):
        try:
            url = self.url_input.get()
            print(url)
            video = pytube.YouTube(url)
            title=video.title
            video.streams.first().download(self.path)
        except:
            self.url_error.configure(background='#f0f0f0', foreground='#e60031', text='You need to to enter a valid URL. Like https//youtube.com/a2dr3')
            self.url_error.place(anchor='nw', x='25', y='160')

    def run(self):
        self.mainwindow.mainloop()

if __name__ == '__main__':
    app = GraphApp()
    app.run()
