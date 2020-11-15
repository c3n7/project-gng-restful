#!venv/bin/python
""" TODO: Put something meaningful"""
from flask import Flask
from flask_restful import Resource, Api, reqparse

app = Flask(__name__)
api = Api(app)

parser = reqparse.RequestParser()
# For the student resource
parser.add_argument("name")
parser.add_argument("age")
parser.add_argument("spec")

# For the code resource
parser.add_argument("code")
parser.add_argument("test")

CODE = {}


class HelloWorld(Resource):
    """Returns hello world"""

    def get(self):
        return {'noma': 'tupu'}


class EvalCode(Resource):
    """Runs code and returns the result"""

    def get(self):
        return CODE

    def post(self):
        args = parser.parse_args()
        CODE = {
            "code": args["code"],
            "test": args["test"]
        }
        eval(CODE["code"])
        print(CODE)
        return CODE, 201


api.add_resource(HelloWorld, '/')
api.add_resource(EvalCode, "/code/")

if __name__ == '__main__':
    app.run(debug=True)
