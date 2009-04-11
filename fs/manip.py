import os
from os.path import exists, lexists, join

def symlink(src,dest,replace=True):
    if lexists(dest):
        if not replace:
            return
        os.remove(dest)
    os.symlink(src,dest)
    
def link(src,dest,replace=True):
    if exists(dest):
        if not replace:
            return
        os.remove(dest)
    os.link(src,dest)
    
def first_exists(name_list):
    """Return the first file or directory in the supplied list that exists"""
    for fn in name_list:
        if exists(fn):
            return fn
    return None
