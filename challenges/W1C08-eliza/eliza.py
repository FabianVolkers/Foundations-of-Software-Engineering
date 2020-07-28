name = input ("Hello, I am Eliza! What is your name?  ")
print ("Hello",name)
question = input ("Tell me about your day  ")
print ("That sounds interesting... ")
again = input ("Tell me some more!  ")
feeling = input ("And how does that make you feel?  ")
print ("Hmm...I see. ")
yes_no = input ("Have you tried to speak to someone about it?  ")
if yes_no == ("yes"):
  print ("That's great! You should always tell someone you trust when you feel", feeling)
  print ("Maybe they can help you better than me :) ")
elif yes_no == ("no"):
  print ("That doesn't sound very healthy! You should always talk to someone when you feel", feeling)
  print ("Go on, tell the person you trust most, then come back to talk about how that makes you feel")
else:
  print ("You can't hide things from your therapist, this is supposed to be a relationship built on trust. I don't think we can work together anymore.")
print ("Good bye and good luck!")