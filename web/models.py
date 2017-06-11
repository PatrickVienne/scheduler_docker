import datetime
from flask import Flask
from flask_security import RoleMixin, SQLAlchemyUserDatastore, UserMixin
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class Base(db.Model):
    """Base class for all the tables.

    Consists of two default columns `created_at` and `modified_at` .
    """

    __abstract__ = True
    id = db.Column(db.Integer, primary_key=True)
    created_at = db.Column(db.DateTime, default=db.func.current_timestamp())
    modified_at = db.Column(db.DateTime,
                            default=db.func.current_timestamp(),
                            onupdate=db.func.current_timestamp())


roles_users = db.Table('roles_users', db.Column('user_id', db.Integer(),
                                                db.ForeignKey('employee.id')),
                       db.Column('role_id', db.Integer(),
                                 db.ForeignKey('auth_role.id')))


class Role(Base, RoleMixin):
    __tablename__ = 'auth_role'

    name = db.Column(db.String(80), nullable=False, unique=True)
    description = db.Column(db.String(255))

    def __repr__(self):
        """String representation of the class."""
        return '<Role %r>' % self.name
    def to_dict(self):
        tmp = self.__dict__
        del tmp['_sa_instance_state']
        del tmp['created_at']
        del tmp['modified_at']
        return tmp

class Servicelocation(Base):
    __tablename__ = 'servicelocation'

    shortname = db.Column(db.String(50), nullable=False)
    name = db.Column(db.String(50), nullable=False)
    nightshiftneeded = db.Column(db.Boolean())
    comment = db.Column(db.String(255))
    def to_dict(self):
        tmp = self.__dict__
        del tmp['_sa_instance_state']
        del tmp['created_at']
        del tmp['modified_at']
        return tmp

class Employee(Base, UserMixin):
    __tablename__ = 'employee'

    firstname = db.Column(db.String(50), nullable=False)
    lastname = db.Column(db.String(50), nullable=False)
    username = db.Column(db.String(50), nullable=False, unique=True)
    nightshift = db.Column(db.Boolean())
    password = db.Column(db.String(255), nullable=False)
    active = db.Column(db.Boolean())
    employedsince = db.Column(db.DateTime())
    servicelocationid = db.Column(db.Integer, db.ForeignKey('servicelocation.id'))
    weeklyhours = db.Column(db.Integer)
    vacationdays = db.Column(db.Integer)
    comments = db.Column(db.String(255))
    roles = db.relationship('Role',
                            secondary=roles_users,
                            backref=db.backref('users', lazy='dynamic'))

    # def __init__(self, firstname, lastname, username, nightshift, password, active, employedsince, weeklyhours,
    #              vacationdays, comments):
    #     self.firstname = firstname
    #     self.lastname = lastname
    #     self.username = username
    #     self.nightshift = nightshift
    #     self.password = password
    #     self.active = active
    #     self.employedsince = employedsince
    #     self.weeklyhours = weeklyhours
    #     self.vacationdays = vacationdays
    #     self.comments = comments

    def to_dict(self):
        tmp = self.__dict__
        del tmp['_sa_instance_state']
        del tmp['created_at']
        del tmp['modified_at']
        del tmp['password']
        #datetime.datetime.utcfromtimestamp(tmp['employedsine'])
        tmp['employedsince'] = tmp['employedsince'].strftime("%Y-%m-%d")
        return tmp

    def __repr__(self):
        return '<User %r>' % self.username


#db.create_all()

user_datastore = SQLAlchemyUserDatastore(db, Employee, Role)
