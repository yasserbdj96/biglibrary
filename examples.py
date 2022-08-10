#!/usr/bin/env python
# coding:utf-8
#   |                                                          |
# --+----------------------------------------------------------+--
#   |   Code by : yasserbdj96                                  |
#   |   Email   : yasser.bdj96@gmail.com                       |
#   |   Github  : https://github.com/yasserbdj96               |
#   |   BTC     : bc1q2dks8w8uurca5xmfwv4jwl7upehyjjakr3xga9   |
# --+----------------------------------------------------------+--  
#   |        all posts #yasserbdj96 ,all views my own.         |
# --+----------------------------------------------------------+--
#   |                                                          |

#START{
from biglibrary import *

# string:
str="hello world!"

# list:
lslist=['orange','pear','kiwi','apple','banana','strawberry','watermelon','pineapple']

# :
bl=biglibrary()# Default returning=False, False for print, True for return.

# Placing text in the middle of the command line interface:
bl.center(str)

# Arrange list and items according to the length of the command line interface:
bl.lslist(lslist,separator=" | ")# Default separator=" | ".
#}END.