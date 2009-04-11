import os
dir1 = os.path.join(os.path.dirname(__file__),'dir1')
dir3 = os.path.join(os.path.dirname(__file__),'dir3')
del os

import fs

def test_walk():
    pass
    
def test_listdir():
    l = fs.listdir(dir1)
    assert len(l) == 1
    assert l[0] == "dir2"
    
    l2 = fs.listdir(dir1,filters=(fs.filters.no_system,))
    assert len(l2) == 1
    
    l3 = fs.listdir(dir1,filters=(fs.filters.no_system,fs.filters.no_directories))
    assert len(l3) == 0
    
def test_fnmatch():
    l = fs.listdir(dir3)
    assert len(l) == 3
    assert l == ["file1.test1","file2.test2","file3.test1"]
    
    l2 = fs.listdir(dir3,filters=(fs.filters.fnmatch("*.test1"),))
    assert l2 == ["file1.test1","file3.test1"]
    
    l3 = fs.listdir(dir3,filters=(fs.filters.fnmatch("*.test2"),))
    assert l3 == ["file2.test2",]
    