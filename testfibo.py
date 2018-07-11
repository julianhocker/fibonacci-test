# -*- coding: utf-8 -*-
"""
Created on Wed Jul 11 11:17:56 2018

@author: hocker

Testing. gives back an assertion error, if something is wrong
"""

import fibo

##this program does some tests on fibo
def test_fibo_10():
    result_10 = fibo.fib2(10)
    expected_result = [0,1,1,2,3,5,8]
    assert result_10 == expected_result
    
    
def test_fibo_0():
    result_0 = fibo.fib2(0)
    expected_result = []
    assert result_0 == expected_result

def test_fib_5():
    result_5 = fibo.fib2(5)
    expected_result = [0,1,1,2,3]
    assert result_5 == expected_result

def test_fib_type():
    result_5 = fibo.fib2(5)
    assert type(result_5) == list

#test_fibo_10()
#test_fibo_0()
"""
number = fibo.fib2(0)
print(number)
"""

##call this with testfibo.py; from spyder or ipython: !testfibo.py
##test looks at all the functions starting with test_
