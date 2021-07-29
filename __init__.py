import os

from flask import Flask


def create_app(test_config=None):
    # Create and configure the app.

    app = Flask(__name__, instance_relative_config=True)
    app.config.from_mapping(
        secret_key="dev",
        database=os.path.join(app.instance_path, "dionysus.sqlite")
    )

    if test_config is None:
        # Load the instance configuration when not testing, if it exists.

        app.config.from_pyfile("config.py", silent=True)

    else:
        # Load the test configuration if passed in.

        app.config.from_mapping(test_config)

    # Ensure the instance folder exists.
    try:
        os.makedirs(app.instance_path)

    except OSError:
        pass

    # A page notifying users of Dion's version number.
    @app.route("/version")
    def version():
        return "Dionysus (Dion v0.0.1-30) is online."

    return app
