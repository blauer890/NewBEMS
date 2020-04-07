from flask import Flask, render_template

def create_app():
    app = Flask(__name__)
    app.config.from_pyfile('settings.py')
    from . import auth
    app.register_blueprint(auth.bp)

    @app.route('/')
    def index():
        return render_template("index.html")

    return app

