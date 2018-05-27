#!/usr/bin/env python
# -*- coding: utf-8 -*-
import dropbox
import os

def token(path="./"):
    """
    path: full path of dropbox token text file
    """
    secret=[]
    secret_str=""
    with open(path+"dsecret.txt","r") as f:
        for l in f:
           secret.append(l.replace('\xef\xbb\xbf',""))
    secret_str=secret[0].replace('\ufeff',"")
    return secret_str

def display(token,path=''):
    """
    token: dutil.token()
    path: dropbox folder
    """
    display=[]
    dbx=dropbox.Dropbox(token)
    for entry in dbx.files_list_folder(path).entries:
        display.append(entry.name)
    return display

def dwnld(token,dbx_fpath,wtype='wb'):
    """
    token: dutil.token()
    path: dropbox folder    
    """
    dbx=dropbox.Dropbox(token)
    md, res = dbx.files_download(dbx_fpath)
    data = res.content
    #print(data)
    f_name=os.path.basename(dbx_fpath)
    print(f_name)
    f=open(f_name,wtype)
    f.write(data)
    f.close()
