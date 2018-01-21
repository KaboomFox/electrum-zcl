from lib.plugins import hook
from plugins.digitalbitbox.digitalbitbox import DigitalBitboxPlugin
from plugins.hw_wallet import CmdLineHandler


class Plugin(DigitalBitboxPlugin):
    handler = CmdLineHandler()
    @hook
    def init_keystore(self, keystore):
        if not isinstance(keystore, self.keystore_class):
            return
        keystore.handler = self.handler
