# -*- coding: utf-8 -*-
 
from Tkinter import * 
from PIL import Image, ImageTk

class FullScreenApp(object):
    def __init__(self, master, **kwargs):
        self.master=master
        pad=3
        self._geom='200x200+0+0'
        master.geometry("{0}x{1}+0+0".format(
            master.winfo_screenwidth()-pad, master.winfo_screenheight()-pad))
        master.bind('<Escape>',self.toggle_geom)            
    def toggle_geom(self,event):
        geom=self.master.winfo_geometry()
        print(geom,self._geom)
        self.master.geometry(self._geom)
        self._geom=geom

root=Tk()
app=FullScreenApp(root)

# image = Image.open("images/angry.png")
photo = PhotoImage(file="angry.png")

# canvas = Canvas(root,width=root.winfo_screenwidth(), height=root.winfo_screenheight())
# canvas.create_image(0, 0, anchor=NW, image=photo)
# canvas.pack()
Label(root, image=photo).pack()

root.mainloop()
