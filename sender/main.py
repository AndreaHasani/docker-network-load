from flask import Flask
from flask_restful import Resource, Api

app = Flask(__name__)
api = Api(app)

data = {"dummy1": "return, dummy"}

#Nested json
# data = {"dummy1": {"nested, dummy": "return, dummy"}}

class Recommendations(Resource):
    def get(self):
        return data

api.add_resource(Recommendations, '/')

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)
