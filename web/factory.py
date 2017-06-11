import os

import datetime
import random

from flask import Flask
from flask_cors import CORS
from flask_security import Security, utils

from app_utils import utilities
from config import CONFIG
from create_scripts import stringgenerator, boolgenerator
from models import Employee, db, user_datastore, Servicelocation, Role


def create_app():
    """Configure the app w.r.t Flask-security, databases, loggers."""
    app = Flask(__name__)
    config_name = os.getenv('FLASK_CONFIGURATION', 'default')
    app.config.from_object(CONFIG[config_name])
    app.secret_key = app.config['SECRET_KEY']
    utilities.setup_logger()
    db.init_app(app)
    Security(app, user_datastore)
    CORS(app, headers=['Content-Type'])
    return app


def create_seed():
    db.create_all()
    create_roles(5)
    create_servicelocations(10)
    create_employees(15)

def create_servicelocations(N):
    if not Servicelocation.query.first():
        for _ in range(N):
            sn, nm, ns = stringgenerator(4), stringgenerator(3), boolgenerator()
            SL = Servicelocation(shortname=sn, name=nm, nightshiftneeded=ns)
            db.session.add(SL)
        db.session.commit()


def create_roles(N):
    if not Role.query.first():
        for _ in range(N):
            sn, desc = stringgenerator(4), stringgenerator(15)
            user_datastore.create_role(name=sn, description=desc)
        db.session.commit()


def create_employees(N):
    if not Employee.query.first():

        sls = Servicelocation.query.all()
        rs = Role.query.all()

        user_datastore.create_user(
            firstname='Admin',
            lastname='Admin',
            username='Admin',
            password=utils.encrypt_password('PASSWORD'),
            nightshift=True,
            active=True,
            employedsince=datetime.datetime(2001, 1, 1),
            servicelocationid=random.choice(sls).id,
            weeklyhours=25,
            vacationdays=100
        )



        for _ in range(N):
            sl = random.choice(sls)
            r = random.choice(rs)

            fn, ln, un, pw, ns, a, es, wh, vd = stringgenerator(4), stringgenerator(5), stringgenerator(
                3), 'PASSWORD', boolgenerator(), True, datetime.datetime(2001, 1, 1), random.randint(30, 40), 25
            u = user_datastore.create_user(
                firstname=fn,
                lastname=ln,
                username=un,
                password=utils.encrypt_password(pw),
                nightshift=ns,
                active=a,
                employedsince=es,
                servicelocationid=sl.id,
                weeklyhours=wh,
                vacationdays=vd)

            user_datastore.add_role_to_user(u,r)

        db.session.commit()
