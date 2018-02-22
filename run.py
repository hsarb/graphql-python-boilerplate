#!/usr/bin/env python3

from boilerplate import app
from boilerplate.database import db_session, init_db


@app.teardown_appcontext
def shutdown_session(exception=None):
    db_session.remove()


if __name__ == '__main__':
    init_db()
    app.run(
        host=app.config['HOST'],
        port=app.config['PORT']
    )
