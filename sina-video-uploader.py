#!/usr/bin/env python3

# The original author of this program, sina-video-uploader, is StarBrilliant.
# This file is released under General Public License version 3.
# You should have received a copy of General Public License text alongside with
# this program. If not, you can obtain it at http://gnu.org/copyleft/gpl.html .
# This program comes with no warranty, the author will not be resopnsible for
# any damage or problems caused by this program.

import argparse
import logging
import uuid
import os
import sys

if sys.version_info < (3,):
    raise RuntimeError('至少需要 Python 3.0 版本')

try:
    import requests
except ImportError:
    raise ImportError('请从 https://pypi.python.org/pypi/requests/ 安装 requests 模块')

def main():
    def InputFailure(value=None):
        if value:
            logging.warning('未指定输入，使用“%s”。' % value)
            return value
        else:
            logging.error('未指定输入，退出。')
            sys.exit(1)

    if len(sys.argv) == 1:
        sys.argv.append('--help')
    parser = argparse.ArgumentParser()
    parser.add_argument('-t', '--title', metavar='标题', help='视频标题')
    parser.add_argument('-d', '--desc', metavar='简介', help='视频简介')
    parser.add_argument('-c', '--cookie', metavar='Cookie文件', default='cookies.txt', help='指向Cookie文件的文件名')
    parser.add_argument('file', metavar='文件', help='视频文件名')
    args = parser.parse_args()
    filename = args.file or input('输入视频文件名：') or InputFailure()
    title = args.title or input('输入视频标题：') or InputFailure(os.path.splitext(os.path.basename(filename))[0])
    desc = args.desc or input('输入视频简介：') or InputFailure(title)
    DoUpload(filename, title, desc)

def DoUpload(filename, title, desc):
    pass

if __name__ == '__main__':
    main()
