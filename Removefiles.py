import os
import shutil
import time
def main():
    path = "deleting path"
    days = 30

    secs = time.time()-(days * (24*60*60))

    if(os.path.exists(path)):
        for folders, files, subfolders in os.walk(path):
            if secs >= os.stat(path).st_ctime(subfolders):
                shutil.rmtree(subfolders)
                break
            else: 
                for fol in folders:
                    folpath=os.path.join(subfolders, fol)
                    if secs >= os.stat(path).st_ctime(folpath):
                        shutil.rmtree(folpath)
                for fi in files: 
                    fipath = os.path.join(subfolders, fi)
                    if secs >= os.stat(path).st_ctime(fipath):
                        shutil.rmtree(fipath)

main()