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

def walk(top, topdown=True, onerror=None, use_nlink=1,filters=(fs_filters.no_hidden,fs_filters.no_system)):
    # use_nlink:
    #    0 = ignore nlink
    #    1 = try to use nlink
    #    2 = use nlink

    try:
        names = listdir(top)
    except error, err:
        if onerror is not None:
            onerror(err)
        return

    try:
        nlink = lstat(top).st_nlink
    except error:
        nlink = -1
    dirs, nondirs = [], []
    for name in names:
        passed = fs_filters.check_filters(top,name,lstat(join(top,name)),filters)
        if not passed: continue
        if use_nlink == 2 and nlink - 2 == len(dirs):
            nondirs.append(name)
        elif isrealdir(join(top, name)):
            dirs.append(name)
        else:
            nondirs.append(name)

    # if nlink seems ok, start trusting it
    if use_nlink == 1 and nlink - 2 == len(dirs):
        use_nlink = 2
        
    if topdown:
        yield top, dirs, nondirs
    for name in dirs:
        path = join(top, name)
        for x in walk(path, topdown, onerror, use_nlink):
            yield x
    if not topdown:
        yield top, dirs, nondirs

