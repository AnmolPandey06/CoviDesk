import os
from app import create_app, db
from app.models import NGOs, AvailableBeds
from flask_migrate import Migrate

app = create_app(os.getenv('FLASK_CONFIG'))
migrate = Migrate(app,db)

@app.shell_context_processor
def make_shell_context():
    return dict(db=db,NGOs=NGOs,
                AvailableBeds=AvailableBeds)
