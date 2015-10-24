# -*- coding: utf-8 -*-
from sys import argv
script , filename = argv
import time   #调用时间函数

now = time.strftime ("%Y-%m-%d %H:%M:%S")  #  显示载入程序时的时间
print "Goodmoring sir.Now time is : %r" % now

print "do you want write your daily? Y or N"
key = raw_input("???")

if key == "N":
    print "bye~ system closed."
else:
    print "="*20
    print "all system go,let's start writing"
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

    print "do you want to read your daily? Y or N"
    answer = raw_input (">")

    if answer == "Y" : 

        print "Here's your daily:"
        print "="*20
        daily = open(filename)
        print daily.read()
        print "="*20
    else:
        print "bye,system closed"