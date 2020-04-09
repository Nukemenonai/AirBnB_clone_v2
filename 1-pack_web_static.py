#!/usr/bin/python3

"""
fabric script to generate a tgz
"""

from fabric.api import *
from datetime import datetime


def do_pack():
    """
    this script packs the contents of the web_static folder
    to tgz format
    """
    try:
        current_time = datetime.now().strftime("%Y%m%d%H%M%S")
        path = 'versions/web_static_{:s}.tgz'.format(current_time)
        local('mkdir -p ./versions')
        local('tar -cvzf {} web_static'.format(path))
        bytec = local('wc -c {}'.format(path), capture=True)
        bytec = bytec.split(' ')[0]
        print("web_static packed: {} -> {}Bytes".format(path, bytec))
        return path
    except:
        return None
