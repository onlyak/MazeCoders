import Tkinter as tk
import os
root = tk.Tk()
root.wm_geometry("1920x1080")
#root.configure(background="black")
def openr3(event) :
	os.system("gnome-terminal -x ./openr3.sh &")
	root.destroy() 
photo = tk.PhotoImage(file="image3414.png")
button = tk.Button(root, image=photo,bg="black",fg="black",height="1080",width="1920")
button.pack(side="top", fill="both", expand=True)
button.bind("<Button-1>", openr3)
root.mainloop()





