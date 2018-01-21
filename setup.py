#!/usr/bin/env python3

# python setup.py sdist --format=zip,gztar

from setuptools import setup, find_packages
import os
import sys
import platform
import imp
import argparse

version = imp.load_source('version', 'lib/version.py')

if sys.version_info[:3] < (3, 4, 0):
    sys.exit("Error: Electrum requires Python version >= 3.4.0...")

data_files = []

if platform.system() in ['Linux', 'FreeBSD', 'DragonFly']:
    parser = argparse.ArgumentParser()
    parser.add_argument('--root=', dest='root_path', metavar='dir', default='/')
    opts, _ = parser.parse_known_args(sys.argv[1:])
    usr_share = os.path.join(sys.prefix, "share")
    if not os.access(opts.root_path + usr_share, os.W_OK) and \
       not os.access(opts.root_path, os.W_OK):
        if 'XDG_DATA_HOME' in os.environ.keys():
            usr_share = os.environ['XDG_DATA_HOME']
        else:
            usr_share = os.path.expanduser('~/.local/share')
    data_files += [
        (os.path.join(usr_share, 'applications/'), ['electrum.desktop']),
        (os.path.join(usr_share, 'pixmaps/'), ['icons/electrum.png'])
    ]

setup(
    name="Electrum-ZCL",
    version=version.ELECTRUM_VERSION,
    install_requires=[
        'pyaes>=0.1a1',
        'ecdsa>=0.9',
        'pbkdf2',
        'requests',
        'qrcode',
        'protobuf',
        'dnspython',
        'jsonrpclib-pelix',
        'pyblake2',
        'PySocks>=1.6.6',
        'PyQt5'
    ],
    packages= find_packages(),
    package_data={
        'electrum': [
            'servers.json',
            'servers_testnet.json',
            'currencies.json',
            'checkpoints.json',
            'checkpoints_testnet.json',
            'www/index.html',
            'wordlist/*.txt',
            'locale/*/LC_MESSAGES/electrum.mo',
        ]
    },
    scripts=['electrum'],
    data_files=data_files,
    description="Lightweight Zclassic Wallet",
    author="BTCP Community",
    author_email="csulmone@gmail.com",
    license="MIT Licence",
    url="https://zclassic.org",
    long_description="""Lightweight Zclassic Wallet"""
)
