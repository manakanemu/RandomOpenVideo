# RandomOpenVideo
## 1、简介
* 你是否有小电影太多，到用时不知道该看哪个的烦恼呢？  
* 你是否有小电影太多，到用时不方便寻找的烦难呢？  
* 本软件就是为了这个问题！   
本软件拥有图形用户界面，可以获取指定目录下的全部视频，并能够实现搜索过滤和随机打开一个视频的功能，同时支持播放指定视频。本软件目前只有mac版，不过GUI使用tkinter编写，软件编译成Windows版本基本无需改动，需要改动的是数据文件存放的目录。可下载[源代码](https://raw.githubusercontent.com/skjgsk/RandomOpenVideo/master/GuiRandomFile.py)自行尝试。如果有Windows用户有需求可以发Issues，没有需要我就不多此一举了。  
<div align="center">
  <img src="https://github.com/skjgsk/RandomOpenVideo/blob/master/img/main_window.png" width="400"/>
  <div>软件界面</div>
</div>  

## 2、安装方法  
下载后直接解压即可使用GuiRandomFile.app，初次使用软件会要求指定视频存放的跟目录和搜索深度，进而创建视频列表。  
1)初次打开软件，会要求选择视频根目录：
<div align="center">
  <img src="https://github.com/skjgsk/RandomOpenVideo/blob/master/img/select_search_path.png" width="400"/>
  <div>选择根目录</div>
</div>  

2)然后选择搜索深度。最小为0，表示仅搜索根目录，为1表示仅向下进入一层文件夹，为2表示向下进入两层，以此类推。  
<div align="center">
  <img src="https://github.com/skjgsk/RandomOpenVideo/blob/master/img/select_search_deep.png" width="400"/>
  <div>选择搜索深度</div>
</div>   

3)之后软件会开始搜索视频列表，请耐心等待。待搜索完毕后，生成的视频列表回显示在软件的“视频列表”中，生成好“视频列表”后，即可开始正式使用软件。  
## 3、使用方法
<div align="center">
  <img src="https://github.com/skjgsk/RandomOpenVideo/blob/master/img/using.png" width="400"/>
  <div>正常使用界面</div>
</div> 

**每个按钮对应功能就如按钮文字所示，文字后括号内的内容是按钮的全局快捷键，例如打开视频的快捷键是回车。**
* 打开视频(↩︎)  

软件会随机选中“视频列表”中的一个视频，然后用系统设置的默认打开方式打开视频。最近打开的视频会显示在软件最下方的“历史记录”中。你也可以**指定具体打开哪个视频**，方法是点选“视频列表”或“历史记录”中的条目，然后点击“打开视频”按钮或直接按下回车，即可打开指定视频。
* 打开配置文件目录  

打开配置文件所在目录。软件在搜索完创建视频列表后，会在用户目录下生成`video_type.txt`和`video_list.txt`两个配置文件，分别用于存放视频类型和视频列表，`video_list.txt`里存放的是视频列表，可以手动添加，但如非必要，请不要随意修改。`video_type.txt`中存放的是视频文件的后缀，只有视频文件的后缀在`video_type.txt`中，才会被添加到“视频列表”中，可以手动修改`video_type.txt`中的内容，以指定保留什么文件，文件格式为：每行一个文件后缀。  
* 删除视频  

软件提供删除视频的功能，为防止误触键盘，本功能没有快捷键。若要删除视频，是先选定“历史记录”或“视频列表”中的视频，然后点击“删除视频”按钮。该按钮自动禁止了连续点按，每次删除必须重新在“历史记录“或“视频列表”中选择。  
* 更新视频列表(r)  

点击更新视频列表按钮，可以重新指定视频根目录和搜索深度，详见“2、安装方法”中的步骤。
* 视频列表过滤

在输入框中输入要进行过滤的关键词，“视频列表”中会显示包含所输入的关键词的选项。随机打开视频功能仅会在过滤后的视频中随机选择要打开的视频。


