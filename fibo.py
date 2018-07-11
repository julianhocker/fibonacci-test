# -*- coding: utf-8 -*-
"""
Created on Wed Jul 11 08:30:35 2018

@author: hocker
"""

##python2

##source: python documentation modules https://hackmd.io/ERXxduPVTPSc3LvSjL2nfw?view
def fib(n):    # write Fibonacci series up to n
   a, b = 0, 1
   while a < n:
       print(a, end=' ')
       a, b = b, a+b
   print()

def fib2(n):   # return Fibonacci series up to n
   """
   As described by Fibonacci et al.
   doi:sdfsdf
   can write more documentation here
   
   
   documentation testing: but not really comprehensive
   >>> from fibo import fib2
   >>> fib2(10)
   [0,1,1,2,3]
   """
   result = []
   a, b = 0, 1
   while a < n:
       result.append(a)
       a, b = b, a+b
   #result.append(10000)
   return result