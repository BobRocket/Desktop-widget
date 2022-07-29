#项目名称：Desktop-widget
#开源地址：https://github.com/BobRocket/Desktop-widget
#作者：云里物理
#本项目根据GNU3.0通用公共开源许可证的条款发布
import tkinter as tk
import tkinter.messagebox
import time
import requests
import json
import os

t=time.gmtime()

lan = "chinese"
getData = []
 
def signUp(usrName, usrPwd):
    with open('data.txt','a') as usrFile:
        usrFile.writelines("{}\n{}\n".format(usrName, usrPwd))

def removeN():
    asd = " "
    c = ""
    bd = []
    de = 0
    fg = "\n"
    with open('data.txt','r') as usrFile:
        asd = usrFile.readlines()
        for j in range(len(asd)):
            er = asd[j]
            pos = er.index(fg)
            cex = er[0:pos]
            bd.append(cex)
            de = 0
            cex = ""
        return bd
 
def language():
    global lan
    answer = False
    if lan == "english":
        answer = tk.messagebox.askquestion(title='language changing', message='Do you want to switch to 简体中文?')
        if answer == "yes":
            lan = "chinese"
            d_name.set("更换语言")
            e_name.set("添加日程")
            f_name.set("待办事件")
        else:
            pass
    elif lan == "chinese":
        answer = tk.messagebox.askquestion(title='language changing', message='Do you want to switch to English?')
        if answer == "yes":
            lan = "english"
            d_name.set("language")
            e_name.set("schedule")
            f_name.set("to do event")
        else:
            pass
    

def insert_point():
    var = entry.get()
    g.insert('insert',var)

def about():
    os.startfile(r".\about.exe")

window = tk.Tk()
window.title('桌面助手')
window.geometry('600x350')
window.wm_attributes("-alpha", 0.75)        # 透明度(0.0~1.0)
window.wm_attributes("-toolwindow", True)  # 置为工具窗口(没有最大最小按钮)
window.wm_attributes("-topmost", True)     # 永远处于顶层
z = tk.Label(window,anchor = 'w',bg='white',
                    justify = 'center', width=500, height=500)
z.place(x = 0, y = 0)
api_url = 'https://v1.hitokoto.cn/?c=b&encode=json'
response = requests.get(api_url)
res = json.loads(response.text)
a_word = res['hitokoto']
a = tk.Label(window,anchor = 'w',text=a_word,fg = 'black', bg='lightblue', 
                     font=('微软雅黑', 16),
                    justify = 'center',wraplength = 460, width=40, height=2)
a.place(x = 50, y = 30)
 
#b = tk.Label(window,anchor='nw',text="事事及时做，一日胜三日",
#             fg='black',bg='white',font=('TimesNewRoman',12),
#             justify='center',width=50,height=20)
#b.place(x = 50, y = 150)
 
#c = tk.Button(window, text='language', width=15,
#              height=2, command=language)
#c.place(x = 270,y = 190)
 
d_name = tk.StringVar()
d_name.set("更换语言")
d = tk.Button(window,anchor='nw',textvariable=d_name,
             fg='black',bg='white',font=('微软雅黑',16),
             justify='center',width=7,height=1,command=language)
d.place(x = 50, y = 110)
 
h_name = tk.StringVar()
h_name.set("添加日程")
h = tk.Button(window,anchor='nw',textvariable=h_name,
             fg='black',bg='white',font=('微软雅黑',16),
             justify='center',width=7,height=1,command=insert_point)
h.place(x = 200, y = 110)

i_name = tk.StringVar()
i_name.set("关于")
i = tk.Button(window,anchor='nw',textvariable=i_name,
             fg='black',bg='white',font=('微软雅黑',16),
             justify='center',width=7,height=1,command=about)
i.place(x = 350, y = 110)

e_name = tk.StringVar()
e_name.set("待填日程")
e = tk.Label(window,anchor='nw',textvariable=e_name,
             fg='black',bg='white',font=('微软雅黑',16),
             justify='center',width=8,height=1)
e.place(x = 50, y = 170)
 
f_name = tk.StringVar()
f_name.set("待办事件")
f = tk.Label(window,anchor='nw',textvariable=f_name,
             fg='black',bg='white',font=('微软雅黑',16),
             justify='center',width=20,height=1)
f.place(x = 50, y = 220)
 
 
var_usr_name = tk.StringVar()
entry = tk.Entry(window,font=('微软雅黑',16))
entry.place(x=270, y=170)
g = tk.Text(window,width=20,height=3,font=('微软雅黑',16))
g.place(x=270, y=220)
 
window.mainloop()