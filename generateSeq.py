# -*- coding=utf-8 -*-
# 生成随机字符串，大小写加数字

import random
import string

# 利用string，大小写字母加阿拉伯数字
forSelect = string.ascii_letters + string.digits
# 字符串效果同下，但不知效率差别如何
# forSelect = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ01234567890"


# random.choice
def generate_1(count, length):
    for x in range(count):
        Re = ""
        for y in range(length):
            Re += random.choice(forSelect)
        print(Re)


# random.sample
def generate_2(count, length):
    for i in range(count):
        print("".join(random.sample(forSelect, length)))


if __name__ == "__main__":
    generate_1(5, 8)
