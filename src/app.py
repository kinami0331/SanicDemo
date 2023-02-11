from sanic import Sanic

from . import controller

app = Sanic('demo')

app.blueprint(controller.bp)


def start() -> None:
    app.run()
