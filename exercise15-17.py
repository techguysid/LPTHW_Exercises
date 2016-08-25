#Exercise 15
from sys import argv
script, filename = argv
txt = open(filename)
print "Here's your file %r:" % filename
print txt.read()
print "Type the filename again:"
file_again = raw_input("> ")
txt_again = open(file_again)
print txt_again.read()

#Exercise 16
print "Exercise 16 starts here."
from sys import argv
script, filename = argv
print "We're going to erase %r." % filename
print "If you don't want that, hit CTRL- C (^C)."
print "If you do want that, hit RETURN."
raw_input("?")
print "Opening the file..."
target = open(filename, 'w')
print "Truncating the file."
target.truncate()
print "Goodbye!"
print "Now I'm going to ask you for three lines."
line1 = raw_input("line 1: ")
line2 = raw_input("line 2: ")
line3 = raw_input("line 3: ")
print "I'm going to write these to the file."
target.write(line1)
target.write("\n")
target.write(line2)
target.write("\n")
target.write(line3)
target.write("\n")
print "And finally, we close it."
target.close()

#Exercise 17
print "Exercise 17 starts here where we will copy the content of one file to another."
from sys import argv
from os.path import exists
script, from_file, to_file = argv
print "Copying from %s to %s" % (from_file, to_file)
# we could do these two on one line too, how?
in_file = open(from_file)
indata = in_file.read()
print "The input file is %d bytes long" % len(indata)
print "Does the output file exist? %r" % exists(to_file)
print "Ready, hit RETURN to continue, CTRL- C to abort."
raw_input()
out_file = open(to_file, 'w')
out_file.write(indata)
print "Alright, all done."
out_file.close()
in_file.close()
