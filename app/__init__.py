import flask
import os
import flask_sqlalchemy
import flask_migrate
from flask_uploads import configure_uploads, DATA, UploadSet




basedir = os.path.abspath(os.path.dirname(__file__))

app = flask.Flask(__name__)
app.config['SECRET_KEY'] = 'sdjhgsjghlakjf'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///'+os.path.join(basedir, "app.db")


app.config['UPLOADED_FILES_DEST'] = os.path.join(basedir, 'static/files')
files = UploadSet('files', DATA)
configure_uploads(app, files)

db = flask_sqlalchemy.SQLAlchemy(app)
migrate = flask_migrate.Migrate(app, db)

from app import routes, models