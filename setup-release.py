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
        'electrum_gui',
        'electrum_gui.qt',
        'electrum_plugins',
        'electrum_plugins.audio_modem',
        'electrum_plugins.cosigner_pool',
        'electrum_plugins.email_requests',
        'electrum_plugins.greenaddress_instant',
        'electrum_plugins.hw_wallet',
        'electrum_plugins.keepkey',
        'electrum_plugins.labels',
        'electrum_plugins.ledger',
        'electrum_plugins.trezor',
        'electrum_plugins.digitalbitbox',
        'electrum_plugins.trustedcoin',
        'electrum_plugins.virtualkeyboard'
    ],
    package_dir={
        'electrum': 'lib',
        'gui': 'gui',
        'lib.plugins': 'plugins'
    },
    options=dict(py2app=dict(argv_emulation=False,
                             includes=['sip'],
                             packages=['lib', 'gui', 'plugins', 'packages'],
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
