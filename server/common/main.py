from flask import Flask, jsonify
from flask_cors import CORS

from server.api import v1
from server.models.mariadb import db


def create_app(config_object=None):
    app = Flask(__name__)

    app.config.from_object(config_object)
    CORS(app, resources={r"/apis/*": {"origins": "*"}})

    app.register_blueprint(v1, url_prefix='/apis/v1')

    db.init_app(app)

    @app.route('/ping')
    def ping():
        return jsonify(dict(pong='pong'))

    return app
