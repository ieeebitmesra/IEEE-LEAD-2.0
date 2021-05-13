from tkinter import *
from PIL import Image,ImageTk
import os

root = Tk()
root.title("IEEE LEAD 2.0 [Web Scraping Project]")
# root.iconphoto(False, PhotoImage(file='Programs/WebScrapping/Images/th.jfif'))
root.call('wm', 'iconphoto', root._w, PhotoImage(file='Images/ieee.png'))
logo = ImageTk.PhotoImage(Image.open("Images/Web-Scrap.jpg"))
l_logo = Label(image=logo)
l_logo.grid(row=0,column=0, columnspan=3, padx=20)

# ----------------------------------------------------------------------------------------------------------

gs_logo = ImageTk.PhotoImage(Image.open("Images/web_gs.png"))
label_gs = Label(image=gs_logo)
label_gs.grid(column=1, row=3, pady=10)


def open_gs():
    os.system('python googleSearchResult.py')
    root.quit()
    
gs_btn = Button(root, text="Google Search Result", command=open_gs, bg='#dddddd', borderwidth=3)
gs_btn.config(font=(12))
gs_btn.grid(column=1, row=4, pady=5)

#-----------------------------------------------------------------------------------------------------------
ns_logo = ImageTk.PhotoImage(Image.open("Images/web_ns.png"))
label_ns = Label(image=ns_logo)
label_ns.grid(column=0, row=5)


def open_naukri():
    os.system('python naukriResult.py')
    root.quit()
    
ns_btn = Button(root, text="Open window", command=open_naukri, bg='#dddddd', borderwidth=3)
ns_btn.config(font=(12))
ns_btn.grid(column=0, row=6, pady=5)

#-------------------------------------------------------------------------------------------------------

ms_logo = ImageTk.PhotoImage(Image.open("Images/web_ms.png"))
label_ms = Label(image=ms_logo)
label_ms.grid(column=2, row=5)


def open_monster():
    os.system('python monsterResult.py')
    root.quit()
    
ms_btn = Button(root, text="Open Window", command=open_monster, bg='#dddddd', borderwidth=3)
ms_btn.config(font=(12))
ms_btn.grid(column=2, row=6, pady=5)

#--------------------------------------------------------------------------------------------------------------

def open_comp():
    os.system('python compare.py')
    root.quit()

compare_btn = Button(root, text="Compare", command=open_comp, bg='#dddddd', borderwidth=2)
compare_btn.config(font=(12))
compare_btn.grid(column=1,row=6,pady=5)


exit_btn = Button(root, text="Exit", command=root.quit, padx=20, bg='#dddddd', borderwidth=2)
exit_btn.config(font=(12))
exit_btn.grid(column=1, row=7, pady=15)



mainloop()