from flask import request, render_template, redirect, url_for
from app import db, models
from .forms import CreateForm, CreatePlace
from . import home
import logging

# logging setup
logging.basicConfig(filename='log/homelog.log',
                    filemode='a',
                    format='%(asctime)s,%(msecs)d %(name)s %(levelname)s %(message)s',
                    datefmt='%H:%M:%S',
                    level=logging.DEBUG)

logger = logging.getLogger(__name__)  # initialize logger
logger.handlers = []

@home.route('/')
@home.route('/index')
def index():
    return render_template('index.html')


@home.route('/create', methods=['GET', 'POST'])
def create():
    """
    handle new input
    - first select all 'place' options
    - if request == get then send options to html form
    - else (request == post) insert new data in database
    """
    form = CreateForm()
    form.place_id.choices = [(row.id, row.place) for row in models.place.query.all()]

    if request.method == 'GET':
        return render_template('create.html', form=form)

    if form.validate:
        name = form.name.data
        lastname = form.lastname.data
        place = form.place_id.data
        form.name.data = ''
        form.lastname.data = ''
        form.place_id.data = ''
        entity = models.entity(name=name, lastname=lastname, place_id=place)
        db.session.add(entity)
        db.session.commit()

    data = models.entity.query.all()

    logger.debug(f'test logging')

    return render_template('read.html', data=data)


@home.route('/read')
def read():
    """
    select all data in a join between entity and place
    :return:
    """
    # data = models.entity.query.all()
    data2 = models.entity.query.join(models.place,
                                     models.entity.place_id == models.place.id,
                                     isouter=True).\
        add_columns(models.entity.name,
                    models.entity.lastname,
                    models.place.place).all()
    return render_template('read.html', data=data2)


@home.route('/delete', methods=['GET', 'POST'])
def delete():
    if request.method == 'GET':
        # populate html page
        data = models.entity.query.all()
        return render_template('delete.html', data=data)
    else:
        # database actions (delete data)
        if request.form["entity_id"]:
            a = request.form.getlist("entity_id")
            models.entity.query.filter(models.entity.id.in_(a)).delete(synchronize_session='fetch')
            db.session.commit()

    data = models.entity.query.all()

    return render_template('read.html', data=data)


@home.route('/update', methods=['GET', 'POST'])
def update():
    if request.method == 'GET':
        # populate html page
        data = models.entity.query.all()
        places = [(row.id, row.place) for row in models.place.query.all()]
        return render_template('modify.html', data=data, places=places)

    else:
        # database actions
        if request.form["entity_id"]:
            ids = request.form.getlist("entity_id")
            names = request.form.getlist("entity_name")
            lastnames = request.form.getlist("entity_lastname")
            places = request.form.getlist("entity_place")
            print(places)

            for cnt, id in enumerate(ids):
                entity = models.entity.query.filter_by(id=id).first()
                entity.name = names[cnt]
                entity.lastname = lastnames[cnt]
                entity.place_id = places[cnt]
                db.session.commit()

    data = models.entity.query.all()

    return render_template('read.html', data=data)


@home.route('/create_place', methods=['GET', 'POST'])
def create_place():
    name = None
    form = CreatePlace()

    if form.validate():
        place = form.place.data
        form.place.data = ''
        place = models.place(place=place)
        db.session.add(place)
        db.session.commit()

        return redirect(url_for('home.read'))

    return render_template('create_place.html', form=form)
