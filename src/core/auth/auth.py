from abc import ABC, abstractmethod


class Auth(ABC):
    def __init__(self, config):
        super().__init__()
        self.username = config.USERNAME
        self.password = config.PASSWORD

    @abstractmethod
    def login(self):
        pass
