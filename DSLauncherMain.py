import tkinter
from tkinter.messagebox import *
from tkinter import *
from tkinter import ttk
import os
import zipfile
import subprocess

ver='3'
cwd=os.getcwd()

root=Tk()
root.title('Darkstar Minecraft Launcher '+ver)
root.geometry('800x400')
root.resizable(False,False)
root.iconbitmap('launchericon.ico')
os.system('mkdir DSLauncherStatic')

notebook = tkinter.ttk.Notebook(root)
starttab = tkinter.Frame()
connecttab = tkinter.Frame()
notebook.add(starttab, text='启动')
notebook.add(connecttab, text='游戏外NatFrp联机')
notebook.pack(padx=80, pady=40, fill=tkinter.BOTH, expand=True)
javaroute='"'+cwd+'/DSMC Pack/java/bin/javaw.exe'

def downloadjava():
    print('传输链接：https://cowtransfer.com/s/5e80d5e5390040')
def downloadbedrock():
    print('传输链接：https://cowtransfer.com/s/6d0c64bd05bf46')
def unpack(targetfile):
    with zipfile.ZipFile(targetfile) as zf:
        try:
            zf.extractall()
            print('\n[WARN]Unpack Successfully.')
        except zipfile.BadZipFile:
            print('\n[ERROR]Failed when unpacking DSMCpck file')
def decompiled():
    showinfo('DSLauncher','请把DSMCJava.dsmcpck放到程序根目录中，然后按下确定\n警告：解压过程中请勿关闭程序！')
    print('='*20+'UNPACKING'+'='*20)
    try:
        unpack('./DSMCJava.dsmcpck')
        showinfo('DSLauncher - 提示','解包成功！')
        os.system('del DSMCJava.dsmcpck')
    except:
        showwarning('DSLauncher - 警告','找不到文件.')
def full():
    root.attributes("-fullscreen",'true')
    fullscreen.config(state=DISABLED,text='全屏模式已开启\n(点击左上角“退出”以离开)')
def dslwelcome():
    dw=showinfo('DSlauncher - 关于','Darkstar Minecraft Launcher v'+ver+'\n版权所有。Jeffery Darkstar, 2022')
def startfrompcl():
    print('='*10+'准备从PCL脚本启动'+'='*10)
    try:
        open(cwd+'\DSLauncherStatic\PCLLaunch.bat')
        print(checkVar.get())
        print(str(checkVar.get()))
        if str(checkVar.get()) == '1':
            with open(cwd+'/DSLauncherCache/StartAll.bat','a') as f:
                f.write('@echo off\nstart /D "'+cwd+'\DSLauncherStatic" PCLLaunch.bat\nstart /D "'+cwd+'" frpc.exe')
            root.withdraw()
            try:
                subprocess.run([cwd+'\DSLauncherCache\StartAll.bat'])
            except KeyboardInterrupt:
                root.deiconify()
        else:
            root.withdraw()
            try:
                subprocess.run([cwd+'\DSLauncherStatic\PCLLaunch.bat'])
            except KeyboardInterrupt:
                root.deiconify()
    except:
        showinfo('DSlauncher','你还没有设定PCL2启动脚本！')
def clearpcl():
    os.system('del DSLauncherStatic /q')
    showinfo('DSLauncher','PCL启动脚本已经清理！')
    root.destroy()
def startconnect():
    root.withdraw()
    try:
        subprocess.run([cwd+'/frpc.exe'])
    except FileNotFoundError:
        root.deiconify()
        root.update()
        showinfo('DSLauncher','联机模块已丢失')
def importsc():
    try:
        open(cwd+'/DSLauncherStatic/PCLLaunch.bat')
        root2=tkinter.Tk()
        root2.title('更改PCL2启动脚本')
        root2.geometry('600x200')
        root.destroy()
        titlesc=Label(root2,text='复制PCL目录下LatestLaunch.bat内所有内容，然后再按下下方的按钮。')
        titlesc.pack()
        def getentersc():
            def destroypg():
                f=open(cwd+'/DSLauncherStatic/PCLLaunch.bat','a')
                f.write(scget)
                root2.destroy()
            try:
                scget = root2.clipboard_get()
            except:
                showerror('错误','你还没有复制任何内容！')
            print('[INFO]GETTED PCL2 LAUNCH SCRIPT:'+scget)
            titlesc.configure(text='已加载启动脚本！请稍后重新启动程序！')
            confirmsc.config(text='应用并退出',command=destroypg)
        confirmsc=Button(root2,text='导入剪贴板内容',command=getentersc)
        confirmsc.pack()
        root2.mainloop()
    except:
        root2=tkinter.Tk()
        root2.title('加载PCL2启动脚本')
        root2.geometry('600x200')
        root.destroy()
        titlesc=Label(root2,text='复制PCL目录下LatestLaunch.bat内所有内容，然后再按下下方的按钮。')
        titlesc.pack()
        def getentersc():
            def destroypg():
                f=open(cwd+'/DSLauncherStatic/PCLLaunch.bat','a')
                f.write(scget)
                root2.destroy()
            try:
                scget = root2.clipboard_get()
            except:
                showerror('错误','你还没有复制任何内容！')
            print('[INFO]GETTED PCL2 LAUNCH SCRIPT:'+scget)
            titlesc.configure(text='已加载启动脚本！请稍后重新启动程序！')
            confirmsc.config(text='应用并退出',command=destroypg)
        confirmsc=Button(root2,text='导入剪贴板内容',command=getentersc)
        confirmsc.pack()
        root2.mainloop()
def startbedrock():
    print('准备从Bedrock启动')
def startpcl():
    print('启动PCL2')
    os.system('"'+cwd+'/PCL.exe"')

menu1 = Menu(starttab, tearoff=0)
menu1.add_command(label="下载Java安装包",command=downloadjava)
menu1.add_command(label="下载Bedrock安装包",command=downloadbedrock)
menu1.add_command(label="手动提前解编译Java包",command=decompiled)
menu1.add_command(label="编辑PCL2启动脚本...（备用）",command=importsc)
menu1.add_command(label="清除PCL启动脚本",command=clearpcl)
menu1.add_separator()
menu1.add_command(label="使用BedrockPack快速启动Minecraft（Win10）",command=startbedrock)
mebubar = Menu(starttab)
mebubar.add_command(label="DSlauncher", command=dslwelcome)
mebubar.add_cascade(label="启动器", menu=menu1)
mebubar.add_cascade(label="打开PCL2",command=startpcl)
mebubar.add_command(label="退出", command=root.quit)
root.config(menu=mebubar)

title=Label(starttab,text='Darkstar Minecraft Launcher '+ver,font=('微软雅黑','20'))
title.pack(anchor='n')
fullscreen=Button(starttab,text='全屏模式',command=full)
fullscreen.pack(anchor='ne')

title=Label(connecttab,text='联机',font=('微软雅黑','20'))
title.pack(anchor='n')
warnfrp=Label(connecttab,text='注意：联机服务由NatFrp提供，不属于DSLauncher管辖！游戏内修改端口信息请转到/Plugins的frpc.ini\n在连机过程中不要关闭DSLauncher!')
warnfrp.pack()
startfrpbt=Button(connecttab,text='开始跨局域网联机',command=startconnect)
startfrpbt.pack()
infofrp=Label(connecttab,text='使用配置文件：根目录/frpc.ini')
infofrp.pack()
checkVar = StringVar(value="0")
cbutOne = tkinter.Checkbutton(root, text="游戏启动后自动开启联机",variable=checkVar)
cbutOne.pack()

startwarn=Label(starttab,text='使用包体内置的PCL选择PACK内Minecraft启动，再转到PCL文件夹获取启动脚本。')
startwarn.pack()
startbutton=Button(starttab,text='          从PCL2脚本启动DSMC          ',height='3',command=startfrompcl)
startbutton.pack()
root.mainloop()