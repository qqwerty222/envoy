from flask import (
    Blueprint, jsonify, g, redirect, request, url_for
)

from app.db import db_data

bp = Blueprint('worker', __name__, url_prefix='/api/worker')


@bp.route('/')
def return_all_workers_data():
    all_workers_data = jsonify(db_data()['workers_'])
    return all_workers_data


@bp.route('/<int:id>')
def return_one_worker(id):
    some_worker_data = jsonify(db_data()['workers_'][f'{id}'])
    return some_worker_data


@bp.route('/<int:id>/<string:value>')
def return_one_worker_value(id, value):
    some_worker_values = jsonify(db_data()['workers_'][f'{id}'][f'{value}'])
    return some_worker_values


@bp.route('/<int:id>/tasks')
def return_one_worker_tasks(id):
    some_worker_tasks = jsonify({
        'tasks_received' : db_data()['workers_'][f'{id}'][f'tasks_received'],
        'tasks_in_progress' : db_data()['workers_'][f'{id}'][f'tasks_in_progress'],
        'tasks_finished' : db_data()['workers_'][f'{id}'][f'tasks_finished'],
        'tasks_coverage' : db_data()['workers_'][f'{id}'][f'tasks_coverage'],
    })
    return some_worker_tasks





