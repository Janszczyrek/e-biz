from flask import Flask
from flask_cors import CORS

from .config import Config
from .extensions import oauth
from .database import init_app
from .routes.auth import auth_bp
from .routes.products import products_bp

def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(config_class)

    CORS(app, supports_credentials=True)
    oauth.init_app(app)
    oauth.register(
        name='google',
        client_id=app.config['GOOGLE_CLIENT_ID'],
        client_secret=app.config['GOOGLE_CLIENT_SECRET'],
        server_metadata_url='https://accounts.google.com/.well-known/openid-configuration',
        client_kwargs={'scope': 'openid email profile'},
    )

    init_app(app)

    app.register_blueprint(auth_bp) 
    app.register_blueprint(products_bp)

    @app.route('/')
    def index():
        return "Backend is running!"

    return app


if __name__ == '__main__':
    app = create_app()
    app.run(debug=True, port=5000)