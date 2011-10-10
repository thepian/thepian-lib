import os
base_dir = os.path.dirname(__file__)
dir1 = os.path.join(os.path.dirname(__file__),'dir1')
dir2 = os.path.join(os.path.dirname(__file__),'dir1','dir2')
dir3 = os.path.join(os.path.dirname(__file__),'dir3')
dir4 = os.path.join(os.path.dirname(__file__),'dir4')
dir5 = os.path.join(os.path.dirname(__file__),'dir4',"dir5")
dir6 = os.path.join(os.path.dirname(__file__),'dir4',"dir6")
dir7 = os.path.join(os.path.dirname(__file__),'dir4',"dir6","dir7")
del os

import fs

def test_walk():
    l = [(top, dirs, nondirs) for top, dirs, nondirs in fs.walk(dir4)]
    assert l == [
        (dir4, ["dir5","dir6"], ["test3.test"]),
        (dir5, [], ["test2.test"]),
        (dir6, ["dir7"], []),
        (dir7, [], ["test.test"]),
    ]
    
    l = [(top, dirs, nondirs) for top, dirs, nondirs in fs.walk("dir4",base=base_dir)]
    assert l == [
        ("dir4", ["dir5","dir6"], ["test3.test"]),
        ("dir4/dir5", [], ["test2.test"]),
        ("dir4/dir6", ["dir7"], []),
        ("dir4/dir6/dir7", [], ["test.test"]),
    ]
    
def test_listdir_stats():
    l = fs.listdir(dir1)
    assert len(l) == 1
    assert l[0] == "dir2"
    
    l2 = fs.listdir(dir1,filters=(fs.filters.no_system,))
    assert len(l2) == 1
    
    l3 = fs.listdir(dir1,filters=(fs.filters.no_system,fs.filters.no_directories))
    assert len(l3) == 0

def test_listdir_path():
    l4 = fs.listdir(dir1,full_path=True)
    assert l4 == [ dir2 ]

    l5 = fs.listdir("dir3",base=base_dir)
    assert l5 == ["file1.test1","file2.test2","file3.test1"]
    
    l6 = fs.listdir("dir1",base=base_dir,full_path=True)
    assert l6 == [ "dir1/dir2" ]

def test_listdir_recursed():
    l = fs.listdir(dir4,recursed=True)
    assert l == ["test3.test","dir5/test2.test","dir6/dir7/test.test"]

    l = fs.listdir("dir4",recursed=True,base=base_dir)
    assert l == ["test3.test","dir5/test2.test","dir6/dir7/test.test"]

    l = fs.listdir("dir4",recursed=True,base=base_dir,full_path=True)
    assert l == ["dir4/test3.test","dir4/dir5/test2.test","dir4/dir6/dir7/test.test"]

def test_fnmatch():
    l = fs.listdir(dir3)
    assert len(l) == 3
    assert l == ["file1.test1","file2.test2","file3.test1"]
    
    l2 = fs.listdir(dir3,filters=(fs.filters.fnmatch("*.test1"),))
    assert l2 == ["file1.test1","file3.test1"]
    
    l3 = fs.listdir(dir3,filters=(fs.filters.fnmatch("*.test2"),))
    assert l3 == ["file2.test2",]

def test_exclude_paths():
    l = fs.listdir(dir3,filters=(fs.filters.exclude_paths(["*.test2","*.test3"]),))
    assert l == ["file1.test1","file3.test1"]

    