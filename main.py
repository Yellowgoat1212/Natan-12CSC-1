#the start for the quiz 
from tkinter import *
import random
from PIL import Image, ImageTk
from tkinter import messagebox

name_list = []
asked = []
score=0
#Randomiser for questions 
def randomiser():
    global qnum
    qnum = random.randint(1,10)
    if qnum not in asked:
      asked.append(qnum)
    elif qnum in asked:
      randomiser()

#Quiz starter page code      
class QuizStarter:
  def __init__(self, parent):
  #users input is taken by an Entr Widget
    self.entry_box=Entry(parent)
    self.entry_box=Entry(window,width=13)
    self.entry_box.place(x=455,y=410)
    #Continue button
    self.continue_button = Button(window, text="Start Quiz ", font=("Helvetica","13","bold"), bg="orange",command=self.name_collection)
    self.continue_button.place(x=447,y=440)

  #Name collection and entry box   
  def name_collection(self):
      name=self.entry_box.get()
      if name == '':
            messagebox.showerror('Name is required!',
                                 'Please enter your name')
      elif len(name) > 15:

        # to make sure name entered is between 1-15

            messagebox.showerror('limit error',
                                 'please enter a name between 1 and 15 characters'
                                 )
      elif name.isnumeric():
            messagebox.showerror('Name error',
                                 'Name can only consist of alphabet')
      elif not name.isalpha():

        # to make sure name entered is only letters not numbers

            messagebox.showerror('Symbol error', 'name cant consist of symbols')
      else:
    #destroying entry box and continue button to transfer to question frame
       name_list.append(name)   
       self.entry_box.destroy()
       self.continue_button.destroy()
       Quizquestions(window)
#Quiz question frame     
class Quizquestions:
  def __init__(self, parent):
    bg_image = Image.open("questionframe.jpg")
    bg_image = bg_image.resize((950,750),Image.ANTIALIAS)
    bg_image = ImageTk.PhotoImage(bg_image)
    image_label.configure(image=bg_image)
    image_label.place(x=0, y=0, relwidth=1, relheight=1)
    #Question 1
    self.quiz_questions = {
      1:["When was basketball officially invented?",
        '1891',
        '1987',
        '1950',
        '1850',
        '1891'
        ,1],
      #Question 2
      2:["how many players are on a team?",
        '20 players',
        '15 players',
        '12 players',
        '5 player',
        '12 players'
         ,3],
      #Question 3
      3:["How many fouls can a player commit before fouling out the game?",
        'Five fouls',
        'Seven fouls',
        'Nine fouls',
        'Six fouls',
        'Six fouls'
        ,4],
      #Question 4
      4:["How many games are in an NBA season?",
        '75 games',
        '82 games',
        '85 games',
        '70 games',
        '82 games'
        ,2],
      #Question 5
      5:["How many points is a dunk?",
        '1 point',
        '2 points',
        '4 points',
        '0.5 points',
        '2 points'
        ,2],
      #Question 6
      6:["What is the role of a point guard?",
        'runs the offense and usually is the teams best dribbler and passer',
        'score points for their team and steal the ball on defense',
        'plays against small and large players',
        'the tallest player on each team, playing near the basket',
        'runs the offense and usually is the teams best dribbler and passer'
        ,1],
      #Question 7
      7:["A free throw is worth",
        '1 point',
        '2 point',
        '3 point',
        '4 point',
        '1 point'
        ,1],
      #Question 8
      8:["Kicking a basketball is what kind of foul?",
        'Personal foul',
        'Flagrant foul',
        'Technical foul',
        'Kick Ball violation',
        'Kick Ball violation'
        ,4],
      #Question 9
      9:["Which team won the first NBA Championship?",
        'The Warriors',
        'New York Knicks',
        'Boston Celtic',
        'oklahoma city thunder',
        'The Warriors'
        ,1],
      #Question 10
      10:["How long is an NBA game?",
         '60 minutes',
         '48 minutes',
         '2 hours',
         '90 minutes',
         '48 minutes'
         ,2], 
    }
    
    #self.quiz_frame = Frame(parent, bg = background_color, padx=40, pady=40)
    #self.quiz_frame.grid()
    
    #defining question randomiser
    randomiser()
    
    # img= Image.open("questionframe.jpg")
    # img= img.resize((950,750),Image.ANTIALIAS)

    # picture = ImageTk.PhotoImage(img)
    # image_label.configure(image = picture)
    
    #Label for questions
    self.question_label=Label(window, text = self.quiz_questions[qnum][0], font =( "Tw Cen MT","18","bold"))
    self.question_label.grid(row= 0, padx=10, pady=10)  

    self.con1=IntVar()
    #Raido buttons for answer selection 
    self.rb1 = Radiobutton(window, text = self.quiz_questions[qnum][1], font=("Helvetica", "12"),  value=1, variable=self.con1, pady=10)
    self.rb1.grid(row=1, sticky=W)

    self.rb2 = Radiobutton(window, text = self.quiz_questions[qnum][2], font=("Helvetica", "12"),  value=2, variable=self.con1, pady=10)
    self.rb2.grid(row=2, sticky=W)

    self.rb3 = Radiobutton(window, text = self.quiz_questions[qnum][3], font=("Helvetica", "12"), value=3, variable=self.con1, pady=10)
    self.rb3.grid(row=3, sticky=W)

    self.rb4 = Radiobutton(window, text = self.quiz_questions[qnum][4], font=("Helvetica", "12"),  value=4, variable=self.con1, pady=10)
    self.rb4.grid(row=4, sticky=W)
   #Confirm button for end-user after selecting an answer  
    self.confirm_button = Button(window, text="Confrim",bg="Light blue",command=self.quiz_progress)
    self.confirm_button.place(x=300,y=235)
    #Score label to get track for user scores  
    self.score_label  = Label(window, text = 'score',bg="Lightblue")
    self.score_label.place(x=50,y=340)  
      #leave button for question page 
    self.leave=Button(window,text="Leave",font=("Helvetica","13","bold"),bg="lightblue",command=self.end_screen)
    self.leave.place(x=50,y=235)

    

   #This part of the code is for the question setup 
  def questions_setup(self):
     randomiser()
     self.con1.set(0)
     self.question_label.config(text=self.quiz_questions[qnum][0])
     self.rb1.config(text=self.quiz_questions[qnum][1])
     self.rb2.config(text=self.quiz_questions[qnum][2])
     self.rb3.config(text=self.quiz_questions[qnum][3])
     self.rb4.config(text=self.quiz_questions[qnum][4])
 #This is for score system 
  def quiz_progress(self):
      global score
      scr_label=self.score_label
      choice=self.con1.get()
      if len(asked)>9:
        if choice == self.quiz_questions[qnum][6]:
          score +=1
          scr_label.configure(text=score)
          self.confirm_button.config(text="Confirm")
          self.end_screen()
         
        else:
          score+=0
          scr_label.configure(text="The correct answer was: "+ self.quiz_questions[qnum][5])
          self.confirm_button.config(text="confirm")
         
      else:
          if choice==0:
              self.confirm_button.config(text="Try Again, you didn't select an option then submit again" )#This part of the code is to remind users to select an answer
              choice=self.con1.get()
          else:
           if choice == self.quiz_questions[qnum][6]:
                score+=1
                scr_label.configure(text=score)
                self.confirm_button.config(text="confirm")
                self.questions_setup()
           else:
                  score+=0
                  scr_label.configure(text="The correct answer was: " + self.quiz_questions[qnum][5])#if user gets correct answer program print^^
                  self.confirm_button.config(text="Confirmn")#confirm button to confirm their selected answer
                  self.questions_setup()
  #this destroy quizquestion page  
  def end_screen(self):
        window.destroy()
       

        open_end_object = end()  
#exit page when end-user press leave or finishes the quiz
class end:
  def __init__(self):
        background_color = 'dark Orange'#Background colour for exit page
        global exitbox
        exitbox = Tk()
        exitbox.title('Exit Box')#exit box title 
        exitbox.geometry('700x600')

        # end frame

        self.end_frame = Frame(exitbox, width=850, height=750,
                               bg=background_color)
        self.end_frame.grid(row=1)

        # end heading

        self.end_heading = Label(exitbox,
                                 text='That was good effort, hope you enjoyed!'
                                 , font=('Tw Cen Mt', 22, 'bold'),
                                 bg=background_color)
        self.end_heading.place(x=10, y=50)

        # exit button

        self.exit_button = Button(
            exitbox,
            text='Exit',
            width=10,
            bg='red',
            font=('Tw Cen Mt', 12, 'bold'),
            command=self.close_endbox,
            )
        self.exit_button.place(x=260, y=200)

        # list label

        self.list_label = Label(exitbox, text='Feel free to try the quiz again',
                                font=('Tw Cen Mt', 12, 'bold'),
                                width=40, bg=background_color)
        self.list_label.place(x=110, y=100)
   #destroying code to end the program 
  def close_endbox(self):
        self.end_frame.destroy()
        self.end_heading.destroy()
        self.exit_button.destroy()
        self.list_label.destroy()
        exitbox.destroy()
  
if __name__== "__main__":
    window = Tk()
  #Window title for quizstarter 
    window.title("Basketball Knowledge Quiz")
    window.geometry("650x500")
  #image background for quizstarter 
    bg_image = Image.open("Basketball_general_knowledge_quiz.png")
    bg_image = bg_image.resize((650,500),Image.ANTIALIAS)
    bg_image = ImageTk.PhotoImage(bg_image)
    image_label= Label(window, image=bg_image)
    image_label.place(x=0, y=0, relwidth=1, relheight=1)
    start_object = QuizStarter(window)
    window.mainloop()