from file_util import *
from walk import walk
from listdir import listdir,filterdirs
from distutils.dir_util import copy_tree
from manip import link,symlink,first_exists

def makedirs(*elements):
    import os
    from os.path import exists, join
    dirs = join(*elements)
    if not exists(dirs):
        os.makedirs(dirs)
        
mkpath = makedirs
makepath = makedirs

def makedirs_tree(base_dir,dirs):
    """
    Take a list of directory names(string or tuple) and create a tree in base_dir
    """
    import os
    from os.path import exists, join
    for dir in dirs:
        if type(dir) == tuple: dir = join(dir)
        dir = join(base_dir,dir)
        if not exists(dir):
            os.makedirs(dir)
            

"""
class paths:
    __init__(*paths,root="/"):
    
"""