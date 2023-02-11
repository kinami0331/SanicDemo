from sanic import Request, Blueprint, response

bp = Blueprint("dev", url_prefix="/dev")


@bp.route("hello", ["GET"])
async def hello(_req: Request):
    return response.text("hello, world!")
