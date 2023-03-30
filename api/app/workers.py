from flask import (
    Blueprint, jsonify, g, redirect, request, url_for
)

bp = Blueprint('worker', __name__, url_prefix='/api/worker')

@bp.route('/')
def return_all():
    return jsonify({'all':'all'})

@bp.route('/<int:id>')
def return_one(id):
    return jsonify({'name':'Frank', 'team':'Lotos'})

@bp.route('/<int:id>/team')
def return_one_team(id):
    return jsonify({'team':'Lotos'})

@bp.route('/<int:id>/tasks')
def return_one_tasks(id):
    return jsonify({
        'Tasks received':'30',
        'Tasks in progress':'10',
        'Tasks finished':'20',
        'Coverage':'66.7%'
        })

