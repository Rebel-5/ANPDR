from tkinter.ttk import Progressbar
import tkinter as tk
from tkinter import filedialog
from PIL import Image, ImageTk
import shutil, os
from predict_1 import get_text
from time import sleep
import threading


def run_func_with_loading_popup(func, msg, window_title = "Loading", bounce_speed = 8, pb_length = None):
    func_return_l = []

    class Main_Frame(object):
        def __init__(self, top, window_title, bounce_speed, pb_length):
            self.func = func
            self.top = top
            self.top.title(window_title)

            self.bounce_speed = bounce_speed
            self.pb_length = pb_length

            self.msg_lbl = tk.Label(top, text=msg)
            self.msg_lbl.pack(padx = 10, pady = 5)

            self.load_bar = Progressbar(top)
            self.load_bar.pack(padx = 10, pady = (0,10))

            self.bar_init()


        def bar_init(self):
            self.start_bar_thread = threading.Thread(target=self.start_bar, args=())
            self.start_bar_thread.start()

        def start_bar(self):
            try:
                self.load_bar.config(mode='indeterminate', maximum=100, value=0, length = self.pb_length)
                self.load_bar.start(self.bounce_speed)            

                self.work_thread = threading.Thread(target=self.work_task, args=())
                self.work_thread.start()

                self.work_thread.join()


                self.top.destroy()
            except:
                pass

        def work_task(self):
            func_return_l.append(func())


    root = tk.Tk()

    Main_Frame(root, window_title, bounce_speed, pb_length)
    root.mainloop() 
    return func_return_l[0]


def comment(text):
    lb1.config(text= text)
    
def extend():
    get_text()
    with open("output.txt", "r") as file:
        data = file.read()
    result = data.split('@')
    lb2.config(text= result[1])
    comment(text= result[0])


def on_submit():
    b3.config(state='disabled')
    r = run_func_with_loading_popup(lambda: extend(), msg='Loading')
    
    

def remove_all_files():
    for file_name in os.listdir('images'):
            file_path = os.path.join('images', file_name)
            os.remove(file_path)

def upload_file():
    remove_all_files()
    global img, filename
    f_types = [('Jpg Files', '*.jpg'), ('Jpg Files', '*.jpeg')]
    filename = filedialog.askopenfilename(filetypes=f_types)
    if filename:
        b3.config(state='normal')
        try:
            shutil.copy(filename, 'images')
        except:
            pass
        img=Image.open(filename)
        img_resized=img.resize((400,200))
        img=ImageTk.PhotoImage(img_resized)
        b2 =tk.Button(my_w,image=img)
        b2.grid(row=3,column=1)



my_w = tk.Tk()
my_w.geometry("400x400")  # Size of the window 
my_w.title('License Detection System')
my_font1=('times', 18, 'bold')
l1 = tk.Label(my_w,text='Upload Image file to detect License',width=30,font=my_font1)  
l1.grid(row=1,column=1)
b1 = tk.Button(my_w, text='Upload File', width=20,command = lambda:upload_file())
b1.grid(row=2,column=1)
b3 = tk.Button(my_w, text='Submit', command= on_submit)
b3.grid(row=4, column=1)
b3.config(state='disabled')
lb1 = tk.Label(my_w, text= '', font=40)
lb1.grid(row=6, column=1)
lb2 = tk.Label(my_w, text= '', font=40)
lb2.grid(row=7, column=1)

my_w.mainloop()


remove_all_files()
