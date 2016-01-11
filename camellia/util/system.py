import os
import shutil
import tempfile
import datetime
import collections

def exists(filename):
    return os.path.exists(filename)

def mkdir(dirname):
    if not exists(dirname):
        os.makedirs(dirname)
    return dirname

def rmdir(dirname):
    if exists(dirname):
        return shutil.rmtree(dirname)

def touch(filename, refresh=False):
    filepath = os.path.abspath(filename)
    mkdir(os.path.dirname(filepath))
    f = filepath.split(os.sep)[-1]
    if not exists(filepath):
        open(filepath, 'w').close()
    elif refresh:
        with open(filepath, 'w') as f: pass
    return filepath

def uniq(filename):
    dstr = datetime.datetime.today().strftime("%Y%m%d_%H%M%S")
    filepath = os.path.normpath(os.path.join(filename, dstr))
    return touch(filepath)

def mv(src, dist):
    if exists(src) and exists(dist):
        shutil.move(src, dist)

def rm(filename):
    if exists(filename):
        return os.remove(filename)

if __name__ == "__main__":
    import time
    d = mkdir("sample")
    time.sleep(10)
    rmdir(d)
    f = touch("hogehoge.txt")
    time.sleep(10)
    rm(f)
