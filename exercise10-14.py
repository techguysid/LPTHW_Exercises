#Exercise 10
tabby_cat = "\tI'm tabbed in."
persian_cat = "I'm split\non a line."
backslash_cat = "I'm \\ a \\ cat."
fat_cat = """
I'll do a list:
\t* Cat food
\t* Fishies
\t* Catnip\n\t* Grass
"""
print tabby_cat
print persian_cat
print backslash_cat
print fat_cat

#Exercise11
print "Exercise 11 starts here. Introduction to taking input from user using raw_input()."
#print "How old are you?",
#age = raw_input()
#print "How tall are you?",
#height = raw_input()
#print "How much do you weigh?",
#weight = raw_input()
#print "So, you're %r old, %r tall and %r heavy." % (
#age, height, weight)

#Exercise 12
#age = raw_input("How old are you? ")
#height = raw_input("How tall are you? ")
#weight = raw_input("How much do you weigh? ")
#print "So, you're %r old, %r tall and %r heavy." % (
#age, height, weight)


#Exercise 13
print "Exercise 13 is about Parameters, Unpacking, Variables."
#from sys import argv
#script, first, second, third = argv
#print "The script is called:", script
#print "Your first variable is:", first
#print "Your second variable is:", second
#print "Your third variable is:", third

#Exerice 14
from sys import argv
script, user_name = argv
prompt = '> '
print "Hi %s, I'm the %s script." % (user_name, script)
print "I'd like to ask you a few questions."
print "Do you like me %s?" % user_name
likes = raw_input(prompt)
print "Where do you live %s?" % user_name
lives = raw_input(prompt)
print "What kind of computer do you have?"
computer = raw_input(prompt)
print """
Alright, so you said %r about liking me.
You live in %r. Not sure where that is.
And you have a %r computer. Nice.
""" % (likes, lives, computer)
