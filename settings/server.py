from fastapi import FastAPI


class Server:
    app = FastAPI()

    @classmethod
    def get_app(cls):
        return cls.app

ServerService = Server()
