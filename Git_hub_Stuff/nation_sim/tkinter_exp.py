import tkinter as tk
from tkinter import ttk
import matplotlib
matplotlib.use('TkAgg')
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2TkAgg
from matplotlib.figure import Figure
import matplotlib.animation as animation
from matplotlib import style
import urllib
import json
import pandas as pd
import numpy as np
from nation_sim import country, region, map_, get_neighbors
import nation_sim as sim
import pickle

LARGE_FONT=('Verdana',16)
style.use("ggplot")

f = Figure(figsize=(5,5),dpi=100)
a = f.add_subplot(111)
with open('country1.pkl', 'rb') as input:
    c1 = pickle.load(input)
with open('country2.pkl', 'rb') as input:
    c2 = pickle.load(input)

def animate(i):
    #pullData = open("sampleData.txt","r").read()
    #dataList = pullData.split('\n')
    #xList=[]
    #yList=[]
    #for eachLine in dataList:
    #    if len(eachLine)>1:
    #        x, y = eachLine.split(",")
    #        xList.append(float(x))
    #        yList.append(float(y))
    map_array=sim.ai_turn(c1,c2)
    a.clear()
    a.imshow(map_array)
    #with open('country1_a.pkl', 'wb') as output:
    #    c1 = pickle.dump(c1,output,pickle.HIGHEST_PROTOCOL)
    #with open('country2_a.pkl', 'wb') as output:
    #    c2 = pickle.dump(c2,output,pickle.HIGHEST_PROTOCOL)

class SeaofBTC(tk.Tk):

    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self,*args,**kwargs)
        container=tk.Frame(self)
        
        tk.Tk.iconbitmap(self,default='myicon.ico')
        tk.Tk.wm_title(self, "My own App")
        
        container.pack(side='top',fill='both',expand=True)
        
        container.grid_rowconfigure(0,weight=1)
        container.grid_columnconfigure(0,weight=1)
        
        self.frames={}
        
        for F in (StartPage, Graph_page, Page_two):
            frame=F(container,self)
            self.frames[F]=frame
            frame.grid(row=0,column=0,sticky='nsew')
        
        self.show_frame(StartPage)
    
    def show_frame(self, cont):
        frame=self.frames[cont]
        frame.tkraise()
        
def first():
    print('Hello World!')
        

class StartPage(tk.Frame):
    
    def __init__(self, parent,controller):
        tk.Frame.__init__(self,parent)
        #tk.Tk.iconbitmap(self,default='myicon.ico')
        
        label=tk.Label(self, text='My App', font=LARGE_FONT)
        label.pack(pady=10,padx=10)
        
        button1=ttk.Button(self,text='Start Simulation',command=lambda: controller.show_frame(Graph_page))
        button1.pack()
        
        button2=ttk.Button(self,text='Go to a Blank Page',command=lambda: controller.show_frame(Page_two))
        button2.pack()
        
        
class Graph_page(tk.Frame):
    def __init__(self, parent,controller):
        tk.Frame.__init__(self,parent)
        label=tk.Label(self, text='War Time', font=LARGE_FONT)
        label.pack(pady=10,padx=10)
        
        button1=ttk.Button(self,text='Back to Home',command=lambda: controller.show_frame(StartPage))
        button1.pack()
        
        canvas = FigureCanvasTkAgg(f,self)
        canvas.show()
        canvas.get_tk_widget().pack(side=tk.TOP,fill=tk.BOTH,expand=True)
        
        toolbar = NavigationToolbar2TkAgg(canvas, self)
        toolbar.update()
        canvas._tkcanvas.pack(side=tk.TOP,fill=tk.BOTH,expand=True)
        
class Page_two(tk.Frame):
    def __init__(self, parent,controller):
        tk.Frame.__init__(self,parent)
        label=tk.Label(self, text='Second Page', font=LARGE_FONT)
        label.pack(pady=10,padx=10)
        
        button1=ttk.Button(self,text='Back to Home',command=lambda: controller.show_frame(StartPage))
        button1.pack()
        
app=SeaofBTC()
ani = animation.FuncAnimation(f, animate, interval=200)
app.mainloop()
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        