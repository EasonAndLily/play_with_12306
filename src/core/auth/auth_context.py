from src.core.auth.api_auth import APIAuth
from src.core.auth.auth import Auth
from src.core.auth.browser_auth import BrowserAuth
from src.core.auth.qr_code_auth import QRCodeAuth


class AuthContext(object):
    def __init__(self, config):
        auth_list = {
            0: APIAuth(config),
            1: BrowserAuth(config),
            2: QRCodeAuth(config)
        }
        self.__auth = auth_list.get(config.LOGIN_METHOD, Auth(config))

    def auth(self):
        self.__auth.login()
