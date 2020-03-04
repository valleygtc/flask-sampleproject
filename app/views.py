from flask import Blueprint, jsonify, request, current_app

from . import db
from .models import Student


bp_main = Blueprint('bp_main', __name__)


"""
GET
resp: 200
"""
@bp_main.route('/')
def hanlde_hello():
    ua = request.headers.get('User-Agent')
    current_app.logger.info('access from User-Agent: %s', ua)
    return 'Hello, World!'


"""/students/
GET
resp: 200, body中的"data"字段:
[{
    "id": [Number],
    "name": [String],
    "remark": [String],
    "create_at": [String]
}, ...]
"""
@bp_main.route('/students/')
def hanlde_show_students():
    records = Student.query.all()

    columns = ['id', 'name', 'age', 'address']

    resp = {
        'data': [r.readyToJSON(columns) for r in records]
    }
    return jsonify(resp)


"""
POST:
{
    "name": [String],
    "age": [Number], [Optional]
    "address": [String] [Optional]
}
resp: 200, body: {"msg": [String]}
"""
@bp_main.route('/students/add', methods=['POST'])
def hanlde_add_student():
    data = request.get_json()
    if 'name' not in data:
        return jsonify({
            'msg': '要添加的学生必须含有姓名',
        }), 400

    record = Student(
        name=data['name'],
        age=data.get('age'),
        address=data.get('address'),
    )
    db.session.add(record)
    db.session.commit()
    return jsonify({
        'msg': f'成功添加学生: {record}',
    })
