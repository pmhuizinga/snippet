# from app import create_app, db
# from app.models import tbl_entity
import os

from app import create_app

config_name = os.getenv("FLASK_CONFIG")
app = create_app(config_name)

if __name__ == 'main':
    app.run()