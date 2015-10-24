from sys import argv
script , filename = argv

line1 = raw_input ("let's start writing")

target = open(filename)
target.write(line1)
target.write("\n")
