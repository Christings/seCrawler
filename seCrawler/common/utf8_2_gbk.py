#! /usr/bin/env python
# -*- coding: utf-8 -*-

import codecs

# 将utf-8格式转换为gbk格式
def readFile(filePath, encoding='utf-8'):
    with codecs.open(filePath, 'r', encoding) as f:
        return f.read()


def writeFile(filePath, u, encoding='gbk'):
    with codecs.open(filePath, 'wb') as f:
        f.write(u.encode(encoding, errors='ignore'))


def utf8_2_gbk(src, dst):
    content = readFile(src, encoding='utf-8')
    writeFile(dst, content, encoding='gbk18030')
