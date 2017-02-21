from flask import Flask
from flask_restful import Resource, Api
import time

app = Flask(__name__)
api = Api(app)

latest_vision_result = {'state' : 'None', 'range' : 1000000, 'angle' : 900, 'time' : str(time.time())}

class VisionResult(Resource):
    def get(self):
        return latest_vision_result

api.add_resource(VisionResult, '/')

if __name__ == "__main__":
    app.run(debug=False)