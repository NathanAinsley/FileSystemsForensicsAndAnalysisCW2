import hashlib
import os
from prettytable import PrettyTable
#Loads Files from folder
items = os.listdir("images")
Files = []
for names in items:
	if names.endswith(".jpg"):
        	Files.append('images/'+names)

#Hashes file with MD5
def MD5(Files):
    hasher = hashlib.md5()
    with open(Files,'rb') as afile:
        buf = afile.read()
        hasher.update(buf)
        HASH = hasher.hexdigest()
    return(HASH)
#Hashes file with SHA256
def SHA(Files):
    hasher = hashlib.sha256()
    with open(Files,'rb') as afile:
        buf = afile.read()
        hasher.update(buf)
        HASH = hasher.hexdigest()
    return(HASH)
#Creates the Table
def TableData():
    i = 0
    table = PrettyTable(['ID','File','MD5','SHA-256'])
    while(i<len(Files)):
        table.add_row([i , Files[i] , MD5(Files[i]) , SHA(Files[i])])
        i+=1
    print(table)
    
TableData()
    