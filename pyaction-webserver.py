from flask import Flask
from flask_restful import Api, Resource, reqparse
import os

app = Flask(__name__)
api = Api(app)

class Action(Resource):
    def get(self, name):
        return name, 200

    def post(self, name):
        # For adding additional parameters:
        # parser = reqparse.RequestParser()
        # parser.add_argument("arg_name")
        # args = parser.parse_args()
        # print(args["arg_name"])

        # Action exmple: play song on Ubuntu
        if(name == "handsome"):
            os.system("aplay you-look-so-handsome.wav")


api.add_resource(Action, "/action/<string:name>")
app.run(debug=True, host='0.0.0.0')