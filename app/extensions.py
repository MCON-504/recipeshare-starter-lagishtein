from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

# Extensions are created here and initialized in the app factory.
db = SQLAlchemy()
migrate = Migrate()
