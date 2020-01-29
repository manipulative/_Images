# -*- coding:utf-8 -*-
import os
import sys

base_dir = sys.argv[1] #the dictionay of .md, read from shell
base_len = len(base_dir)
img_base_old = "/Users/siyuan/OneDrive/function/_Images/"
img_base_new = "https://raw.githubusercontent.com/manipulative/_Images/master/"


def replace_str(file_path, old_str, new_str):
    """
    replace strings in file
    """
    try:
        f = open(file_path, 'r+')
        all_lines = f.readlines()
        f.seek(0)
        f.truncate()
        for line in all_lines:
            line = line.replace(old_str, new_str)
            f.write(line)
        f.close()
    except Exception as e:
        print(e)


def recursive_replace(working_dir, old_str, new_str):
    os.chdir(working_dir)
    cwd = os.getcwd()
    for d in os.listdir(cwd):
        path = os.path.join(cwd, d)
        if os.path.isfile(path):
            if not path.endswith(".md"):
                # print(path + " is not md file, continue")
                continue
            print("file: " + path)
            print("replace: " + old_str + " -> " + new_str)
            replace_str(path, old_str, new_str)
        elif os.path.isdir(path):
            if path.endswith(".git") or path.endswith("Images"):
                print("repo: " + path + ", skip...")
                continue
            suffix = path[base_len:]
            print("dir: " + path + ", folder name: " + path[len(working_dir):])
            next_old = img_base_old + suffix
            next_new = img_base_new + suffix.replace(" ", "%20")
            # print("going to replace: " + next_old + " -> " + next_new)
            new_path = path + os.sep
            recursive_replace(new_path, next_old, next_new)


if __name__ == '__main__':
    recursive_replace(base_dir, img_base_old, img_base_new)


# def find_files(path):
#     """
#     Find all files under the given path
#     :param path:
#     :return:
#     """
#     file_list = []
#     for root, dirs, files in os.walk(path):
#         for fileObj in files:
#             file_list.append(os.path.join(root, fileObj))
#     return file_list


# if __name__ == "__main__":
#     # if len(sys.argv) < 4:
#     #     print("need 3 params")
#     #     sys.exit(1)
#     # file_name = sys.argv[1]
#     # src_str = sys.argv[2]
#     # dst_str = sys.argv[3]
#
#     base_dir = "/Users/hlyin/Documents/Foundations/"
#     old_str = "/Users/hlyin/Documents/Foundations/_Images/Java Concurrency/"
#     new_str = "https://github.com/louiehuang/Foundations/blob/master/_Images/Java%20Concurrency/"
#
#     file_list = find_files(base_dir)
#     for file_path in file_list:
#         print(file_path)
#         # replace_str(file_path, old_str, new_str)
