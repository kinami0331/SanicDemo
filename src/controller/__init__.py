from sanic import Blueprint

from . import dev

bp = Blueprint.group(dev.bp)
