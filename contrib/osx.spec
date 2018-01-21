# -*- mode: python -*-

from PyInstaller.utils.hooks import collect_data_files, collect_submodules

import sys
for i, x in enumerate(sys.argv):
    if x == '--name':
        VERSION = sys.argv[i+1]
        break
else:
    raise BaseException('no version')

import os
home = os.getcwd()
block_cipher=None

datas = [
(home+'lib/currencies.json', 'lib'),
(home+'lib/servers.json', 'lib'),
(home+'lib/checkpoints.json', 'lib'),
(home+'lib/servers_testnet.json', 'lib'),
(home+'lib/checkpoints_testnet.json', 'lib'),
(home+'lib/wordlist/english.txt', 'lib/wordlist'),
]

# We don't put these files in to actually include them in the script but to make the Analysis method scan them for imports
a = Analysis([home+'electrum-mac'],
             datas=datas,
             hiddenimports=[],
             hookspath=[])

# http://stackoverflow.com/questions/19055089/pyinstaller-onefile-warning-pyconfig-h-when-importing-scipy-or-scipy-signal
for d in a.datas:
    if 'pyconfig' in d[0]:
        a.datas.remove(d)
        break

pyz = PYZ(a.pure, a.zipped_data, cipher=block_cipher)

exe = EXE(pyz,
          a.scripts,
          a.binaries,
          a.datas,
          name='Electrum',
          debug=False,
          strip=False,
          upx=True,
          icon=home+'electrum.icns',
          console=False)

app = BUNDLE(exe,
             version = VERSION,
             name='Electrum.app',
             icon=home+'electrum.icns',
             bundle_identifier=None,
             info_plist = {
                 'NSHighResolutionCapable':'True'
             }
)
