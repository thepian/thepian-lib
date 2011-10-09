import os
from fs.listdir import _permissive_lstat
base_dir = os.path.dirname(__file__)
dir1 = os.path.join(os.path.dirname(__file__),'dir1')
dir3 = os.path.join(os.path.dirname(__file__),'dir3')
dir2_stats = _permissive_lstat(os.path.join(dir1,"dir2"))
file1_stats = _permissive_lstat(os.path.join(dir3,"file1.test1"))
del os

import fs
from fs.listdir import _permissive_lstat
from fs.filters import *

def test_filters_directories():
    assert check_filters(base_dir, "dir1", "dir2", dir2_stats, filters=(only_directories,)) is True
    assert check_filters(base_dir, "dir1", "file1.test1", file1_stats, filters=(only_directories,)) is False
    assert check_filters(base_dir, "dir1", "dir2", dir2_stats, filters=(no_directories,)) is False
    assert check_filters(base_dir, "dir1", "file1.test1", file1_stats, filters=(no_directories,)) is True

def test_filters_hidden():    
    assert check_filters(base_dir, "dir1", ".dir2", dir2_stats, filters=(only_hidden,)) is True
    assert check_filters(base_dir, "dir3", ".file1", dir2_stats, filters=(only_hidden,)) is True
    assert check_filters(base_dir, "dir1", ".dir2", dir2_stats, filters=(no_hidden,)) is False
    assert check_filters(base_dir, "dir3", ".file1", dir2_stats, filters=(no_hidden,)) is False
    
def test_filters_system():
    assert check_filters(base_dir, "dir1", "dir2", dir2_stats, filters=(no_system,)) is True
    assert check_filters(base_dir, "dir1", "dir2", dir2_stats, filters=(no_system,only_directories)) is True
    assert check_filters(base_dir, "dir1", "dir2", dir2_stats, filters=(no_system,no_directories)) is False
    
    # TODO system stat variables
    
def test_filters_fnmatch():
    assert check_filters(base_dir, "dir1", "dir2", dir2_stats, filters=(fnmatch("dir*"),)) is True
    assert check_filters(base_dir, "dir1", "dir2", dir2_stats, filters=(fnmatch("dir-*"),)) is False
    assert check_filters(base_dir, "dir1", "dir2.x", dir2_stats, filters=(fnmatch("*.x"),)) is True
    assert check_filters(base_dir, "dir1", "dir2.x", dir2_stats, filters=(fnmatch("*.y"),)) is False
    assert check_filters(base_dir, "dir1", "dir2.x", dir2_stats, filters=(fnmatch("dir*.x"),)) is True
    assert check_filters(base_dir, "dir1", "dir2.x", dir2_stats, filters=(fnmatch("dir*.y"),)) is False
    assert check_filters(base_dir, "dir1", "file1.test1", file1_stats, filters=(fnmatch("*.test1"),)) is True
    assert check_filters(base_dir, "dir1", "dir2", dir2_stats, filters=(fnmatch("dir*"),only_directories)) is True
    assert check_filters(base_dir, "dir1", "dir2", dir2_stats, filters=(fnmatch("dir*"),only_directories,no_system)) is True
    