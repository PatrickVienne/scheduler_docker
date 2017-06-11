import logging
import json
from flask import request, make_response
from flask_security import auth_token_required
from gevent.wsgi import WSGIServer

from models import Employee, db, Servicelocation, Role
from factory import create_app, create_seed

logger = logging.getLogger(__name__)
app = create_app()

# Flask(__name__)


@app.before_first_request
def init():
    create_seed()


@app.route('/')
def hello_world():
    return json.dumps([{"id": 1, "name": "wtf"}])

@app.route("/testauth")
@auth_token_required
def testauth():
    return 'sollte nicht sein'


@app.route('/employee/create', methods=['PUT'])
def create_employee():
    # print request.
    employee_data = json.loads(request.data)
    emp = Employee()
    for k,v in employee_data.iteritems():
        if k == 'id': continue
        emp.__setattr__(k, v)
    db.session.add(emp)
    return make_response()


@app.route('/employee/update', methods=['PUT'])
def edit_employee():
    # print request.
    employee_data = json.loads(request.data)
    emp = Employee.query.get(employee_data['id'])
    if emp:
        for k,v in employee_data.iteritems():
            if k == 'id': continue
            emp.__setattr__(k, v)
        db.session.commit()
        return make_response()
    else:
        return make_response()


@app.route('/employee/delete/<int:id>', methods=['DELETE'])
def delete_employee(id):
    # print request.
    emp = Employee.query.get(id)
    print emp
    if emp:
        db.session.delete(emp)
        db.session.commit()
    return "Deleting %i" % id


@app.route('/employee/get_employees', methods=['GET'])
def get_employees():
    return json.dumps([emp.to_dict() for emp in Employee.query.all()])


@app.route('/employee/get/<int:id>', methods=['GET'])
def get_employee(id):
    emp = Employee.query.get(id)
    if emp:
        return json.dumps(emp.to_dict())
    else:
        return json.dumps({"id": 0, "firstname":""})


@app.route('/servicelocation/create', methods=['PUT'])
def create_servicelocation():
    # print request.
    servicelocation_data = json.loads(request.data)
    sloc = Servicelocation()
    for k,v in servicelocation_data.iteritems():
        if k == 'id': continue
        sloc.__setattr__(k, v)
    db.session.add(sloc)
    return make_response()


@app.route('/servicelocation/update', methods=['PUT'])
def edit_servicelocation():
    # print request.
    servicelocation_data = json.loads(request.data)
    sloc = Servicelocation.query.get(servicelocation_data['id'])
    if sloc:
        for k,v in servicelocation_data.iteritems():
            if k == 'id': continue
            sloc.__setattr__(k, v)
        db.session.commit()
        return make_response()
    else:
        return make_response()


@app.route('/servicelocation/delete/<int:id>', methods=['DELETE'])
def delete_servicelocation(id):
    # print request.
    sloc = Servicelocation.query.get(id)
    print sloc
    if sloc:
        db.session.delete(sloc)
        db.session.commit()
    return "Deleting %i" % id


@app.route('/servicelocation/get_servicelocations', methods=['GET'])
def get_servicelocations():
    return json.dumps([sloc.to_dict() for sloc in Servicelocation.query.all()])


@app.route('/servicelocation/get/<int:id>', methods=['GET'])
def get_servicelocation(id):
    sloc = Servicelocation.query.get(id)
    if sloc:
        return json.dumps(sloc.to_dict())
    else:
        return json.dumps({"id": 0, "name":""})


@app.route('/role/get_roles', methods=['GET'])
def get_roles():
    return json.dumps([role.to_dict() for role in Role.query.all()])


def main():
    """Main entry point of the app."""
    try:
        http_server = WSGIServer(('127.0.0.1', 8081),
                                 app,
                                 log=logging,
                                 error_log=logging)

        http_server.serve_forever()
    except Exception as exc:
        logger.error(exc.message)
        print exc.message
    finally:
        # get last entry and insert build appended if not completed
        # Do something here
        print "finished"
        pass
