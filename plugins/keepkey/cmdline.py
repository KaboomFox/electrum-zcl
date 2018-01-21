from lib.plugins import hook
from plugins.keepkey.keepkey import KeepKeyPlugin
from plugins.hw_wallet import CmdLineHandler

class Plugin(KeepKeyPlugin):
    handler = CmdLineHandler()
    @hook
    def init_keystore(self, keystore):
        if not isinstance(keystore, self.keystore_class):
            return
        keystore.handler = self.handler
