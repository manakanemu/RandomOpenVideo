#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import tkinter as tk
from tkinter import simpledialog
from tkinter import filedialog
import random
import os
import sys
import re


def openFile(filePath: str):
    platform = sys.platform.lower()
    filePath = '"' + filePath + '"'
    try:
        if platform.find("darwin") > -1:
            os.system("open " + filePath)
        elif platform.find("win32") > -1:
            os.startfile(filePath)
    except:
        pass


def cal_deep(file_path: str):
    file_path = file_path.replace(work_path, '')
    return file_path.count('/') - 1


def save_video_list(content: list):
    file = open(conf_path + 'video_list.txt', 'w', encoding='utf-8')
    for video in content:
        file.write(video + '\n')
    file.close()


def get_file_list(path, self):
    file_list = [path + x for x in os.listdir(path)]
    i = 0
    while i < len(file_list):
        if (cal_deep(file_list[i]) > DEEP):
            file_list.pop(i)
            continue
        if os.path.isdir(file_list[i]):
            file_list += [file_list[i] + '/' + x for x in os.listdir(file_list[i])]
            file_list.pop(i)
            continue
        global window
        i += 1
    return file_list


def get_video_type():
    if not os.path.exists(conf_path + 'video_type.txt'):
        vt = ['mp4', 'm4v', 'flv', 'avi', 'mov', 'mkv', 'rmvb', 'rm', 'asf', 'wmv']
        file = open(conf_path + 'video_type.txt', 'w', encoding='utf-8')
        for v in vt:
            file.write(v + '\n')
        file.close()

    file = open(conf_path + 'video_type.txt', 'r')
    vt = file.read().strip().split('\n')
    file.close()
    return vt


def get_video_list(file_list: list):
    video_type = get_video_type()
    video_list = []
    for file in file_list:
        try:
            file_type = re.search(r'\.([0-9a-zA-Z]{0,4})$', file).group(1)
            if file_type in video_type:
                video_list.append(file)
        except:
            pass
    video_list.sort()
    return video_list


def new_video_list(self):
    new_list = get_video_list(get_file_list(work_path + '/', self))
    save_video_list(new_list)


class Window():
    def __init__(self, width=500, height=700, title='随机视频'):
        self.window = tk.Tk()
        self.window.title = title
        self.window_size = (width, height)
        x = (self.window.winfo_screenwidth() - width) // 2
        y = (self.window.winfo_screenheight() - height) // 2
        self.window.geometry('{}x{}+{}+{}'.format(str(width), str(height), str(x), str(y - 20)))
        self.create_widget()
        self.init_widget()
        self.bind_event()
        self.selected = None
        self.is_selected = False
        self.random = 0

    def create_widget(self):
        miniside = 10
        bigside = 120
        textsize = 30
        buttonsize = 30
        # 状态标签
        self.info_label = tk.Label(self.window, text='选择操作:')
        self.info_label.place(x=miniside, y=3)
        # 文件目录文本框
        self.filepath_entry = tk.Entry(self.window, width=100, takefocus=False)
        self.filepath_entry.place(x=miniside, width=self.window_size[0] - 2 * miniside, y=textsize - 5)

        # 打开视频按钮
        self.openfile_button = tk.Button(self.window, text='打开视频(↩︎)', takefocus=False,default=tk.ACTIVE,fg='white')
        self.openfile_button.place(x=bigside, width=self.window_size[0] - 2 * bigside,
                                   y=buttonsize + textsize)
        # 打开目录按钮
        self.opendir_button = tk.Button(self.window, text='打开配置文件目录', takefocus=False)
        self.opendir_button.place(x=bigside, width=self.window_size[0] - 2 * bigside,
                                  y=2 * buttonsize + textsize)
        # 删除视频按钮
        self.delet_button = tk.Button(self.window, text='删除视频', takefocus=False)
        self.delet_button.place(x=bigside, width=self.window_size[0] - 2 * bigside,
                                y=3 * buttonsize + textsize)
        # 更新视频列表按钮
        self.renewlist_button = tk.Button(self.window, text='更新视频列表(r)', takefocus=False)
        self.renewlist_button.place(x=bigside, width=self.window_size[0] - 2 * bigside,
                                    y=4 * buttonsize + textsize)

        # 文件列表变量
        self.filelist_var = tk.Variable()

        # 文件列表标签
        tk.Label(self.window, text='视频列表:').place(x=miniside, y=5 * buttonsize + textsize)

        # 搜索框
        self.search_var = tk.Variable()
        self.search_entry = tk.Entry(self.window, width=100, takefocus=False,textvariable=self.search_var)
        self.search_entry.place(x=miniside+100,width = 380, y=5 * buttonsize + textsize-2)

        # 文件列表
        self.filelist_listbox = tk.Listbox(self.window, listvariable=self.filelist_var, height=17, takefocus=False)
        self.filelist_listbox.place(x=miniside, y=6 * buttonsize + textsize, width=self.window_size[0] - 2 * miniside)

        # 历史记录标签
        tk.Label(self.window, text='历史记录:').place(x=miniside, y=480 + textsize)

        # 历史记录变量
        self.history_var = tk.Variable()

        # 历史记录列表
        self.history_listbox = tk.Listbox(self.window, listvariable=self.history_var, height=8, takefocus=False)
        self.history_listbox.place(x=miniside, y=515 + textsize, width=self.window_size[0] - 2 * miniside)

    def bind_event(self):
        self.window.bind('<Return>', self.open_file_event)
        self.window.bind('<KeyPress-r>', self.renew_list_event)
        self.window.bind('<KeyPress-R>', self.renew_list_event)

        self.openfile_button.bind('<Button-1>', self.open_file_event)
        self.opendir_button.bind('<Button-1>', self.open_dir_event)
        self.delet_button.bind('<Button-1>', self.delete_event)
        self.renewlist_button.bind('<Button-1>', self.renew_list_event)
        self.filelist_listbox.bind('<<ListboxSelect>>', self.file_list_event)
        self.history_listbox.bind('<<ListboxSelect>>', self.history_event)
        self.search_var.trace('w', self.search)
    def init_widget(self):
        self.set_info('初始化程序...')
        self.filepath_entry.config(state=tk.DISABLED)
        self.init_filelist_listbox()
        self.history_listbox.config(state=tk.DISABLED)
        self.search_var.set('')

    def init_filelist_listbox(self):
        self.set_info('初始化视频列表...')
        global video_list
        if not os.path.exists(conf_path + 'video_list.txt'):
            self.set_info('正在创建视频列表...')
            global work_path
            global DEEP
            work_path = filedialog.askdirectory(title='选择视频跟目录')
            if work_path == '':
                raise Exception('work_path must be seleted')
            DEEP = int(simpledialog.askinteger('视频目录:' + work_path, '请输入视频目录最大深度'))
            print(DEEP)
            new_video_list(self)

        file = open(conf_path + 'video_list.txt', 'r', encoding='utf-8')
        content = file.read().strip()
        file.close()
        video_list = content.split('\n')
        self.search()
        if video_list[0] == '':
            self.set_info('已加载{}个视频'.format(0))
        else:
            self.set_info('已加载{}个视频'.format(len(video_list)))

    def set_filelist_listbox(self, content: list):
        self.filelist_var.set(content)

    def set_history_listbox(self, content: list):
        self.history_listbox.config(state=tk.NORMAL)
        self.history_var.set(content)

    def get_file_list_select(self):
        value = self.filelist_listbox.get(self.filelist_listbox.curselection())
        return str(value).strip()

    def get_hisroty_select(self):
        value = self.history_listbox.get(self.history_listbox.curselection())
        return str(value).strip()

    def set_entry(self, text=None):
        self.filepath_entry.config(state=tk.NORMAL)
        self.filepath_entry.delete(0, 'end')
        if text != None:
            self.filepath_entry.insert('end', text)
        else:
            self.filepath_entry.insert('end', self.selected)
        self.filepath_entry.config(state=tk.DISABLED)

    def get_entry(self):
        value = self.filepath_entry.get()
        return str(value).strip()

    def set_info(self, info):
        self.info_label['text'] = info

    def set_focus(self):
        self.openfile_button.focus_set()

    def run(self):
        self.window.mainloop()

    def open_file_event(self, event):
        if not self.is_selected:
            rand_num = random.randint(0, len(box_list) - 1)
            while abs(self.random - rand_num) < (len(box_list) / 100):
                rand_num = random.randint(0, len(box_list) - 1)
            self.random = rand_num
            self.selected = box_list[self.random]

        openFile(self.selected)
        self.set_info('打开视频:')
        self.set_entry(self.selected)
        self.is_selected = False
        index = box_list.index(self.selected)
        self.filelist_listbox.select_clear(0, 'end')
        self.filelist_listbox.select_set(index)
        self.filelist_listbox.see(index)
        global history_list
        history_list.insert(0, self.selected)
        if len(history_list) > 8:
            history_list.pop()
        self.set_history_listbox(history_list)

    def open_dir_event(self, event):
        openFile(conf_path)
        self.is_selected = False

    def delete_event(self, event):
        try:
            if self.is_selected:
                video = self.selected
                os.remove(video)
                video_list.remove(video)
                save_video_list(video_list)
                self.search()
                self.set_info('已删除:{}'.format(video))
                self.set_entry('')
                self.is_selected = False
                global history_list
                i = 0
                while i < len(history_list):
                    if history_list[i] == video:
                        history_list.pop(i)
                        continue
                    i += 1
                self.set_history_listbox(history_list)

        except:
            pass

    def renew_list_event(self, event):
        global video_list
        self.set_info('正在创建视频列表...')
        global DEEP
        global work_path
        work_path = filedialog.askdirectory(title='选择视频跟目录')
        if work_path == '':
            raise Exception('work_path must be seleted')
        DEEP = int(simpledialog.askinteger('视频目录', '请输入视频目录最大深度'))
        new_video_list(self)
        file = open(conf_path + 'video_list.txt', 'r', encoding='utf-8')
        content = file.read().strip()
        file.close()
        video_list = content.split('\n')
        self.search()
        if video_list[0] == '':
            self.set_info('更新视频列表完成，已加载{}个视频'.format(0))
        else:
            self.set_info('更新视频列表完成，已加载{}个视频'.format(len(video_list)))
        self.selected = None
        self.is_selected = False
        global history_list
        history_list = []
        self.set_history_listbox(history_list)
        self.history_listbox.config(state=tk.DISABLED)

    def file_list_event(self, event):
        self.selected = self.get_file_list_select()
        self.is_selected = True
        print(self.selected)

    def history_event(self, event):
        self.selected = self.get_hisroty_select()
        self.is_selected = True
        print(self.selected)

    def search(self, *args):
        key = str(self.search_var.get()).strip()
        global box_list
        box_list = []
        if key == '':
            box_list = video_list
        else:
            for video in video_list:
                if video.find(key) != -1:
                    box_list.append(video)
        self.set_filelist_listbox(box_list)
        self.is_selected = False



box_list = []
video_list = []
history_list = []
video_type = []

argv = sys.argv[0]
print('1' + argv)
try:
    argv = re.search(r'.+\.app', argv).group(0)
except:
    print('error')
    pass
print('2' + argv)
work_path = ''
conf_path = os.environ['HOME'] + '/Library/Application Support/' + os.path.splitext(os.path.split(argv)[1])[0] + '/'
if not os.path.exists(conf_path):
    os.makedirs(conf_path)
DEEP = 4
window = Window()
window.run()
