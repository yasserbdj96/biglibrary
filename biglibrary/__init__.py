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
import os

#start biglibrary class:
class biglibrary:
    #__init__:
    def __init__(self,**kwargs):
        try:
            self.retu=kwargs["returning"]
        except:
            pass

    #center:
    def center(self,text):
        try:
            import shutil
            ts = shutil.get_terminal_size(fallback=(120, 50))
        except:
            ts=os.get_terminal_size(0)
        w=ts.columns
        texttocenter=len(text)
        w=((w-texttocenter)/2)
        w=str(w).split(".")[0]
        text=" "*int(w)+text
        try:
            if self.retu==False:
                print(text)
            else:
                return text
        except:
            print(text)
    
    def lslist(self,lslist,separator='|'):
        lslist_final=""
        try:
            import shutil
            ts = shutil.get_terminal_size(fallback=(120, 50))
        except:
            ts=os.get_terminal_size(0)
        ss=len(max(lslist,key=len))
        n=str(ts.columns/(ss+len(separator))).split(".")[0]
        for idx,key in enumerate(lslist):
            if(idx+1)%int(n):
                lslist_final+=key+(ss-len(key))*" "+f'{separator}'
            else:
                lslist_final+=key+'\n'
        try:
            if self.retu==False:
                print(lslist_final)
            else:
                return lslist_final
        except:
            print(lslist_final)
#}END.