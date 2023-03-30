from flask import (
    Blueprint, jsonify, g, redirect, request, url_for
)

bp = Blueprint('teams', __name__, url_prefix='/api/team')


@bp.route('/')
def return_all():
    return jsonify({'All':'all'})

@bp.route('/<string:name>')
def return_one(name):
    return jsonify({
            'Name':'Lotus',
            'Size':2,
            'Tasks':{
                'received':100,
                'in progress':30,
                'finished':70,
                'coverage':"70%"
            },
            'Team members':{
                '1':'Frank',
                '2':'John'
            }
    })

@bp.route('/<string:name>/tasks')
def return_tasks(name):
    return jsonify({
            'Tasks':{
                'received':100,
                'in progress':30,
                'finished':70,
                'coverage':"70%"
            },
    })

@bp.route('/<string:name>/members')
def return_members(name):
    return jsonify({
            'Size':2,
            'Team members':{
                '1':'Frank',
                '2':'John'
            }
    })