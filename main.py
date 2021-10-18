import os.path
import datetime as dt
#initilizing variable
filesmodified=[]
suspiciousfiles=[]

path='c:\\'
now = dt.datetime.now()
# Sets the age in minutes when searching for modified timestamp
age = now-dt.timedelta(minutes=5)
oldfilename="this is a test"


for root, dirs,files in os.walk(path):
   for fname in files:
       path = os.path.join(root, fname)
       st = os.stat(path)
       # obtains the timestamp of file being analyzed
       mtime = dt.datetime.fromtimestamp(st.st_mtime)
       # if file age is within the 5 minute modified time stamp will enter into this if statement
       if mtime > age:
           # saving all modified files that have modified timestamp last 5 minutes
           filesmodified.append((path))
           #compare previous file name with current file name using the first 10 characters
           if oldfilename[:10]==fname[:10]:
               #if first 10 character of filename from previous loop == to current file name then add to list
               suspiciousfiles.append(oldfilename)
           oldfilename=fname

print("priting all modified files")
#this prints all modified files that have modified timestamp of 5 minutes
print(filesmodified)
#print('\n' * 5)
print("printing suspicious looking files. meaning these files have duplicate names")
print(suspiciousfiles)

