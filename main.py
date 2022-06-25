from tkinter import *
from PIL import Image, ImageTk
name_list = []
global questions_answers
asked = []
score=0

def randomiser():
    global qnum
    qnum = random.randint(1,3)
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

    #coninue button
    self.continue_button = Button(window, text="Start Quiz ", font=( "Helvetica","13","bold"), bg="orange",command=self.name_collection)
    self.continue_button.place(x=447,y=440)

    
def name_collection(self):
    name=self.entry_box.get()
    name.append(name)
    print(name_list)
    self.entry_box.destroy()
    self.continue_button.destroy()
    Quiz(window)
    
class Quizquestions:
  def __init__(self, parent):
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
        'los angeles lakers',
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