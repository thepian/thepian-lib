import os
import filters as fs_filters
from walk import walk

def listdir(dir_path,filters=(fs_filters.no_hidden,fs_filters.no_system),full_path=False,recursed=False,followlinks=True,base=None):
    with_base = os.path.join(base or "",dir_path)
    prefix = len(dir_path)
    if dir_path[-1] != "/": 
        prefix += 1

    r = []
    if recursed:
        r = []
        for top,dirs,nondirs in walk(dir_path,use_nlink = followlinks and 2 or 1,filters=filters,base=base):
            r.extend([(top[prefix:],nd) for nd in nondirs])
    else:
        def check(name):
            #TODO consider (base, dir_path,name, ...)
            return fs_filters.check_filters(dir_path, "", name, os.lstat(os.path.join(base or "",dir_path,name)),filters)
        r = [("",name) for name in os.listdir(with_base) if check(name)]

    if full_path:
        return [os.path.join(dir_path,rel,name) for rel,name in r]

    return [os.path.join(rel,name) for rel,name in r]
 


def _permissive_lstat(path):
    try:
        return os.lstat(path)
    except OSError:
        return None
        
def filterdirs(dirs,base_dir=None,filters=(fs_filters.only_directories,),full_path=False):
    
    if base_dir:
        if full_path:
            return [os.path.join(base_dir,path) for path in dirs if fs_filters.check_filters(base_dir,path,_permissive_lstat(os.path.join(base_dir,path)),filters)]
        return [path for path in dirs if fs_filters.check_filters(base_dir,path,_permissive_lstat(os.path.join(base_dir,path)),filters)]
        
    return [path for path in dirs if fs_filters.check_filters(os.path.dirname(path),os.path.split(path)[1],_permissive_lstat(path),filters)]
