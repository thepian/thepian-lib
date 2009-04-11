import os
import filters as fs_filters
from walk import walk

def listdir(dir_path,filters=(fs_filters.no_hidden,fs_filters.no_system),full_path=False,recursed=False):
    if recursed:
        r = []
        for top,dirs,nondirs in walk(dir_path):
            if full_path:
                r.extend([os.path.join(top,nd) for nd in nondirs])
            else:
                r.extend([nd for nd in nondirs])
        return r
    if full_path:
        return [os.path.join(dir_path,name) for name in os.listdir(dir_path) if fs_filters.check_filters(dir_path,name,os.lstat(os.path.join(dir_path,name)),filters)]
    return [name for name in os.listdir(dir_path) if fs_filters.check_filters(dir_path,name,os.lstat(os.path.join(dir_path,name)),filters)]
    
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
