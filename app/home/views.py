from flask import request, render_template, redirect, url_for
from app import db, models
from .forms import CreateSnippet, CreateLanguage, CreateUser
from . import home
import logging

# logging setup
logging.basicConfig(filename='log/homelog.log',
                    filemode='a',
                    format='%(asctime)s,%(msecs)d %(name)s %(levelname)s %(message)s',
                    datefmt='%H:%M:%S',
                    level=logging.NOTSET)

logger = logging.getLogger(__name__)  # initialize logger
logger.handlers = []

@home.route('/')
@home.route('/index')
def index():
    return render_template('index.html')


@home.route('/create_snippet', methods=['GET', 'POST'])
def create_snippet():
    """

    """
    form = CreateSnippet()
    form.user.choices = [(row.id, row.name) for row in models.user.query.all()]
    form.language.choices = [(row.id, row.name) for row in models.language.query.all()]

    if request.method == 'GET':
        return render_template('create.html', form=form)

    if form.validate:
        user = form.user.data
        language = form.language.data
        tag = form.tag.data
        snippet = form.snippet.data
        # name = form.name.data
        # lastname = form.lastname.data
        # place = form.place_id.data
        # form.name.data = ''
        # form.lastname.data = ''
        # form.place_id.data = ''
        entity = models.snippet(user_id=user, language_id=language, tag=tag, snippet=snippet)
        db.session.add(entity)
        db.session.commit()

    data = models.snippet.query.all()

    logger.debug(f'test logging')

    return render_template('index.html', data=data)


@home.route('/create_user', methods=['GET', 'POST'])
def create_user():
    name = None
    form = CreateUser()

    if form.validate():
        name = form.user.data
        form.user.data = ''
        user = models.user(name=name)
        db.session.add(user)
        db.session.commit()

        return redirect(url_for('home.index'))

    return render_template('create_user.html', form=form)


@home.route('/create_language', methods=['GET', 'POST'])
def create_language():
    name = None
    form = CreateLanguage()

    if form.validate():
        name = form.language.data
        form.language.data = ''
        language = models.language(name=name)
        db.session.add(language)
        db.session.commit()

        return redirect(url_for('home.index'))

    return render_template('create_language.html', form=form)


@home.route('/read')
def read():
    """
    select all data in a join between entity and place
    :return:
    """
    # data = models.entity.query.all()
    data2 = models.snippet.query.join(models.language,
                                     models.snippet.language == models.language.id,
                                     isouter=True).\
        add_columns(models.entity.name,
                    models.entity.lastname,
                    models.place.place).all()

    return render_template('read.html', data=data2)


# @home.route('/delete', methods=['GET', 'POST'])
# def delete():
#     if request.method == 'GET':
#         # populate html page
#         data = models.entity.query.all()
#
#         data2 = models.entity.query.join(models.place,
#                                          models.entity.place_id == models.place.id,
#                                          isouter=True). \
#             add_columns(models.entity.id,
#                         models.entity.name,
#                         models.entity.lastname,
#                         models.place.place).all()
#
#         print('method is get')
#
#         return render_template('delete.html', data=data2)
#     else:
#         print('entity_id: {}'.format(request.form["entity_id"]))
#         # database actions (delete data)
#         if request.form["entity_id"]:
#             a = request.form.getlist("entity_id")
#
#             models.entity.query.filter(models.entity.id.in_(a)).delete(synchronize_session='fetch')
#             db.session.commit()
#
#         print('method is not get')
#
#     data = models.entity.query.all()
#
#     return render_template('read.html', data=data)


# @home.route('/update', methods=['GET', 'POST'])
# def update():
#     if request.method == 'GET':
#         # populate html page
#         # data from entity table
#         data = models.entity.query.all()
#         # data for populating the select boxes for 'places'
#         places = [(row.id, row.place) for row in models.place.query.all()]
#
#         return render_template('modify.html', data=data, places=places)
#
#     else:
#         # database actions
#         if request.form["entity_id"]:
#             ids = request.form.getlist("entity_id")
#             names = request.form.getlist("entity_name")
#             lastnames = request.form.getlist("entity_lastname")
#             places = request.form.getlist("entity_place")
#             print(places)
#
#             for cnt, id in enumerate(ids):
#                 entity = models.entity.query.filter_by(id=id).first()
#                 entity.name = names[cnt]
#                 entity.lastname = lastnames[cnt]
#                 entity.place_id = places[cnt]
#                 db.session.commit()
#
#     data = models.entity.query.all()
#
#     return render_template('read.html', data=data)





# @home.route('/users', methods=['GET', 'POST'])
# def users():
#     return render_template('read.html')

# @home.route('/aws', methods=['GET'])
# def aws():
#     return render_template('aws.html')