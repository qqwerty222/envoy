from flask import (
    Blueprint, jsonify, g, redirect, request, url_for
)

from app.db import get_db, db_execute

bp = Blueprint('common', __name__, url_prefix='/api/common')

@bp.route('/')
def return_all():
    return jsonify({
            'Workers':{
                'Frank':{ 'id':1, 'Coverage':"66.6%"},
            },
            'Teams':{
                'Lotus': { 'Size':2, 'Coverage':"70%"},
            },
            'Tasks':{
                'received':300,
                'in progress':50,
                'finished':250,
                'coverage':"70%"
            },
    })

@bp.route('/workers')
def return_workers():
    return jsonify(db_execute("SELECT id, name, team FROM workers"))

@bp.route('/teams')
def return_teams():
    return jsonify(db_execute("SELECT name FROM teams"))
        #'Lotus': { 'Size':2, 'Coverage':"70%"},

@bp.route('/tasks')
def return_tasks():
    # return jsonify(
    #     db_execute("SELECT SUM(tasks_received) FROM workers")
    # )
    return jsonify(
        db_execute("SELECT SUM(tasks_received) FROM workers"),
        db_execute("SELECT SUM(tasks_in_progress) FROM workers"),
        db_execute("SELECT SUM(tasks_finished) FROM workers"),
        )

        #   'Tasks':{
        #         'received':300,
        #         'in progress':50,
        #         'finished':250,
        #         'coverage':"70%"
        #     },  




