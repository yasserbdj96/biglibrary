#!/usr/bin/env python
# coding:utf-8
# Code by : Yasser BDJ
# E-mail  : yasser.bdj96@gmail.com
"""
#set:usage.py,examples.py,changelog.txt
##################################################################
# USAGE :
#s
from biglibrary import *
#e
##################################################################
# EXAMPLES :
#s
from biglibrary import *

#make text in the center of terminal.
print(texts.center("hiii"))

#Return the list to a table:
li=["1996","2020","25/01/1996","yasserbdj96",'root96',"2021","corona","help","about"]
print(lists.ls_the_list(li," | "))
#OUTPUT:
'''
1996        | 2020        | 25/01/1996
yasserbdj96 | root96      | 2021
corona      | help        | about
'''
#e
##################################################################
# CHANGELOG :
#s
## 1.0.1
 - Fix bugs.

## 1.0.0
 - First public release.
#e
##################################################################
"""
# VALUES :
__version__="1.0.1"
__name__="biglibrary"
__author__="Yasser Bdj (Boudjada Yasser)"
__author_email__="yasser.bdj96@gmail.com"
__github_user_name__="yasserbdj96"
__title__="BIGlibrary"
__description__="A large library with many functions to facilitate and simplify the code, time and effort."
__author_website__=f"https://{__github_user_name__}.github.io/"
__source_code__=f"https://github.com/{__github_user_name__}/{__name__}"
__keywords__=[__github_user_name__,'python']
__keywords__.extend(__title__.split(" "))
__keywords__.extend(__description__.split(" "))
__install_requires__=['pipincluder']
__Installation__="pip install "+__name__+"=="+__version__
__license__='MIT License'
__copyright__='Copyright © 2008->Present, '+__author__+"."
__license_text__=f'''MIT License

{__copyright__}

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

You also agree that if you become very rich you will give me 1% of your wealth.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.'''
##################################################################
#s
try:
    from pipincluder import pipincluder
except:
    print("please use this command : pip install pipincluder")
    exit()

exec(pipincluder("import os,re").modules())

#texts:
class texts:
    #center:
    def center(text):
        w,h=os.get_terminal_size()
        texttocenter=len(text)
        w=((w-texttocenter)/2)
        w=str(w).split(".")[0]
        text=" "*int(w)+text
        return text

#lists:
class lists:
    #ls_the_list:
    def ls_the_list(list_con,commas=' | '):
        ls_the_list=""
        ls_the_list_len=[]
        ls=[]
        for i in range(len(list_con)):
            ls_the_list_len.append(int(len(re.sub(r'\\[0-9]+(\[|\])[0-9]*;?[A-Z]?', '',list_con[i]))))
        xx=max(ls_the_list_len)
        for i in range(len(list_con)):
            ls.append(list_con[i]+" "*(xx-int(ls_the_list_len[i])))
        #get_terminal_size
        ts=os.get_terminal_size()
        n=str(ts.columns/(xx+len(commas))).split(".")[0]
        for idx,key in enumerate(ls):
            if(idx+1)%int(n):
                ls_the_list+=key+commas
            else:
                ls_the_list+=key+'\n'

        return ls_the_list
#e