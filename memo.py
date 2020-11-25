import tkinter as tk
import tkinter.font as font
import shelve as sh



root = tk.Tk()



def create_wgt():
    lbl=tk.Label(frm1,text=txt1.get("1.0", "end").rstrip(),background="#ffffff",foreground="#ff0000",width="30",font=my_font)
    lbl.pack(side=tk.TOP,pady=3,padx=3)
    lbl.bind("<Double-Button-1>",callback1)
    txt1.delete("1.0", "end")
    lbl_list.append(lbl)
    txt1.focus_set()

def call_cw(ev):
    create_wgt()

def callback1(event):
    a=event.widget["text"]
    txt1.delete("1.0", "end")
    txt1.insert("1.0", a)
    event.widget.destroy()

    lbl_list.remove(event.widget)

#update
def upd(ev):
    n=[]
    for i in lbl_list:
        n.append(i["text"])
        
    memo_data=sh.open("memodata")
    memo_data["text"]=n
    #print(memo_data["text"])
    memo_data.close

    txt1.focus_set()
    

#data load
def load_data():
    
    memo_data=sh.open("memodata")

    for i in memo_data["text"]:
        txt1.delete("1.0", "end")
        txt1.insert("1.0", i)

        create_wgt()
    memo_data.close

    txt1.focus_set()
    

#font
my_font = font.Font(root,family="游ゴシック",size=12,weight="bold")

#set display
root.title("MyGuiApp")
root.geometry("800x500")
root.configure(bg='#113311')

#make object
txt1=tk.Text(root,font=my_font,height="20", width="30")

btn=tk.Button(root,text="Add \n memo",font=my_font,width="5")
btn.bind("<Button-1>",call_cw)
btn.bind("<Return>",call_cw)

btn_upd=tk.Button(root,text="update",width="5",font=my_font)
btn_upd.bind("<Button-1>",upd)
btn_upd.bind("<Return>",upd)

frm1=tk.Frame(root,width="300",height="400", bg="#333333")

#list for upload
lbl_list=[]

#set object
txt1.pack(side=tk.LEFT,padx=10)
btn.pack(side=tk.LEFT)
btn_upd.place(x=450,y=5)
frm1.place(x=450,y=50)

#load first time
try:
    load_data()
except Exception as e:
    a=e #stop without this



root.mainloop()
