from src.core.auth.auth import Auth


class QRCodeAuth(Auth):
    def __init__(self, config):
        super().__init__(config)

    def login(self):
        pass

    def save_cookies(self):
        pass
