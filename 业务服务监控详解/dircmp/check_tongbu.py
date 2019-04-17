#!/usr/bin/python
# -*- coding: utf-8 -*-
#用于备份目录和源目录校验和同步，使用filecmp模块的 left_only,diff_files方法递归获取源目录的更新项，再通过shutil.copyfile,os.makedirs方法对更新项进行复制。

import os,sys
import filecmp
import re
import shutil

holderlist = []

#递归获取更新项函数
def compareme(dir1,dir2):
    dircomp = filecmp.dircmp(dir1,dir2)
    #源目录新文件或目录
    only_in_one = dircomp.left_only
    #不匹配文件
    diff_in_one = dircomp.diff_files
    #定义源目录绝对路径
    dirpath = os.path.abspath(dir1)
    #将更新文件名或目录追加到holderlist
    [holderlist.append(os.path.abspath(os.path.join(dir1,x))) for x in only_in_one]
    [holderlist.append(os.path.abspath(os.path.join(dir1,x))) for x in diff_in_one]
    #判断是否存在相同子目录，以便递归
    if len(dircomp.common_dirs) > 0:
        #递归子目录
        for item in dircomp.common_dirs:
            compareme(os.path.abspath(os.path.join(dir1,item)),os.path.abspath(os.path.join(dir2,item)))
    return holderlist

test = compareme('./dir1','./dir2')
print test


def main():
    #要求输入源目录与备份目录
    if len(sys.argv) > 2:
        dir1 = sys.argv[1]
        dir2 = sys.argv[2]
    else:
        print "Usage: ", sys.argv[0], "datadir backupdir"
        sys.exit()
    #对比源目录和备份目录
    source_files = compareme(dir1,dir2)
    dir1 = os.path.abspath(dir1)

    #备份目录路径加"/"符
    if not dir2.endswith('/'):
        dir2 = dir2 + '/'
    dir2 = os.path.abspath(dir2)
    destination_files = []
    createdir_bool = False

    #遍历返回的差异文件或目录清单
    for item in source_files:
        #将源目录差异路径清单对应替换成备份目录
        destination_dir = re.sub(dir1,dir2,item)
        destination_files.append(destination_dir)
        #如果差异路径为目录且不存在，则在备份目录中创建
        if os.path.isdir(item):
            if not os.path.exists(destination_dir):
                os.makedirs(destination_dir)
                #再次调用compareme函数标记
                createdir_bool=True

    #重新调用compareme函数，重新遍历新创建目录的内容
    if createdir_bool:
        destination_files = []
        source_files = []
        #调用compareme函数
        source_files = compareme(dir1,dir2)
        #获取源目录差异路径清单，对应替换成备份目录
        for item in source_files:
            destination_dir = re.sub(dir1,dir2,item)
            destination_files.append(destination_dir)

    print "update item:"
    #输出更新项列表清单
    print source_files
    #将源目录与备份目录文件清单拆分成元组
    copy_pair = zip(source_files,destination_files)
    for item in copy_pair:
        if os.path.isfile(item[0]):
            shutil.copyfile(item[0],item[1])

if __name__ == '__main__':
    main()
