﻿#-*- coding: utf-8 -*-
#Quick Python Script Explanation for Progeammers
#������Ա�ĳ�����Py�ű���˵.........
import os

def main():
    print 'Hello World:'
	
    print "����Alice\���ʺ�."
    print '����Bob\ �����ʺ�'

    foo(5,10)

    print '=' * 10
    print '�⽫ֱ��ִ��'+os.getcwd()

    counter = 0
    counter += 1 
    
    food = ['ƻ��','����','����','��']
    for i in food :
        print '���Ͱ���ֻ:'+i 

    print '����10'
    for i in range(10):
        print i 

def foo(param1, secondParam):
    res = param1+secondParam
    print '%s �� %s ���� %s'%(param1, secondParam, res)
    if res < 50:
	    print '���'
    elif (res>=50) and ((param1==42) or (secondParam==24)):
	    print '�Ǹ�'
    else:
	    print '�š�����'
    return res 
	

if __name__=='__main__':
    main()
