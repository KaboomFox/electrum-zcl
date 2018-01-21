"""
py2app build script for Electrum Bitcoin Private

Usage (Mac OS X):
     python setup.py py2app
"""

from setuptools import setup, find_packages
import os
import re
import shutil
import sys

from lib.util import print_error
from lib.version import ELECTRUM_VERSION as version


name = "Electrum"
mainscript = 'electrum-mac'

from plistlib import Plist
plist = Plist.fromFile('Info.plist')
plist.update(dict(CFBundleIconFile='electrum.icns'))

shutil.copy(mainscript, mainscript + '.py')
mainscript += '.py'
extra_options = dict(
    setup_requires=['py2app'],
    app=[mainscript],
    packages=[
        'electrum',
        'gui',
        'gui.qt',
        'lib.plugins',
        'lib.plugins.audio_modem',
        'lib.plugins.cosigner_pool',
        'lib.plugins.email_requests',
        'lib.plugins.greenaddress_instant',
        'lib.plugins.hw_wallet',
        'lib.plugins.keepkey',
        'lib.plugins.labels',
        'lib.plugins.ledger',
        'lib.plugins.trezor',
        'lib.plugins.digitalbitbox',
        'lib.plugins.trustedcoin',
        'lib.plugins.virtualkeyboard',
    ],
    package_dir={
        'electrum': 'lib',
        'gui': 'gui',
        'lib.plugins': 'plugins'
    },
    options=dict(py2app=dict(argv_emulation=False,
                             includes=['sip'],
                             packages=['lib', 'gui.qt', 'plugins', ],
                             iconfile='electrum.icns',
                             plist=plist,
                             resources=["icons"])),
)

setup(
    name=name,
    version=version,
    **extra_options
)
from distutils import dir_util

# Remove the copied py file
# os.remove(mainscript)
