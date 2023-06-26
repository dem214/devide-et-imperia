from flask import Flask

from devide_et_imperia.views import views_bp


def create_app():
    app = Flask(__name__)
    app.register_blueprint(views_bp)

    return app

if __name__ == '__main__':
    app = create_app()
    app.run()

