from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
from flask_migrate import Migrate
from app.config import Config
from flask_cors import CORS

db = SQLAlchemy()
ma = Marshmallow()
migrate = Migrate()

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    db.init_app(app)
    ma.init_app(app)
    migrate.init_app(app,db)

    CORS(app)

    from app.routes.user_routes import user_bp
    app.register_blueprint(user_bp, url_prefix="/api/user")

    return app