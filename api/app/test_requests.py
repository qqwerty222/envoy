import pymysql
from flask import jsonify

def get_db():
    db = pymysql.connect(
        host="172.17.0.2",
        user="api",
        password="api_pass",
        database="company",
        cursorclass=pymysql.cursors.DictCursor
    )
    return db

def db_execute(query):
    db = get_db().cursor()
    db.execute(query)

    return db.fetchall()
  
print(db_execute("SELECT * FROM workers"))
