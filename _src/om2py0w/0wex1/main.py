from sys import argv
script , filename = argv

print "let's start writing"
line1 = raw_input ()

target = open(filename,'a')
target.write(line1)
target.write("\n")
target.write("\n")
target.close()

print "Here's your daily"
daily = open(filename)
print daily.read()