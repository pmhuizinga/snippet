from flask import request, render_template, redirect, url_for
from app import db, models
from .forms import CreateForm

from . import home

('/')
@home.route('/')
@home.route('/index')
def index():
    return render_template('index.html')


@home.route('/read')
def read():
    data = models.entity.query.all()

    return render_template('read.html', data=data)

@home.route('/delete')
def delete():
    data = models.entity.query.all()

    return render_template('delete.html', data=data)


@home.route('/delete_submit', methods=['GET', 'POST'])
def delete_submit():
    if request.method == 'POST':
        if request.form["entity_id"]:
            a = request.form.getlist("entity_id")
            models.entity.query.filter(models.entity.id.in_(a)).delete(synchronize_session='fetch')
            db.session.commit()

    data = models.entity.query.all()

    return render_template('read.html', data=data)


@home.route('/update')
def update():
    data = models.entity.query.all()

    return render_template('modify.html', data=data)


@home.route('/update_submit', methods=['GET', 'POST'])
def update_submit():

    if request.method == 'POST':

        if request.form["entity_id"]:
            ids = request.form.getlist("entity_id")
            names = request.form.getlist("entity_name")
            lastnames = request.form.getlist("entity_lastname")

            for cnt, id in enumerate(ids):
                entity = models.entity.query.filter_by(id = id).first()
                entity.name = names[cnt]
                entity.lastname = lastnames[cnt]
                db.session.commit()

    data = models.entity.query.all()

    return render_template('read.html', data=data)


@home.route('/create', methods=['GET', 'POST'])
def create():
    name = None
    form = CreateForm()

    if form.validate():
        name = form.name.data
        lastname = form.lastname.data
        form.name.data = ''
        form.lastname.data = ''
        entity = models.entity(name=name, lastname=lastname)
        db.session.add(entity)
        db.session.commit()

        return redirect(url_for('home.read'))

    return render_template('create.html', form=form)