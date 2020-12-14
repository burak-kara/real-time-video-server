#!/bin/bash
ffmpeg -i udp://192.168.1.38:5000 -y -s 640x360 -c:v libx264 -b:v 512k -g 25 -sc_threshold 0 -max_muxing_queue_size 1024 -hls_time 2 -hls_list_size 100 stream.m3u8