from flask_sqlalchemy import SQLAlchemy

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///development.db'
db = SQLAlchemy(app)
""" Another way to run the app"""

from src import create_app

app = create_app()

if __name__ == "__main__":
    app.run()
