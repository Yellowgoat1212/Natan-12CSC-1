from tkinter import *
import random
from PIL import Image, ImageTk
name_list = []
asked = []
score=0

def randomiser():
    global qnum
    qnum = random.randint(1,10)
    if qnum not in asked:
      asked.append(qnum)
    elif qnum in asked:
      randomiser()

      
class QuizStarter:
  def __init__(self, parent):
  #users input is taken by an Entr Widget
    self.entry_box=Entry(parent)
    self.entry_box=Entry(window,width=13)
    self.entry_box.place(x=450,y=410)
    #Continue button
    self.continue_button = Button(window, text="Start Quiz ", font=("Helvetica","13","bold"), bg="orange",command=self.name_collection)
    self.continue_button.place(x=447,y=440)

    
  def name_collection(self):
      name=self.entry_box.get()
      name_list.append(name)
      self.entry_box.destroy()
      self.continue_button.destroy()
      Quizquestions(window)
    
class Quizquestions:
  def __init__(self, parent):
    background_color="orange"

    self.quiz_questions = {
      1:["When was basketball officially invented?",
        '1891',
        '1987',
        '1950',
        '1850',
        '1891'
        ,1],
      2:["how many players are on a team?",
        '20 players',
        '15 players',
        '12 players',
        '5 player',
        '12 players'
         ,3],
      3:["How many fouls can a player commit before fouling out the game?",
        'Five fouls',
        'Seven fouls',
        'Nine fouls',
        'Six fouls',
        'Six fouls'
        ,4],
      4:["How many games are in an NBA season?",
        '75 games',
        '82 games',
        '85 games',
        '70 games',
        '82 games'
        ,2],
      5:["How many points is a dunk?",
        '1 point',
        '2 points',
        '4 points',
        '0.5 points',
        '2 points'
        ,2],
      6:["What is the role of a point guard?",
        'runs the offense and usually is the teams best dribbler and passer',
        'score points for their team and steal the ball on defense',
        'plays against small and large players',
        'the tallest player on each team, playing near the basket'
        'runs the offense and usually is the teams best dribbler and passer'
        ,2],
      7:["A free throw is worth",
        '1 point',
        '2 point',
        '3 point',
        '4 point',
        '1 point'
        ,1],
      8:["Kicking a basketball is what kind of foul?",
        'Personal foul',
        'Flagrant foul',
        'Technical foul',
        'Kick Ball violation',
        'Kick Ball violation'
        ,4],
      9:["Which team won the first NBA Championship?",
        'The Warriors',
        'New York Knicks',
        'Boston Celtic',
        'oklahoma city thunder',
        'The Warriors'
        ,1],
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

    randomiser()
    img= Image.open("questionframe.jpg")
    img= img.resize((950,750),Image.ANTIALIAS)

    picture = ImageTk.PhotoImage(img)
    image_label.configure(image = picture)

    self.question_label=Label(window, text = self.quiz_questions[qnum][0], font =( "Tw Cen MT","18","bold"))
    self.question_label.grid(row= 0, padx=10, pady=10)  

    self.con1=IntVar()

    self.rb1 = Radiobutton(window, text = self.quiz_questions[qnum][1], font=("Helvetica", "12"), bg=background_color, value=1, variable=self.con1, pady=10)
    self.rb1.grid(row=1, sticky=W)

    self.rb2 = Radiobutton(window, text = self.quiz_questions[qnum][2], font=("Helvetica", "12"), bg=background_color, value=2, variable=self.con1, pady=10)
    self.rb2.grid(row=2, sticky=W)

    self.rb3 = Radiobutton(window, text = self.quiz_questions[qnum][3], font=("Helvetica", "12"), bg=background_color, value=3, variable=self.con1, pady=10)
    self.rb3.grid(row=3, sticky=W)

    self.rb4 = Radiobutton(window, text = self.quiz_questions[qnum][4], font=("Helvetica", "12"), bg=background_color, value=4, variable=self.con1, pady=10)
    self.rb4.grid(row=4, sticky=W)

    self.confirm_button = Button(window, text="Confrim",bg="white",command=self.quiz_progress)
    self.confirm_button.place(x=300,y=235)
   
    self.score_label  = Label(window, text = 'score')
    self.score_label.place(x=390,y=240)  

    self.leave=Button(window,text="Leave",font=("Helvetica","13","bold"),bg="lightblue",command=self.end_screen)
    self.leave.place(x=50,y=235)

   
  def questions_setup(self):
     randomiser()
     self.con1.set(0)
     self.question_label.config(text=self.quiz_questions[qnum][0])
     self.rb1.config(text=self.quiz_questions[qnum][1])
     self.rb2.config(text=self.quiz_questions[qnum][2])
     self.rb3.config(text=self.quiz_questions[qnum][3])
     self.rb4.config(text=self.quiz_questions[qnum][4])
 
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
              self.confirm_button.config(text="Try Again, you didn't select an option then submit again" )
              choice=self.con1.get()
          else:
           if choice == self.quiz_questions[qnum][6]:
                score+=1
                scr_label.configure(text=score)
                self.confirm_button.config(text="confirm")
                self.questions_setup()
           else:
                  score+=0
                  scr_label.configure(text="The correct answer was: " + self.quiz_questions[qnum][5])
                  self.confirm_button.config(text="Confirmn")
                  self.questions_setup()
             
if __name__== "__main__":
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