#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Date    : 2016-09-05 11:11:52
# @Author  : K3vi (k3vi@atksec.com)
# @Link    : http://k3vi.xyz
# @Version : $Id$
'''
处理内容样式
用户名 密码
username、nickname、password、email、salt、mobile、qq、idcard、realname、address、ip、from
'''
import os
import sys
import re


def getFileName(l):
    '''
    description:get file's name from this DIR
    return:fileName_list
    '''
    fileName_list = os.listdir(l)
    return fileName_list


def dealData(l):
    errNum = 0
    f = open(l, 'rb')
    r = open('163mail3.txt', 'a+')
    lines = f.readlines()
    for line in lines:
        if errNum == 500:
            os.system("echo %s异常结束 >> err.txt" % l)
            break
        if line.strip() == "":
            continue
        try:
            name_mi = line.strip().decode('utf8')  # .replace(',', ',')
            name_m = re.subn(r' +|,|\t|\|','----', name_mi)
            code = name_m[0].split('----')
            if code[0].strip() == "":
                continue
            elif len(code) != 2:
                continue
            print(l,"=====",code)
            r.write('%s\t\t%s\t\t\t\t\t\t\t\t\t网易52G\n' %
                    (code[0], code[1]))
            errNum = 0
        except Exception as e:
            errNum += 1
            try:
                err_t.write(l+'\n')
                err_t.write(e+'\n')
            except Exception as e:
                print(e)
    f.close()
    r.close()


def deal(fileName, l):
    for name in fileName:
        _l = l + name
        dealData(_l)


if __name__ == '__main__':
    name = '163mail3'
    fileName = getFileName('./%s/'% name)
    deal(fileName, './%s/'% name)
