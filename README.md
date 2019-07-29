# RandomOpenVideo
## 1、简介
你是否有小电影太多，到用时不知道该看哪个的烦恼呢？  
你是否有小电影太多，到用时不方便寻找的烦难呢？  
本软件就是为了这个问题！   
本软件拥有图形用户界面，可以获取指定目录下的全部视频，并能够实现搜索过滤和随机打开一个视频的功能，同时支持播放指定视频。
本软件目前只有mac版，不过GUI使用tkinter编写，软件编译成Windows版本基本无需改动，需要改动的是数据文件存放的目录。可下载[源代码](https://raw.githubusercontent.com/skjgsk/RandomOpenVideo/master/GuiRandomFile.py)自行尝试。如果有Windows用户有需求可以发Issues，没有需要我就不多此一举了。  
<div align="center">
  <img src="https://github.com/skjgsk/RandomOpenVideo/blob/master/img/main_window.png" width="400"/>
  <div>软件界面</div>
</div>   
## 2、使用方法
初次使用软件会在`/Users/用户名/Library/软件名/`目录下生成`video_type.txt`和`video_list.txt`两个文件，分别用于存放视频类型和视频列表，`video_type.txt`里存放的是视频后缀名，可以自行添加删除，不在`video_type.txt`中的文件后缀在扫描时不会加入列表。

