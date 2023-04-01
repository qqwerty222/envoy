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

    #.../api/teams
    teams_ = {}
    # {
    #   lemon: {
    #       size: 3
    #       workers: [
    #           "frank",
    #           "john",
    #           "bill",
    #       ]
    #       tasks: {
    #           received: 100
    #           in_progress: 30
    #           finished: 70
    #           coverage: 70%
    #       }
    # }

    teams_list = []

    for worker in table_workers:

        if worker['team'] not in teams_list: 
            teams_list.append(f"{worker['team']}")

            # create key in teams_ with team name, assign dict with key "workers" to store list, and put current worker in this list
            teams_[f"{worker['team']}"] = { 'workers': [f"{worker['name']}"] }
            teams_[f"{worker['team']}"] = { 'size' : "1"}

        else:
            # if team already exist in teams_, add worker name to it's workers
            teams_[f"{worker['team']}"]['workers'].append(f"{worker['name']}")
            # teams_[f"{worker['team']}"]['size'] += 1
        
            
    
    # for team in team_list:
    #     for worker in table_workers:
    #         teams_[f"{worker['team']}"] = {}

    return teams_

print(db_data())