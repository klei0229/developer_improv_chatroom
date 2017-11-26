from app import db
from .models import db, User

# create the database and the db table
db.create_all()
2
# commit the changes
db.session.commit()