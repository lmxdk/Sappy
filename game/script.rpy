﻿# You can place the script of your game in this file.

# Declare images below this line, using the image statement.
# eg. image eileen happy = "eileen_happy.png"

# Declare characters used by this game.
define l = Character('Lumberjack', color="#c8ffc8")
define t = Character('Tree', color="#c8ffc8")
define affinity = 20
define name = "the tree"
define nameCapped = "The tree"

image bg forest = "images/forest.png"
image tree = "images/tree.png"

image emotes bored = "images/emotes/bored.png"
image emotes cute = "images/emotes/cute.png"
image emotes pissed = "images/emotes/pissed.png"
image emotes proud = "images/emotes/proud.png"
image emotes relaxed = "images/emotes/relaxed.png"
image emotes relaxedBlush = "images/emotes/relaxedBlush.png"
image emotes shock = "images/emotes/shock.png"
image emotes shySmile = "images/emotes/shySmile.png"
image emotes superHappy = "images/emotes/superHappy.png"
image emotes unhappy = "images/emotes/unhappy.png"
image emotes okay = "images/emotes/okay.png"
image emotes content = "images/emotes/content.png"

image decoBoxers = "images/deco/boxers.png"
image decoCandles = "images/deco/candles.png"
image decoDecoration = "images/deco/decoration.png"
image decoLights = "images/deco/lights.png"
image decoPanties = "images/deco/panties.png"
image decoCloak = "images/deco/santacloak.png"

transform emotePos:
    xpos 812
    ypos 288

transform proudPos:
   xpos 819
   ypos 267

#415 103
# The game starts here.
label start:
   scene bg forest with fade

   show tree with dissolve

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
         show emotes content at emotePos with dissolve
         $ affinity += 1
         jump afterHi

      "Excuse me haven't I seen you before?":
         "The tree shrugs."
         show emotes content at emotePos with dissolve
         $ affinity += 2
         jump afterHi

label afterHi:

   l "Hi, I'm the lumberjack."
   l "I can't believe I haven't seen you before."
   $ affinity += 1
   define comeHereOften = False
   define whatsYourName = False
   define nameComeOn = False
   define hasLickedTheTree = False

label beforeName:
   if whatsYourName and comeHereOften:
      jump afterName

menu:
   "So… What's your name?" if whatsYourName == False:
      "The tree seems to give you a mysterious glance"
      show emotes okay at emotePos with dissolve
      $ affinity += 2
      $ whatsYourName = True
      jump chooseName

   "Do you come here often?" if comeHereOften == False:
      "[nameCapped] seems to be rolling it's cones at you. You find it oddly tittilating."
      show emotes cute at emotePos with dissolve
      $ affinity += 1
      $ comeHereOften = True
      jump beforeName

   "Lick the tree" if hasLickedTheTree == False:
      "You slowly move closer to [name], your tongue at the ready, salivating at the thought of licking the dew of the needles."
      "The fir however doesn't seem ready for this advance."
      show emotes pissed at emotePos with dissolve
      "A branch snaps and you feel a sharp slap across your cheek…"
      $ hasLickedTheTree = True
      $ affinity -= 2
      jump lickTheTree

label chooseName:
   menu:
      "Come on tell me?" if nameComeOn == False:
         "The tree seems impatient with you."
         show emotes bored at emotePos with dissolve
         $ nameComeOn = True
         $ affinity -= 1
         jump chooseName

      "Can I call you Needles?":
         "The tree doesn't seem to mind"
         show emotes content at emotePos with dissolve
         $ affinity += 1
         $ name = nameCapped = "Needles"
         jump beforeName

      "Can I call you Victorius Darrell?":
         "The tree seems to straighten it's trunk."
         show emotes proud at proudPos with dissolve
         $ affinity += 2
         $ name = nameCapped = "Victorius Darrell"
         jump beforeName

      "What if I call you Æðelmær?":
         "The tree seems to straighten it's trunk and basking in the wind."
         show emotes proud at proudPos with dissolve
         $ name = nameCapped = "Æðelmær"
         $ affinity += 3
         jump beforeName

label lickTheTree: 
   menu:
      "Sorry I was moving to fast.":
         "[nameCapped] seems to look back at you with a heavy grayish blush."
         show emotes shySmile at emotePos with dissolve
         $ affinity += 1
         jump beforeName

      "Why does it always have to end this way (Chop down the tree)?":
         "You take your heavy axe, and with a sigh you start chopping [name] down."
         show emotes shock at emotePos with dissolve
         "[nameCapped] seems to give you a look of horror."
         "Every chip of the axe makes all the delicate needles writhe in pain, until you hear a thumb and its all over."
         show emotes unhappy at emotePos with dissolve
         "The beautiful young fir lays bare in front of your boots on the moss filled ground."
         hide tree
         "You weep a little while you drag it away to your cabin, to do unspeakable things…"
         jump failed
           
label afterName:

   l "Look a three headed beaver!"
   "You point at the small bustling creek behind [name]."
   show emotes cute at emotePos with dissolve
   "[nameCapped] appears to give a nervous chuckle."
   $ affinity += 1
 
   menu:

      "Oh sorry, I guess that was a little insensitive of me.":
         l "I don't usually meet a lot of nice firs and I sometimes start to ramble."
         "[name]'s branches seems to relax a little."
         show emotes relaxed at emotePos with dissolve
         $ affinity += 2
         jump afterBeaver
      
      "You ever had a run in with a beaver, I hear they have nasty teeth?":
         "[name] seems to shake heavily in the breeze."
         show emotes unhappy at emotePos with dissolve
         l "No I guess you wouldn’t."
         l "Probably wouldn’t have been as pretty if you had."
         show emotes relaxedBlush at emotePos with dissolve
         $ affinity += 1
         jump afterBeaver

label afterBeaver: 

   menu:
      "Move clooser":
         "As you move a little closer, your hands gently brush against one of the branches."
         "A slight electrical charge sends a shiver down your spine as you look up at [name] which seems to smile shyly back at you."
         show emotes shySmile at emotePos with dissolve
         define lendMeSomeFir = False
         define touch = False
         define massage = False
         define dressBoxers = False
         define dressPanties = False
         define dressCandles = False
         define dressLights = False
         define dressCloak = False
         define dressDecorations = False
         define allDressed = False
         jump afterMove

label afterMove:
   if (allDressed and lendMeSomeFir and touch and massage):
      jump prepareIntimate

   menu: 
      "Uh, I feel a little bit cold, could you lend me some “fir”?" if lendMeSomeFir == False:
         "[nameCapped] appears to laugh loudly as the branches bob back and forth."
         show emotes superHappy at emotePos with dissolve
         "You feel a pricklish touch as a couple of the branches caress your back."
         $ lendMeSomeFir = True
         $ affinity += 3
         jump afterMove

      "Touch" if touch == False:
         "[nameCapped] doesn’t seem to mind your touch on its bark."
         show emotes content at emotePos with dissolve
         "The beautiful grayish bark with linings of smoked topaz brown is rugged yet soft and temperate."
         "The lines in the bark gives you the impression that [name] has had a tougher life than it had previously let on."
         $ touch = True
         $ affinity += 3
         jump afterMove

      "Massage" if massage == False:
         "Your hands gently wraps around the ankles of two boughs and your fingers try to push away the many years of stiffness."
         "Though your fingers merely scratch off some lichen, [name] seems grateful. You hear a sigh on the wind."
         show emotes okay at emotePos with dissolve
         $ affinity += 3
         $ massage = True
         jump afterMove

      "Dress" if allDressed == False:
         "What would you like to put on [name]?"
         jump dressMenu

label dressMenu:
   if dressBoxers and dressPanties and dressCandles and dressLights and dressCloak and dressDecorations:
      $ allDressed = True
      jump afterMove

   menu:
      "Panties" if dressPanties == False:
         "You pull out a fine pair bottomless laced silken panties."
         "[nameCapped] seems to glance curiously at you, while you pull the panties smoothly over some of its twigs."
         show emotes shySmile at emotePos with dissolve
         show decoPanties with dissolve
         $ affinity += 3
         $ dressPanties = True
         jump dressMenu

      "Boxers" if dressBoxers == False:
         "Not having an extra pair of boxers with you, you turn around self-consciously and take off your jeans and boxers."
         "Once again dressed you feel the tough fabric rub against you, as you turn back around with a bold smile waving your boxers at the tip of your finger."
         "[nameCapped] mostly seems to chuckle at this though."
         show emotes superHappy at emotePos with dissolve
         "You take the cotton undies and pull them determinately on a couple of twigs."
         show decoBoxers with dissolve
         "[nameCapped] seems confused but okay with it."
         show emotes cute at emotePos with dissolve
         $ affinity +=2
         $ dressBoxers = True
         jump dressMenu
      
      "Santa cloak" if dressCloak == False:
         l "Well I did say I was cold, so…"
         "You find your grandfathers worn santa cloak, that just happens to be in your rucksack."
         "[nameCapped] seems to look expectantly at you, while you wrap the coat and snuggle closer to the trunk."
         show decoCloak with dissolve
         show emotes okay at emotePos with dissolve
         $ affinity += 2
         $ dressCloak = True
         jump dressMenu
         
      "A low power, battery driven LED light chain." if dressLights == False:
         l "“Have you ever tried it while tied before?” you say with playful smile."
         "You reveal a line of lights from your padded vest."
         show emotes shySmile at emotePos with dissolve
         "[nameCapped] seems to look coyly at you."
         "You attach the line, and with an eager smile you entangle [name], tightening and tugging just a little bit extra."
         show decoLights with dissolve
         $ affinity += 4
         $ dressLights = True
         jump dressMenu

      "Candles" if dressCandles == False:
         "You pick up your lighter, and spark it while rummaging through your bag to find the wax candles your brought."
         show emotes shock at emotePos with dissolve
         "[nameCapped] seems to give a frightened shiver."
         $ affinity -= 2
         $ dressCandles = True
         jump candleMenu

      "Decorate" if dressDecorations == False:
         "Remembering the air of Christmas, the tree gave you earlier you grab some ornaments from your rucksack."
         l "“Is it okay?” you ask before decorating the tree."
         show emotes superHappy at emotePos with dissolve
         "[nameCapped] seems excited."
         show decoDecoration with dissolve
         $ affinity += 4
         $ dressDecorations = True
         jump dressMenu

      "Back":
         jump afterMove


label candleMenu:

   menu:
      "Oh sorry, of course you don’t like fire.":
         show emotes relaxed at emotePos with dissolve
         "You put away your lighter and [name] seems relieved."
         jump dressMenu

      "Don’t worry honey, I won’t burn you.":
         l "You finally find the candles. As you pull out the sticks you say “and it won’t hurt… too much.”"
         "You hold up the candle and light it dramatically, looking directly at [name] through the flickering flame."
         show emotes cute at emotePos with dissolve
         "[nameCapped] seems nervous but its interests seems to have been peaked."
         "You stand in anticipation while you wait for the wax to melt."
         "You quietly move the candle letting the hot wax drip strategically."
         "You place the candles, making sure not to come too close to burn [name]."
         show decoCandles with dissolve
         "As the wax lands it warms up the bark and the smell of resin becomes stronger."
         "[name] seems to writhe aroused by the cathartic pain."
         $ affinity += 6
         jump dressMenu

label prepareIntimate:
   define fondleRoots = False
   define lickResin = False
   define playWithHollow = False
   define spankYourself = False

label intimate:
   if fondleRoots and lickResin and playWithHollow and spankYourself:
      jump finale

   menu: 
      "Fondle roots" if fondleRoots == False:
         "You run your fingers along the hard trunk as you slowly get to your knees."
         show emotes relaxed at emotePos with dissolve
         "[nameCapped] seems excited."
         "As you get to the moss filled ground, you start to caress the exposed roots of [name]."
         "But as you dig your fingers around the roots, you feel as if [name] closes up its branches and shies away from you."
         show emotes unhappy at emotePos with dissolve
         $ fondleRoots = True
         $ affinity -= 2
         jump intimate

      "Lick resin" if lickResin == False:
         "You gently wrap your arms around the trunk and start to kiss and lick away at the resin that now flows readily."
         "You taste the sticky earthy gold drops as you feel [name] shivering with joy."
         show emotes superHappy at emotePos with dissolve
         $ lickResin = True
         $ affinity += 5
         jump intimate

      "Play with hollow" if playWithHollow == False:
         "You move your gaze to a small hollow, and then back questioning at [name]."
         "You smile as [name] sways as if it was nodding."
         show emotes relaxedBlush at emotePos with dissolve
         "With care you remove the small birds nest stuck in there."
         "[name] seems to rumble ticklishly."
         show emotes superHappy at emotePos with dissolve
         $ playWithHollow = True
         $ affinity += 3
         jump intimate

      "Spank yourself" if spankYourself == False:
         "You let your jeans drop and perk out your firm cheeks as if to let [name] know to spank them."
         show emotes proud at proudPos with dissolve
         "As the wind blows back and forth the branches hit with an exhilarating sting. With each hit you cry out in sweet agony while your cheeks slowly turn red."
         $ spankYourself = True
         $ affinity += 4         
         jump intimate

label finale:
   menu:
      "Shag":
         "You can’t hold yourself back anymore, your throw yourself at [name] who stands firm as you embrace it lovingly."
         show emotes relaxedBlush at emotePos with dissolve
         l "“You were always the strong one.” you say as you furiously unbutton your vest, shirt and bra."
         l "“Take me!” you say."
         "The air shakes while you slide into each other and begin to pulsate."
         "A short breath later you climax and while time stands still you see a seed drop from the tree and start to blossom. You fall to the ground happy and panting."
         "…After having cuddled for a fewer hours you find the sun setting. You kiss your love and head home to your cabin. You will never forget this."
         "Alas you know your love can never be. Maybe, just maybe one day you will return."
         jump credits

      "Chop down":
         "You can’t hold yourself back anymore, you grab your axe and with an incensed howl you start chopping [name] down."
         show emotes shock at emotePos with dissolve
         "[name] seems to give you a look of horror."
         "Every chip of the axe makes all the delicate needles writhe in pain, until you hear a thumb and it’s all over."
         show emotes unhappy at emotePos with dissolve
         "The beautiful young fir lays bare in front of your boots on the moss filled ground."
         hide tree
         "You weep a little while you drag it away to your cabin, to do unspeakable things…"
         jump failed

label failed: 
   return


label credits:
   return