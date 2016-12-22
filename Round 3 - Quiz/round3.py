import Tkinter as tk
import tkMessageBox
import os
count=0

class Question(tk.Frame):
    def __init__(self, *args, **kwargs):
            tk.Frame.__init__(self, *args, **kwargs)
            
    def show(self):
            self.lift()

class Question1(Question):
    def __init__(self, *args, **kwargs):
            Question.__init__(self, *args, **kwargs)
            data_file = open("database/que1.txt")
            data = data_file.read()
            data_file.close()
            label = tk.Label(self, text=data,justify="left",font=("FreeMono",15))
            label.pack(side="top", fill="both", expand=True)
            label1 = tk.Label(self, text="Type Answer below and click validate: ")
            label1.pack(side="top", fill="both", expand=True)
            entry = tk.Entry(self)
            entry.pack(side="top", fill="both", expand=True)
            self.button_1 = tk.Button(self, text="Validate",fg="red")
            self.button_1.config(height = 3, width = 10  )  
            self.button_1.pack(side="top", expand=True)
            label2 = tk.Label(self, text="Hint: use pow() or math.h")
            label2.pack(side="bottom", fill="both", expand=True)                        

            #self.button_1.pack(side="top", fill="both", expand=True)
            
            flag=[0]
            def validate( event ):
                q=entry.get()

                if(q=="9" and not flag[0]):
                    tkMessageBox.showinfo('Correct Answer', '1 down 6 to go\nProceed to next question')
                    global count
                    count=count+1
                    with open("scores.txt","a") as fp:
                    	fp.write("\nScore after Question 1 :%d "%(count))
                    flag[0]=1
                    self.button_1.config(state='disabled')
                else:
                    tkMessageBox.showinfo('Wrong Answer', 'Either a wrong answer or already answered')
                    
            self.button_1.bind("<Button-1>", validate)
            #button_1 = tk.Button(self, text="Validate")
            
            #button_1.bind("<Button-1>", validate)

            #button_1.pack(side="top", fill="both", expand=True)

class Question2(Question):

    def __init__(self, *args, **kwargs):
            Question.__init__(self, *args, **kwargs)
            data_file = open("database/que2.txt")
            data = data_file.read()
            data_file.close()
            label = tk.Label(self, text=data,justify="left",font=("FreeMono",13))
            label.pack(side="top", fill="both", expand=True)
            label1 = tk.Label(self, text="Type Answer below and click validate: ")
            label1.pack(side="top", fill="both", expand=True)
            entry = tk.Entry(self)
            entry.pack(side="top", fill="both", expand=True)
            self.button_1 = tk.Button(self, text="Validate")
            self.button_1.config(height = 3, width = 10  )
            self.button_1.pack(side="top", expand=True)
            label1 = tk.Label(self, text="Hint use 1)curl 2)Translation 3)optical character recognition")
            label1.pack(side="bottom", fill="both", expand=True)            
            flag=[0]
            def validate( event ):
                q=entry.get()
                
                if(q=="73782 2  2" and not flag[0]):

                    tkMessageBox.showinfo('Correct Answer', 'Proceed to next question')
                    global count

                    
                    count=count+1


                    with open("scores.txt","a") as fp:
                    	fp.write("\nScore after Question 2 :%d "%(count)) 
                    flag[0]=1
                    self.button_1.config(state='disabled')

                else:
                    tkMessageBox.showinfo('Wrong Answer', 'Try Again')

            #button_1 = tk.Button(self, text="Validate")
            
            self.button_1.bind("<Button-1>", validate)
            #button_1.pack(side="top", fill="both", expand=True)

class Question3(Question):
   
    def __init__(self, *args, **kwargs):
            Question.__init__(self, *args, **kwargs)
            data_file = open("database/que3.txt")
            data = data_file.read()
            data_file.close()
            label = tk.Label(self, text=data,justify="left",font=("FreeMono",13))
            label.pack(side="top", fill="both",expand=True)
            label1 = tk.Label(self, text="Type Answer below and click validate: ")
            label1.pack(side="top", fill="both", expand=True)
            entry = tk.Entry(self)
            entry.pack(side="top", fill="both", expand=True)
            self.button_1 = tk.Button(self, text="Validate",fg="red")
            
            self.button_1.config(height = 3, width = 10  )  
            self.button_1.pack(side="top", expand=True)

            #self.button_1.pack(side="top", fill="both", expand=True)
            
            flag=[0]
            def validate( event ):
                q=entry.get()

                if(q=="LLLLLLLLLLLLKKKKKKKKKKKJJJJJJJJJJIIIIIIIIIHHHHHHHHGGGGGGGFFFFFFEEEEEDDDDCCCBBA 78" and not flag[0]):
                    tkMessageBox.showinfo('Correct Answer', 'Proceed to next question')
                    global count
                    count=count+1
                    with open("scores.txt","a") as fp:
                    	fp.write("\nScore after Question 3 :%d "%(count))
                    flag[0]=1
                    self.button_1.config(state='disabled')
                else:
                    tkMessageBox.showinfo('Wrong Answer', 'Either a wrong answer or already answered')
                    
            self.button_1.bind("<Button-1>", validate)
	 

            #button_1 = tk.Button(self, text="Validate")
            
            #button_1.bind("<Button-1>", validate)

            #button_1.pack(side="top", fill="both", expand=True)
class Question4(Question):
    def __init__(self, *args, **kwargs):
            Question.__init__(self, *args, **kwargs)
            data_file = open("database/que4.txt")
            data = data_file.read()
            data_file.close()
            label = tk.Label(self, text=data,justify="left",font=("FreeMono",11))
            label.pack(side="top", fill="both", expand=True)
            label1 = tk.Label(self, text="Type Answer below and click validate: ")
            label1.pack(side="top", fill="both", expand=True)
            entry = tk.Entry(self)
            entry.pack(side="top", fill="both", expand=True)
            self.button_1 = tk.Button(self, text="Validate",fg="red")
            
            self.button_1.config(height = 3, width = 10  )  
            self.button_1.pack(side="top", expand=True)

            #self.button_1.pack(side="top", fill="both", expand=True)
            
            flag=[0]
            def validate( event ):
                q=entry.get()

                if(q=="648" and not flag[0]):
                    tkMessageBox.showinfo('Correct Answer', 'Proceed to next question')
                    global count
                    count=count+1
                    with open("scores.txt","a") as fp:
                    	fp.write("\nScore after Question 4 :%d "%(count))
                    flag[0]=1
                    self.button_1.config(state='disabled')
                else:
                    tkMessageBox.showinfo('Wrong Answer', 'Either a wrong answer or already answered')
                    
            self.button_1.bind("<Button-1>", validate)
            #button_1 = tk.Button(self, text="Validate")
            
            #button_1.bind("<Button-1>", validate)

            #button_1.pack(side="top", fill="both", expand=True)
class Question5(Question):
    def __init__(self, *args, **kwargs):
            Question.__init__(self, *args, **kwargs)
            data_file = open("database/que5.txt")
            data = data_file.read()
            data_file.close()
            label = tk.Label(self, text=data,justify="left",font=("FreeMono",11))
            label.pack(side="top", fill="both", expand=True)
            label1 = tk.Label(self, text="Paste added keyword below and click validate: ")
            label1.pack(side="top", fill="both", expand=True)
            entry = tk.Entry(self)
            entry.pack(side="top", fill="both", expand=True)
            self.button_1 = tk.Button(self, text="Validate",fg="red")
            
            self.button_1.config(height = 3, width = 10  )  
            self.button_1.pack(side="top", expand=True)

            #self.button_1.pack(side="top", fill="both", expand=True)
            
            flag=[0]
            def validate( event ):
                q=entry.get()

                if(q=="Charles Davis" and not flag[0]):
                    tkMessageBox.showinfo('Correct Answer', 'Proceed to next question')
                    global count
                    count=count+1
                    with open("scores.txt","a") as fp:
                    	fp.write("\nScore after Question 5 :%d "%(count))
                    flag[0]=1
                    self.button_1.config(state='disabled')
                else:
                    tkMessageBox.showinfo('Wrong Answer', 'Either a wrong answer or already answered')
                    
            self.button_1.bind("<Button-1>", validate)
            #button_1 = tk.Button(self, text="Validate")
            
            #button_1.bind("<Button-1>", validate)

            #button_1.pack(side="top", fill="both", expand=True)
class Question6(Question):
    def __init__(self, *args, **kwargs):
            Question.__init__(self, *args, **kwargs)
            data_file = open("database/que6.txt")
            data = data_file.read()
            data_file.close()
            label = tk.Label(self, text=data,justify="left",font=("FreeMono",13))
            label.pack(side="top", fill="both", expand=True)
            label1 = tk.Label(self, text="Type Answer below and click validate: ")
            label1.pack(side="top", fill="both", expand=True)
            entry = tk.Entry(self)
            entry.pack(side="top", fill="both", expand=True)
            self.button_1 = tk.Button(self, text="Validate",fg="red")
            
            self.button_1.config(height = 3, width = 10  )  
            self.button_1.pack(side="top", expand=True)

            #self.button_1.pack(side="top", fill="both", expand=True)
            
            flag=[0]
            def validate( event ):
                q=entry.get()

                if(q=="610" and not flag[0]):
                    tkMessageBox.showinfo('Correct Answer', 'Proceed to next question')
                    global count
                    count=count+1
                    with open("scores.txt","a") as fp:
                    	fp.write("\nScore after Question 6 :%d "%(count))
                    flag[0]=1
                    self.button_1.config(state='disabled')
                else:
                    tkMessageBox.showinfo('Wrong Answer', 'Either a wrong answer or already answered')
                    
            self.button_1.bind("<Button-1>", validate)
            #button_1 = tk.Button(self, text="Validate")
            
            #button_1.bind("<Button-1>", validate)

            #button_1.pack(side="top", fill="both", expand=True)
class Question7(Question):
    def __init__(self, *args, **kwargs):
            Question.__init__(self, *args, **kwargs)
            data_file = open("database/que7.txt")
            data = data_file.read()
            data_file.close()            
	    label = tk.Label(self, text=data,font=("FreeMono",12))
            label.pack(side="top", fill="both", expand=True)
            label1 = tk.Label(self, text="Type Answer below and click validate: ")
            label1.pack(side="top", fill="both", expand=True)
            entry = tk.Entry(self)
            entry.pack(side="top", fill="both", expand=True)
            self.button_1 = tk.Button(self, text="Validate",fg="red")
            
            self.button_1.config(height = 3, width = 10  )  
            self.button_1.pack(side="top", expand=True)

            #self.button_1.pack(side="top", fill="both", expand=True)
            
            flag=[0]
            def validate( event ):
                q=entry.get()

                if(q=="232792560" and not flag[0]):
                    tkMessageBox.showinfo('Correct Answer', 'Proceed to next question')
                    global count
                    count=count+1
                    with open("scores.txt","a") as fp:
                    	fp.write("\nScore after Question 7 :%d "%(count))
                    flag[0]=1
                    self.button_1.config(state='disabled')
                else:
                    tkMessageBox.showinfo('Wrong Answer', 'Either a wrong answer or already answered')
                    
            self.button_1.bind("<Button-1>", validate)
            #button_1 = tk.Button(self, text="Validate")
            
            #button_1.bind("<Button-1>", validate)

            #button_1.pack(side="top", fill="both", expand=True)
class Question8(Question):
    def __init__(self, *args, **kwargs):
            Question.__init__(self, *args, **kwargs)
            data_file = open("database/que8.txt")
            data = data_file.read()
            data_file.close()            
            label = tk.Label(self, text=data,font=("FreeMono",11))
            label.pack(side="top", fill="both", expand=True)
            label1 = tk.Label(self, text="Type Answer below and click validate: ")
            label1.pack(side="top", fill="both", expand=True)
            entry = tk.Entry(self)
            entry.pack(side="top", fill="both", expand=True)
            self.button_1 = tk.Button(self, text="Validate",fg="red")
            
            self.button_1.config(height = 3, width = 10  )  
            self.button_1.pack(side="top", expand=True)

            #self.button_1.pack(side="top", fill="both", expand=True)
            
            flag=[0]
            def validate( event ):
                q=entry.get()

                if(q=="25164150" and not flag[0]):
                    tkMessageBox.showinfo('Correct Answer', 'Proceed to next question')
                    global count
                    count=count+1
                    with open("scores.txt","a") as fp:
                    	fp.write("\nScore after Question 8 :%d "%(count))
                    flag[0]=1
                    self.button_1.config(state='disabled')
                else:
                    tkMessageBox.showinfo('Wrong Answer', 'Either a wrong answer or already answered')
                    
            self.button_1.bind("<Button-1>", validate)
            #button_1 = tk.Button(self, text="Validate")
            
            #button_1.bind("<Button-1>", validate)

            #button_1.pack(side="top", fill="both", expand=True)


class MainView(tk.Frame):
    def __init__(self, *args, **kwargs):
            tk.Frame.__init__(self, *args, **kwargs)
            p1 = Question1(self)
            p2 = Question2(self)
            p3 = Question3(self)
	    p4 = Question4(self)
            p5 = Question5(self)
            p6 = Question6(self)
            p7 = Question7(self)
            p8 = Question8(self)
            
            buttonframe = tk.Frame(self)
            container = tk.Frame(self)
            buttonframe.pack(side="top", fill="x", expand=False)
            container.pack(side="top", fill="both", expand=True)

            p1.place(in_=container, x=0, y=0, relwidth=1, relheight=1)
            p2.place(in_=container, x=0, y=0, relwidth=1, relheight=1)
            p3.place(in_=container, x=0, y=0, relwidth=1, relheight=1)
            p4.place(in_=container, x=0, y=0, relwidth=1, relheight=1)
            p5.place(in_=container, x=0, y=0, relwidth=1, relheight=1)
            p6.place(in_=container, x=0, y=0, relwidth=1, relheight=1)
            p7.place(in_=container, x=0, y=0, relwidth=1, relheight=1)
            p8.place(in_=container, x=0, y=0, relwidth=1, relheight=1)
            


            b1 = tk.Button(buttonframe, text="Question 1", command=p1.lift)
            b2 = tk.Button(buttonframe, text="Question 2", command=p2.lift)
            b3 = tk.Button(buttonframe, text="Question 3", command=p3.lift)
            b4 = tk.Button(buttonframe, text="Question 4", command=p4.lift)
            b5 = tk.Button(buttonframe, text="Question 5", command=p5.lift)
            b6 = tk.Button(buttonframe, text="Question 6", command=p6.lift)
            b7 = tk.Button(buttonframe, text="Question 7", command=p7.lift)
            b8 = tk.Button(buttonframe, text="Question 8", command=p8.lift)


            b1.pack(side="left",fill="both", expand=True)
            b2.pack(side="left",fill="both", expand=True)
            b3.pack(side="left",fill="both", expand=True)
            b4.pack(side="left",fill="both", expand=True) 
            b5.pack(side="left",fill="both", expand=True)
            b6.pack(side="left",fill="both", expand=True)
            b7.pack(side="left",fill="both", expand=True)
            b8.pack(side="left",fill="both", expand=True)

            p1.show()

if __name__ == "__main__":
    root = tk.Tk()
    main = MainView(root)
    main.pack(side="top", fill="both", expand=True)
    root.wm_geometry("1080x720")
    root.title("Maze Coders Round 3")
    #root.configure(bg="white")
    #root.option_add("*background", "white")
    def openterm():
              os.system("gnome-terminal -x ./openterm.sh")
    def opennano():
              os.system("gnome-terminal -x ./opennano.sh")
              
    def opengedit():
              os.system("./opengedit.sh")

            # Tkinter puts menus at the top by default
    menu = tk.Menu(root)
    root.config(menu=menu)
    subMenu = tk.Menu(menu)
# Adds a drop down when "File" is clicked
    menu.add_cascade(label="Tools", menu=subMenu)
    subMenu.add_command(label="Open Terminal", command=openterm)
    subMenu.add_command(label="Open Gedit", command=opengedit) 
    subMenu.add_command(label="Open Nano", command=opennano)            
    root.mainloop()
