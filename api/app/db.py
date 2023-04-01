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

def db_data():
    table_workers = db_execute("SELECT * FROM workers")

    data = {}

    # .../api/workers/
    workers_ = {}
    # { 
    #   1: {
    #       name: frank
    #       team: orange
    #       tasks_received: 30
    #       tasks_in_progress: 10
    #       tasks_finished: 20
    #       }
    #   }   
    # }

    for worker in table_workers:
        workers_[f"{worker['id']}"] = { 
            'name':                 f"{worker['name']}", 
            'team':                 f"{worker['team']}",
            'tasks_received':       int(f"{worker['tasks_received']}"),
            'tasks_in_progress':    int(f"{worker['tasks_in_progress']}"),
            'tasks_finished':       int(f"{worker['tasks_finished']}"),

            # count tasks coverage:  finished / ( received / 100 ) = coverage%
            'tasks_coverage':       f"{ worker['tasks_finished'] // (worker['tasks_received'] / 100)}%"
        }
    data['workers_'] = workers_

    return data






