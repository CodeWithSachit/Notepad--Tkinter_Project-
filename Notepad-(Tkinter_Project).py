
from tkinter import *
from tkinter.messagebox import showinfo
from tkinter.filedialog import askopenfilename, asksaveasfilename
import os

def newFile():
    global file
    root.title("Untitle - Notepad")
    file = None
    textArea.delete(1.0 , END)

def openFile():
   global file
   file = askopenfilename(defaultextension='.txt',filetypes=[("All files","*.*"),("Text Documents","*.txt")])

   if  file == "":
      file = None
   else:
      root.title(os.path.basename(file) + "- Notepad")
      textArea.delete(1.0 , END)
      f = open(file ,"r")
      textArea.insert(1.0 , f.read())
      f.close()

def saveFile():
    global file
    if file == None :
       file = asksaveasfilename(initialfile = 'Untitled.txt',defaultextension='.txt',filetypes=[("All files","*.*"),("Text Documents","*.txt")])

       if file == "":
         file = None
       else:
         # Save as new file
         f = open(file,"w")
         f.write(textArea.get(1.0 , END))
         f.close
         root.title(os.path.basename(file)+ "-Notepad")
   
    else:
      # Save as new file
         f = open(file,"w")
         f.write(textArea.get(1.0 , END))
         f.close
      
def quitApp():
    root.destroy()
                                
def cut():
    textArea.event_generate("<<Cut>>")
    
def copy():
     textArea.event_generate("<<Copy>>")
    
def paste():
     textArea.event_generate("<<Paste>>")
    
def about():
    showinfo("Notepad","Notepad By Sachit!")

if __name__ == "__main__":
# Basic tkinter setup
   root = Tk()
   root.geometry("444x588")
   root.title("MY Notepad")
   root.wm_iconbitmap('notepad.ico')

#    Add text area
   textArea = Text(root,font="lucida 15")
   file =  None
   textArea.pack(expand=True ,fill= BOTH )
#  Lets creat a Menubar
   Menubar = Menu(root)
   fileMenu = Menu(Menubar,tearoff=0)

#  To Open new file
   fileMenu.add_command(label = "New ",command = newFile)

# To open already existance file
   fileMenu.add_command(label = "Open",command = openFile)

# To save the current file 
   fileMenu.add_command(label = "Save",command= saveFile)

   fileMenu.add_separator()
# To exit the file 
   fileMenu.add_command(label = "Exit",command = quitApp)

   Menubar.add_cascade(label = "File ", menu = fileMenu)

   root.config(menu= Menubar)

# File Menu Ends


# Edit Menu Starts 
   EditMenu = Menu(Menubar,tearoff=0)
  # To give a fiature of Cut , Copy ,Paste
   EditMenu.add_command(label= "Cut", command= cut)
   EditMenu.add_command(label= "Copy", command= copy)
   EditMenu.add_command(label= "Paste", command= paste)

   Menubar.add_cascade(label= "Edit",menu = EditMenu)
# Edit  Menu Ends

# Help Menu Starts
   HelpMenu = Menu(Menubar,tearoff=0)
   HelpMenu.add_command(label = "About Notepad",command=about)
   Menubar.add_cascade(label = "Help", menu = HelpMenu)
# Help Menu Ends
    
# Adding Scrollbar using tut18.py file
   scroll = Scrollbar(textArea)
   scroll.pack(side=RIGHT, fill= Y)
   scroll.config(command= textArea.yview)
   textArea.config(yscrollcommand=scroll.set)




   

