# dutil


from google colaboratory, you can upload text file as following
```
#file_upload_dialog
import google.colab.files as ggl
fname=ggl.upload()
print(fname)
#print_name
fname = [k for k in fname.keys()][0]
print(fname)
#change_the_json_name
import os
os.rename(fname,'dsecret.txt')
```
