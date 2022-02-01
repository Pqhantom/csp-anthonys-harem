from flask import Blueprint, render_template, request

create_task_bp = Blueprint('create_task', __name__,
                       url_prefix='/create-task',
                       template_folder='templates',
                       static_folder='static', static_url_path='static')

@create_task_bp.route("/")
def index():
    return render_template("create_task_home.html")

@create_task_bp.route("/anthony")
def anthony():
    return render_template("anthony.html")