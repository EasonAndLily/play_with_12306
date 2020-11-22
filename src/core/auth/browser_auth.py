from src.core.auth.auth import Auth


class BrowserAuth(Auth):
    def __init__(self, config):
        super().__init__(config)

    def login(self):
        print("user browser login")
