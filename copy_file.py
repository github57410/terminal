# -*- coding: utf-8 -*-
"""File Name：     demo1
   date：          2019/1/11"""
import os
from multiprocessing import Pool
from multiprocessing import Manager
import time
__author__ = 'GaoShuai'

def copy_file(name, old_folder, new_folder, queue):
    file_data = None
    try:
        file = open(old_folder+"/"+name, "rb")
        file_data = file.read()
        file.close()
    except Exception as e:
        file.close()
    if file_data is not None:
        with open(new_folder+"/"+name, "wb") as f:
            f.write(file_data)
    queue.put(name)
    time.sleep(5)

def main():
    # 在进程池中创建队列 需要导入Manager()
    queue = Manager().Queue()
    # 提示用户输入要拷贝的文件夹
    old_folder = input("请输入要拷贝的文件夹")
    # 创建一个新的文件夹
    # "../"
    new_folder = old_folder + '[新]'
    # 获取要拷贝的文件夹中所有的文件名字
    try:
        os.mkdir(new_folder)
    except Exception as e:
        pass
    file_names = os.listdir(old_folder)
    print(file_names)

    po = Pool(3)
    for name in file_names:
        po.apply_async(copy_file, args=(name, old_folder, new_folder, queue))

    po.close()
    # 获取文件夹所有文件数量

    file_num = len(file_names)
    copy_ok_num = 0
    while True:
        file_name = queue.get()
        copy_ok_num += 1
        # 置顶   \t 制表
        print("\r%.2f%%" % (copy_ok_num *100/ file_num), end="")
        if copy_ok_num == file_num:
            break
    # po.join()

if __name__ == '__main__':
    main()

