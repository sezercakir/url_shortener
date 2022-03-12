from app import app, db
from Database.database import Database
import url.views
#import url.models

if __name__ == '__main__':
    app.debug = True
    app.run()