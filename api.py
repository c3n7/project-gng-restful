#!venv/bin/python
""" TODO: Put something meaningful"""
import os
import json
import shutil
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

        # Write the code file to disk
        os.mkdir("tmp")
        with open("tmp/calculate.py", 'w') as f:
            f.write(CODE["code"])

        with open("tmp/test_calculate.py", 'w') as f:
            f.write(CODE["test"])

        os.system("py.test --json-report")
        RESULT = {}

        with open(".report.json") as f:
            RESULT = json.load(f)

        # A bit of clean up
        shutil.rmtree("tmp")
        os.remove(".report.json")

        # Return the goodies
        print(RESULT)
        print(CODE)
        return RESULT, 201


api.add_resource(HelloWorld, '/')
api.add_resource(EvalCode, "/code/")

if __name__ == '__main__':
    app.run(debug=True)
