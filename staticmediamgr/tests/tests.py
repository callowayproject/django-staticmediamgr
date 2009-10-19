import sys, os, shutil

sys.path.append(os.path.dirname(os.path.dirname(__file__)))
import utils


srcpath = os.path.abspath(os.path.join(os.path.dirname(__file__), 'srcdir'))
dstpath = os.path.abspath(os.path.join(os.path.dirname(__file__), 'dstdir'))
try:
    os.makedirs(srcpath)
except:
    pass
try:
    os.makedirs(dstpath)
except:
    pass
f = open(os.path.join(srcpath, 'tmp1'), 'w')
f.close()
utils.copydir(srcpath, dstpath)
shutil.rmtree(srcpath)
shutil.rmtree(dstpath)