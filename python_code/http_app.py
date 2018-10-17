from flask import Flask, Response
from flask_restful import Resource, Api
import time
import cv2
import threading

app = Flask(__name__)
api = Api(app)

latest_vision_result = {'state' : 'None', 'range' : 1000000, 'angle' : 900, 'time' : str(time.time())}

class VisionResult(Resource):
    def get(self):
        return latest_vision_result

def gen_image():
    cap=cv2.VideoCapture(0)
    cap.set(3,640)
    cap.set(4,480)
    while(True):
        ret, frame = cap.read()
        revtval, data = cv2.imencode('.jpg',frame)
        yield(b'--frame\r\nContent-Type: image/jpeg\r\n\r\n' + data.tobytes() + b'\r\n')

@app.route('/stream')
def video_stream():
    return Response(gen_image(),mimetype='multipart/x-mixed-replace; boundary=frame')



api.add_resource(VisionResult, '/')

if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=False)
