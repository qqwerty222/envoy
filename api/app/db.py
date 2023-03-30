import pymysql

from flask import g, current_app

def get_db():
    if 'db' not in g:
        g.db = pymysql.connect(
            host="172.17.0.2",
            user="api",
            password="api_pass",
            database="company",
            cursorclass=pymysql.cursors.DictCursor
        )
    return g.db

def db_execute(query):
    db = get_db().cursor()
    db.execute(query)

    return db.fetchall()
    
def close_db(e=None):
    db = g.pop('db', None)

    if db is not None:
        db.close()



