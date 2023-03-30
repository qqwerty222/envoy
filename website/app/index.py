from flask import (
    Blueprint, redirect, render_template, request, url_for
)
from werkzeug.exceptions import abort

bp = Blueprint('index', __name__)

@bp.route('/')
def index():
    return render_template('index.html')
    