from stat import *

def check_filters(base_path,rel_path,file_name,lstat_info,filters):
    for f in filters:
        r = f(base_path,rel_path,file_name,lstat_info)
        if r is True:
            return True
        if r is False:
            return False
    return True
        

def no_hidden(base_path,rel_path,file_name,lstat_info):
    """Exclude any hidden directory or file"""
    if file_name.startswith("."):
        return False
        
def only_hidden(base_path,rel_path,file_name,lstat_info):
    """Exclude any non-hidden file or directory"""
    if not file_name.startswith("."):
        return False

def any_hidden(base_path,rel_path,file_name,lstat_info):
    """Include any file or directory that is hidden"""
    if file_name.startswith("."):
        return True

def no_system(base_path,rel_path,file_name,lstat_info):
    if not lstat_info:
        return False
    if S_ISCHR(lstat_info[ST_MODE]):
        return False
    if S_ISSOCK(lstat_info[ST_MODE]):
        return False
    if S_ISFIFO(lstat_info[ST_MODE]):
        return False
    if file_name in (".DS_Store",".Trashes",".fseventsd",".hotfiles.btree",".vol"):
        return False
        
def no_directories(base_path,rel_path,file_name,lstat_info):
    if not lstat_info:
        return False
    if S_ISDIR(lstat_info[ST_MODE]):
        return False
        
def only_directories(base_path,rel_path,file_name,lstat_info):
    if not lstat_info:
        return False
    if not S_ISDIR(lstat_info[ST_MODE]):
        return False
        
class fnmatch(object):
    def __init__(self,pattern):
        self.pattern = pattern
        
    def __call__(self,base_path,rel_path,file_name,lstat_info):
        from fnmatch import fnmatch
        if not fnmatch(file_name,self.pattern):
            return False

class exclude_paths(object):
    def __init__(self,excludes):
        specific = []
        wildcards = []
        for e in excludes:
            if "*" in e: 
                wildcards.append(e)
            else:
                specific.append(e)
        self.specific = set(specific)
        self.wildcards = wildcards

    def __call__(self,base_path,rel_path,file_name,lstat_info):
        from fnmatch import fnmatch
        from os.path import split

        if rel_path in self.specific:
            return False

        for e in self.wildcards:
            if fnmatch(file_name,e):
                return False


    