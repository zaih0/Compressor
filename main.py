import gzip
import shutil
import os
import sys
import io
import subprocess
import tkinter
from tkinter import messagebox as mb
from tkinter import filedialog as fd 
import pickle


fName = fd.askopenfilename(
     title = "Select a file of any type",
    filetypes = [("All files", "*.*")],
    
    )

E_name = str.encode(fName)
content = bytes(E_name)


gzip.compress(content)
with open(content, 'rb') as f_in:
    with gzip.GzipFile(fName + '.gz', 'wb', compresslevel=9) as f_out:
        shutil.copyfileobj(f_in, f_out)



print("Your File has been compressed")