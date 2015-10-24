#脚本使用方法：
在CMD启动时需新建一个txt文档，以后日记的所有内容均保留在该文档中：
# 代码特点 #
使用了两个if语句，时间函数，以及文档的读写。并在每次daily更新后询问是否需要查看历史记录
# 代码设计过程中遇到的坑.. #
## 1.历史记录无法保存 ##

最初的设计版本中利用file = open(XX,'w')  file.write()实现了dairy对文档的写入。但在每次重新执行脚本时，历史记录被覆盖。 经过查询，发现 open（XX，'a') file.write()中的'w'会使[所有原来的内容都会被删除。如果想保留原来的内容，可以使用“a”方式在文件中结尾附加数据](http://maincoolbo.iteye.com/blog/626655)

## 2.时间模块的引入： ##
    import time   #调用时间函数
    
    now = time.strftime ("%Y-%m-%d %H:%M:%S")  #  显示载入程序时的时间

    print "Goodmoring sir.Now time is : %r" % now   #输出时间

时间的获取还有一种方式：

    import datetime
    
    now = datetime.datetime.now()
    
    print now  

[资料来源](http://outofmemory.cn/code-snippet/1841/python-time-date-module-usage-summary)  在第一种使用方式中，可以将不需要的组块删掉，从而避免使时间显示显得啰嗦  要注意 `%m`指的是月份，而`%M` 是指分钟。 %Y表示四位数年份，%y表征两位数年份。

## 3.if else语法 ##
注意if语句后面要有引号，后面引发的小程序要缩进四个字符。