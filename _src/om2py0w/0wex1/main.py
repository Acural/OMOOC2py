from sys import argv
script , filename = argv

print "let's start writing"
line1 = raw_input ()

target = open(filename,'w')
target.write(line1)
target.write("\n")
