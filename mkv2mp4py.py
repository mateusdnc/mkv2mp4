import os,time
from fnmatch import fnmatch

root = 'Series/'
pattern = "*.mkv"

for path, subdirs, files in os.walk(root):
    for name in files:
        if fnmatch(name, pattern):
            pathFile = (os.path.join(path, name)).replace("'","\\'").replace(" ","\\ ")
            print("Converting... "+pathFile)
            
            os.system("ffmpeg -i "+pathFile+" -c copy "+ pathFile[:-4]+".mp4")
            os.system("rm "+pathFile)
            time.sleep(5)
