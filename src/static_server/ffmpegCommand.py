import os

os.system("ffmpeg -f dshow -i video=\"HD Webcam\":audio=\"Microphone (Realtek(R) Audio)\" -vcodec libx264 -segment_time 2 -f rtsp rtsp://192.168.1.38:1935/rtmp/teststr.sdp")
