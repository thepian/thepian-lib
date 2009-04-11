
def check_filters(base_path,file_name,lstat_info,filters):
    for f in filters:
        r = f(base_path,file_name,lstat_info)
        if r is True:
            return True
        if r is False:
            return False
    return True
        

def no_hidden(base_path,file_name,lstat_info):
    if file_name.startswith("."):
        return False
        
def no_system(base_path,file_name,lstat_info):
    if file_name == ".DS_Store":
        return False
        
def no_directories(base_path,file_name,lstat_info):
    from stat import S_ISDIR, ST_MODE
    if not lstat_info:
        return False
    if S_ISDIR(lstat_info[ST_MODE]):
        return False
        
def only_directories(base_path,file_name,lstat_info):
    from stat import S_ISDIR, ST_MODE
    if not lstat_info:
        return False
    if not S_ISDIR(lstat_info[ST_MODE]):
        return False
        
class fnmatch(object):
    def __init__(self,pattern):
        self.pattern = pattern
        
    def __call__(self,base_path,file_name,lstat_info):
        from fnmatch import fnmatch
        if not fnmatch(file_name,self.pattern):
            return False
    