from flask import Flask
from flask_cors import CORS

from .config import Config
from .routes.chat import chat_bp
from .llm_provider import get_llm_client

def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(config_class)

    CORS(app, supports_credentials=True)


    app.register_blueprint(chat_bp) 

    @app.route('/')
    def index():
        return "Backend is running!"

    return app


if __name__ == '__main__':
    app = create_app()
    app.run(debug=True, port=5000)