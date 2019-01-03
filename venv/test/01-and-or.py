#-*- coding:utf-8 -*-
"""
@author:ypp

Created on datetime:2019/1/3 10:41
"""
a = 'a'
b = 'b'
c = ''  #' '空格不为假
d = 0
'''
1) and 操作
a and b ：1.如果a,b都为真，则返回最后一个值（不是bool型）
          2.如果有一个不为真，则返回为假的变量的值
          3.如果都为假，则返回第一个变量的值
'''
def and_operate():
    #1.如果a,b都为真，则返回最后一个值（不是bool型）
    str = a and b
    print str    #>>>'b'
    str = b and a
    print str    #>>>'a'


    #2.如果有一个不为真，则返回第一个为假的变量的值
    str1 = a and c
    print str1   #>>>''
    str2 = c and b
    print str2   #>>>''

    #3.如果都为假，则返回第一个变量的值
    str = c and d
    print 'this is _{}_'.format(str)   #>>>''

    str = d and c

    print str   #>>>0

'''
2) or操作
    从左到右计算，遇到第一个为真的就返回该真值变量; 如果都为假，则返回最后一个假值。
'''
def or_operate():
    print a or b
    print b or a
    print a or c
    print c or a
    print c or d
    print d or c  #输出最后一个假值
'''
3) and-or 运算
    1）如果a为真则和bool?a:b 运算一样
    2）如果a为假则输出b
'''
def and_or():
    h = 0
    str = 1 and a or b
    print str
    str = 1 and d or b
    print str
and_or()
