# You can place the script of your game in this file.

# Declare images below this line, using the image statement.
# eg. image eileen happy = "eileen_happy.png"

# Declare characters used by this game.
define l = Character('Lumberjack', color="#c8ffc8")
define t = Character('Tree', color="#c8ffc8")


# The game starts here.
label start:

   "You see a sultry young fir tree in the prime of its youth."
   "It's stands tall and dignified almost as if it hadn't noticed you."
   "Small pieces of morning dew glistening on its spiky green needles."
   $ hi = False
       
label hiBranch:
   menu:

      "Hi" if hi == False:
         "The tree doesn't seem to notice you."
         $ hi = True
         jump hiBranch

      "Well, well, what's a fine young fir do in a place like this?":
         t "..."
         jump afterHi

      "Excuse me haven't I seen you before?":
         "The tree shrugs."
         jump afterHi

label afterHi:

   l "I'm the lumberjack. I can't believe I haven't seen you before."
   return
