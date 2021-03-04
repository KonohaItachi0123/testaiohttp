import os

import aiohttp_cors
import aiopg.sa
from aiohttp import web

from hackernews.routes import init_routes
from hackernews.utils import get_config


def init_config(app: web.Application, argv=None) -> None:

    db_info = os.environ.get("DATABASE_URL", None)
    if db_info:
        db_conf = {}
        password, host = db_info[2].split("@")
        port, database = db_info[-1].split("/")
        user = db_info[1][2:]

        db_conf["user"] = user
        db_conf["host"] = host
        db_conf["port"] = port
        db_conf["database"] = database
        db_conf["password"] = password

        app["config"] = db_conf

    else:
        app["config"] = get_config(argv)


async def init_database(app: web.Application) -> None:
    """
    This is signal for success creating connection with database
    """
    config = app["config"]["postgres"]

    engine = await aiopg.sa.create_engine(**config)
    app["db"] = engine


async def close_database(app: web.Application) -> None:
    """
    This is signal for success closing connection with database before shutdown
    """
    app["db"].close()
    await app["db"].wait_closed()


def init_app(argv=None) -> web.Application:
    app = web.Application()
    cors = aiohttp_cors.setup(app)

    init_config(app, argv)
    init_routes(app, cors)
    app.on_startup.extend([init_database])
    app.on_cleanup.extend([close_database])
    return app


app = init_app()
