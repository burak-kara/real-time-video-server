import cv2
from flask import Flask, render_template, send_from_directory

app = Flask(__name__)


@app.after_request
def add_header(response):
    response.headers['X-UA-Compatible'] = 'IE=Edge,chrome=1'
    response.headers['Cache-Control'] = 'no-cache, no-store, must-revalidate'
    response.headers['Pragma'] = 'no-cache'
    response.headers['Expires'] = '0'
    # response.headers['Content-Type'] = 'application/x-mpegURL'
    return response


@app.route('/')
def index():
    return render_template('index.html')


# @app.route('/live/stream.m3u8')
# def stream():
#     video_dir = './live'
#     return send_from_directory(directory=video_dir, filename="stream.m3u8")
#

@app.route('/live/<string:file_name>')
def stream(file_name):
    video_dir = './live'
    return send_from_directory(directory=video_dir, filename=file_name)


if __name__ == '__main__':
    app.run(host='127.0.0.1', port=8080, debug=True)