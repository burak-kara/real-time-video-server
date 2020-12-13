from flask import Flask, render_template, Response
from live_server.video_source.camera import VideoCamera
from flask_cors import CORS

app = Flask(__name__)
CORS(app)


@app.route('/')
def index():
    return render_template('test.html')


def gen(camera):
    while True:
        frame = camera.get_frame()

        yield b'--frame\r\n'b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n\r\n'
        # yield (b'Content-Type: video/mp4\r\n\r\n' + frame + b'\r\n\r\n')


@app.route('/live')
def live():
    return Response(gen(VideoCamera()), mimetype='multipart/x-mixed-replace; boundary=frame')


if __name__ == '__main__':
    app.run(host='127.0.0.1', port=8081, debug=True)
