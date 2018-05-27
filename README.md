# dutil

install dropbpx by pip  
```
! pip install dropbox
```  

create text file which include Generated access token in first line  
from google colaboratory, you can upload text file as following
```
#file_upload_dialog
import google.colab.files as ggl
fname=ggl.upload()
print(fname)
#print_name
fname = [k for k in fname.keys()][0]
print(fname)
#change fname
import os
os.rename(fname,'dsecret.txt')
```

check drop box folder like this:
```
from dutil import dutil
dbx = dutil.token()
dutil.display(dbx)
```
