from sys import argv
script , filename = argv
import time   #调用时间函数

now = time.strftime ("%Y-%m-%d %H:%M:%S")  #  显示载入程序时的时间
print "now time is : %r" % now
print "="*20

print "let's start writing"
line1 = raw_input ()
now1 = time.strftime ("%Y-%m-%d %H:%M:%S")  #读取写作时的时间

target = open(filename,'a')
target.write("creatime")
target.write(":")
target.write(now1)
target.write("\n")
target.write(line1)
target.write("\n")
target.write("\n")                    #两个空行起美观作用
target.close()

print "Here's your daily:"
print "="*20
daily = open(filename)
print daily.read()
print "="*20