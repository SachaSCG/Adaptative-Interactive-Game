
init python:
     import math

define a = Character("Alex")

label start:
scene class_away at truecenter with fade:
     zoom 0.3 
$ firstrun = 0
$ wins = 0 # Displays the amount of right answers
$ diff = 0 # Controls the difficulty
$ lives = 5 #Displays how much operations you have answered incorrectly

a "Welcome! Welcome!{w=2.0} To the Math Quiz Game!"
a "I'm your host tonight,{w=2.0} Alex!"
a "Here, you have 5 tries to try and give the correct answer!{p=2.0}Do your best!"
scene class_closeup at truecenter with fade:
     zoom 0.27


label question:
show text("Correct!: [wins]                                              Lives: [lives]") at top
if firstrun == 1:
     "Next one is..."
$ firstrun = 1
$ aa = renpy.random.randint(2,5)
$ bb = renpy.random.randint(2,5)
$ numa = int(math.ceil(math.log(renpy.random.randint(math.pow(2, diff), math.pow(aa, diff)))))
$ numb = int(math.ceil(math.log(renpy.random.randint(math.pow(2, diff), math.pow(bb, diff)))))
$ op = renpy.random.randint(1, 2)

if op == 1:
     jump plus
else:
     jump minus

label plus:
python:
     ques = numa + numb
     try:
         ans = int(renpy.input("[numa] + [numb] equals...?", allow="1234567890"))
     except ValueError:
         ans = 0
jump checkans

label minus:
if numa >= numb:
     python:
          ques = numa - numb
          try:
              ans = int(renpy.input("[numa] - [numb] equals...?", allow="1234567890"))
          except ValueError:
              ans = 0
else:
     python:
          ques = numb - numa
          try:
              ans = int(renpy.input("[numb] - [numa] equals...?", allow="1234567890"))
          except ValueError:
              ans = 0
jump checkans

label checkans:
"Your answer was [ans]. That's{w=0.3}.{w=0.3}.{w=0.3}.{w=0.7}{nw}"
if ques == ans:
     jump correct
else:
     jump wrong

label correct:
$ wins+=1
$ diff+=1
"You're correct!"
jump question

label wrong:
$ lives-=1
if diff>=50:
     $ diff-=15
elif diff>=25:
     $ diff-=10
elif diff>=5:
     $ diff-=5
elif diff<5:
     $ diff-=1
if diff<0:
     $ diff=0
"Wrong! Too bad, try again!"
if lives==0:
     jump gameover
jump question

label gameover:
"GAME OVER"
a "Your score was [wins] this time around! Try again?"
menu:
     "Yes":
          jump start
     "No":
          a "See ya!"
          return
