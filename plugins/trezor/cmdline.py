from lib.plugins import hook
from plugins.trezor import TrezorPlugin
from plugins.hw_wallet import CmdLineHandler


class Plugin(TrezorPlugin):
    handler = CmdLineHandler()
    
    @hook
    def init_keystore(self, keystore):
        if not isinstance(keystore, self.keystore_class):
            return
        keystore.handler = self.handler
