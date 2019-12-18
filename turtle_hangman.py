from turtle import *
import random


hangman= Turtle()





def base():
    hangman.pendown()
    hangman.forward(120)
    hangman.penup()
    hangman.backward(90)
    hangman.left(90)
    hangman.pendown()
   
    

def line1():
    hangman.pendown()
    hangman.forward(200)
   
    

def line2():
    hangman.pendown()
    hangman.right(90)
    hangman.pendown()
    hangman.forward(70)
    
def line3():
    hangman.pendown()
    hangman.right(90)
    hangman.forward(30)
    
def head():
    hangman.pendown()
    hangman.left(270)
    hangman.circle(20)
    hangman.right(270)
    hangman.penup()
    hangman.forward(20+20)
    
def left_arm():
    hangman.pendown()
    hangman.pendown()
    hangman.right(45)
    hangman.forward(50)
    hangman.backward(50)
    hangman.right(270)
    

def right_arm():
    hangman.pendown()
    hangman.forward(50)
    hangman.backward(50)
    hangman.right(45)

def boady():
    hangman.pendown()
    hangman.forward(50)
    hangman.right(45)
    
def left_leg():
    hangman.pendown()
    hangman.forward(50)
    hangman.backward(50)
    hangman.right(270)
    
    

def right_leg():
    hangman.pendown()
    hangman.pendown()
    hangman.forward(50)
    hangman.penup()
    hangman.setposition(300, 150)
    
    game_over()

    
words = ['cat', 'computer','house','desktop','python']
#words = ['cat']

figure =[base,line1,line2,line3,head,left_arm,right_arm,boady,left_leg,right_leg]

index=0 
idx=0


rand_no  = random.randint(0,len(words)-1)

random_word = words[rand_no]

word = "_" * len(random_word)
clue = list(word)

last_letter=[]
lives=5

current_pos = hangman.pos()


def game_over ():
    pen = hangman.getpen()
    pen.clear()
    hangman.write('GAME OVER\nThe word was '+random_word,align="left", font=("Arial", 24, "normal"))

user_input=hangman.screen.textinput("Welcome to Hangman ", "I am thinking  of a random word. Would like to play Y/N")

if user_input.lower() =='n':
   pen= hangman.getpen()
   pen.clear()
   hangman.write('GOOD BYE ',align="left", font=("Arial", 24, "normal"))
   user_guess =False
    
elif user_input.lower() =='y':
   user_guess =True



while user_guess:
    
        
       
    guess = hangman.screen.textinput("Welocome to Hangman", "The numner of letters are: "+str(len(word))+"\n"+str(lives)+"\n"+"Enter a letter")
        
    
    if guess  in  random_word:
        
        index = random_word.index(guess)
        clue[index] = guess
        word ="".join(clue)
      
        hangman.penup()
        hangman.setposition(300, 150)
        hangman.write(word,align="left", font=("Arial", 24, "normal"))
        hangman.goto(current_pos)   
          
          

    if word == random_word:
       
      
        user_guess=False
    
        hangman.write("You guessed right!\nYou win",align="left", font=("Arial", 24, "normal"))
                
                
    if guess not in  random_word :
        
        figure[idx]()
        idx  += 1
        current_pos = hangman.pos()
        print()

    if guess  in  last_letter :
        lives  -= 1 
        
    last_letter.append(guess) 

    

    if lives == 0:
        
        game_over()
            
       
exitonclick()