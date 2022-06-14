from tkinter import *

from PIL import Image, ImageTk

name_list = []

class QuizStarter:
  
  
  def __init__(self, parent):
    self.entry_box=Entry(window)
    self.entry_box=Entry(window,width=13)
    self.entry_box.place(x=452,y=410)

    self.continue_button = Button(window, text="Continue", font=( "Helvetica","13","bold"), bg="orange",command=self.name_collection)
    self.continue_button.place(x=455,y=440)
     

  def name_collection(self):
        name=self.entry_box.get()
        names.append(name)
        self.user_label.destroy()
        self.entry_box.destroy()
        self.continue_button.destroy()
        Quiz(window)
    

if __name__== '__main__':
    window = Tk()
    window.title("Basketball Knowledge Quiz")
    window.geometry("650x500")
    bg_image = Image.open("Basketball_general_knowledge_quiz.png")
    bg_image = bg_image.resize((650,500),Image.ANTIALIAS)
    bg_image = ImageTk.PhotoImage(bg_image)
    image_label= Label(window, image=bg_image)
    image_label.place(x=0, y=0, relwidth=1, relheight=1)
    start_object = QuizStarter(window)

    window.mainloop()