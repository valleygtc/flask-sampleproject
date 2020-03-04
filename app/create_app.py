from flask import Flask

from .config import Config


def create_app():
    app = Flask(__name__)
    # config
    app.config.from_object(Config)
    Config.init_app(app)

    # bp
    from .views import bp_main
    app.register_blueprint(bp_main)

    # db
    from .models import db
    db.init_app(app)

    # CLI
    from .cli import create_table, hello
    app.cli.add_command(create_table)
    app.cli.add_command(hello)

    from .models import Student
    def make_shell_context():
        return dict(db=db, Student=Student)

    app.shell_context_processor(make_shell_context)

    return app
