from flask import Blueprint, render_template, request, redirect, url_for
from project_app.utils.main_func import get_lotto
from project_app import db
from project_app.models.model import Users
import datetime

main_bp = Blueprint('main', __name__)

@main_bp.route('/', methods=['GET'])
def index():
    return render_template('main.html'), 200

@main_bp.route('/predict', methods=['POST', 'GET'])
def predict():

    data = get_lotto(1)
    return render_template('predict.html',  data=data)


@main_bp.route('/tolist', methods=['GET','POST'])
def tolist():
    if request.method == 'POST':
        
        task_content = request.form['content']
        now = datetime.datetime.today().strftime("%Y%m%d") 


        if not task_content:
            tasks = Users.query.order_by(Users.date).all()
            return render_template('alert.html')
        else:
            new_task = Users(date=now, num=task_content)

            db.session.add(new_task)
            db.session.commit()
            tasks = Users.query.order_by(Users.date).all()
            return render_template('tolist.html', tasks=tasks)
    else:

        tasks = Users.query.order_by(Users.date).all()
        return render_template('tolist.html', tasks=tasks)

@main_bp.route('/delete/<int:id>')
def delete(id):
    task_to_delete = Users.query.get_or_404(id)


    db.session.delete(task_to_delete)
    db.session.commit()
    return redirect('/tolist')


@main_bp.route('/update/<int:id>', methods=['GET', 'POST'])
def update(id):
    task = Users.query.get_or_404(id)

    if request.method == 'POST':
        task.num = request.form['content']


        db.session.commit()
        return redirect('/tolist')


    else:
        return render_template('update.html', task=task)
