import os

from flask_sqlalchemy import SQLAlchemy


db = SQLAlchemy()


def init_database(app):

    database_dir = os.path.join(
        os.path.dirname(__file__),
        "..",
        "Database"
    )

    os.makedirs(
        database_dir,
        exist_ok=True
    )

    db.init_app(app)

    with app.app_context():
        db.create_all()

    print(
        "[DATABASE] Database initialized successfully"
    )