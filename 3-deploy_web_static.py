#!/usr/bin/python3
"""
fabric script to generate a tgz
"""
from fabric.api import *
from datetime import datetime
from os import path

env.hosts = ['35.231.149.204', '34.228.66.193']


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


def do_deploy(archive_path):
    """
    distributes an archive to my servers
    """

    if not path.exists(archive_path):
        return False

    filename = path.splitext(archive_path)[0].split('/')[-1]
    file_arch = filename + '.tgz'

    try:
        print("Executing task 'deploy'")
        put(archive_path, '/tmp/')
        run('mkdir -p /data/web_static/releases/{:s}'.format(filename))
        run('tar -xzf /tmp/{:s} -C /data/web_static/releases/{:s}'.format(
            file_arch, filename))
        run('rm /tmp/{:s}'.format(file_arch))
        run('mv /data/web_static/releases/{:s}/web_static/*'
            ' /data/web_static/releases/{:s}'.
            format(filename, filename))
        run('rm -rf /data/web_static/releases/{:s}/web_static'
            .format(filename))
        run('rm -rf /data/web_static/current')
        run('ln -s /data/web_static/releases/{:s}/ /data/web_static/current'
            .format(filename))
        print("New version deployed!")
        return True
    except:
        return False


def deploy():
    """
    creates and distributes an archive to my web servers
    """
    archive_path = do_pack()

    if not archive_path:
        return False

    return do_deploy(archive_path)
