#!/user/bin/python3
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
        return path
    except:
        return None
