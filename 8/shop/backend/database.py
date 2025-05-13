import sqlite3
from flask import g, current_app


def get_db():
    db = getattr(g, '_database', None)
    if db is None:
        db = g._database = sqlite3.connect(current_app.config['DATABASE_URL'])
    return db

def close_db(exception=None):
    db = getattr(g, '_database', None)
    if db is not None:
        db.close()

def init_db():
    with current_app.app_context():
        db = get_db()
        with current_app.open_resource('schema.sql', mode='r') as f:
            db.cursor().executescript(f.read())
        db.commit()
        
def init_app(app):
    app.teardown_appcontext(close_db)
    with app.app_context():
        cur = get_db().cursor()
        try:
            cur.execute("SELECT 1 FROM users LIMIT 1")
        except sqlite3.OperationalError:
            current_app.logger.info("Users table not found, initializing database.")
            init_db()