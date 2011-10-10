from os import error, listdir, lstat
from os.path import join, isdir, islink
from stat import S_ISDIR

from fs import filters as fs_filters

def isrealdir(path):
    try:
        st = lstat(path)
    except error:
        return False
    return S_ISDIR(st.st_mode)

def walk(top, topdown=True, onerror=None, use_nlink=1,filters=(fs_filters.no_hidden,fs_filters.no_system),base=None):
    # use_nlink:
    #    0 = ignore nlink
    #    1 = try to use nlink
    #    2 = use nlink

    path = base and join(base,top) or top
    try:
        names = listdir(path)
    except error, err:
        if onerror is not None:
            onerror(err)
        return

    try:
        nlink = lstat(path).st_nlink
    except error:
        nlink = -1
    dirs, nondirs = [], []
    for name in names:
        passed = fs_filters.check_filters(base or "",top,name,lstat(join(path,name)),filters)
        if not passed: continue
        if use_nlink == 2 and nlink - 2 == len(dirs):
            nondirs.append(name)
        elif isrealdir(join(base or "", top, name)):
            dirs.append(name)
        else:
            nondirs.append(name)

    # if nlink seems ok, start trusting it
    if use_nlink == 1 and nlink - 2 == len(dirs):
        use_nlink = 2
        
    if topdown:
        yield top, dirs, nondirs
    for name in dirs:
        for x in walk(join(top,name), topdown=topdown, onerror=onerror, use_nlink=use_nlink,filters=filters,base=base):
            yield x
    if not topdown:
        yield top, dirs, nondirs

