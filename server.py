import os
from flask import Flask
from flask_restful import Api
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
db = SQLAlchemy()


def create_app():
    """Construct the core application."""
    app = Flask(__name__, instance_relative_config=False)
    CORS(app)

    app.config.from_object("config.Config")
    api = Api(app=app)

    #import routes
    from modules.officer.route import create_officer_routes
    from modules.season.route import create_season_routes
    from modules.passenger.route import create_passenger_routes
    from modules.payment.route import create_payment_routes

    #call routes
    create_passenger_routes(api=api)
    create_season_routes(api=api)
    create_officer_routes(api=api)
    create_payment_routes(api=api)

    db.init_app(app)

    with app.app_context():
        db.create_all()  # Create database tables for our data models

        return app


if __name__ == "__main__":
    app = create_app()
    app.run(host="0.0.0.0", port=8080)
