from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate


db = SQLAlchemy()
migrate = Migrate()


SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://{username}:{pw}@{url}/{database}'.format(
    database = 'MYDATABASE',
    username = 'MYUSERNAME',
    pw = 'MYPASSWORD',
    url = 'MYURL',
    db='project_app')

def create_app():
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = SQLALCHEMY_DATABASE_URI
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    # if config is not None:
    #     app.config.update(config)

    db.init_app(app)
    migrate.init_app(app, db)

    from project_app.routes.main_route import main_bp
    app.register_blueprint(main_bp)

    return app

if __name__ == "__main__":
    app = create_app()
    app.run(debug=True)
