""" TODO: Put something meaningful"""
from flask import Flask
from flask_restful import Resource, Api, reqparse

app = Flask(__name__)
api = Api(app)
parser = reqparse.RequestParser()
parser.add_argument("name")
parser.add_argument("age")
parser.add_argument("spec")

STUDENTS = {
    '1': {'name': 'Mark', 'age': 23, 'spec': 'math'},
    '2': {'name': 'Jane', 'age': 20, 'spec': 'biology'},
    '3': {'name': 'Peter', 'age': 21, 'spec': 'history'},
    '4': {'name': 'Kate', 'age': 22, 'spec': 'science'},
}


class HelloWorld(Resource):
    def get(self):
        return {'noma': 'tupu'}


class StudentsList(Resource):
    def get(self):
        return STUDENTS

    def post(self):
        args = parser.parse_args()
        student_id = int(max(STUDENTS.keys())) + 1
        student_id = '%i' % student_id
        STUDENTS[student_id] = {
            "name": args["name"],
            "age": args["age"],
            "spec": args["spec"],
        }
        return STUDENTS[student_id], 201


api.add_resource(HelloWorld, '/')
api.add_resource(StudentsList, '/students/')

if __name__ == '__main__':
    app.run(debug=True)
