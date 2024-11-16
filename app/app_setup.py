from flask import Flask

def create_app():
    """Flask application factory."""
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'your-secret-key'

    # Register Blueprints or Routes
    from .routes import main
    app.register_blueprint(main)

    return app
