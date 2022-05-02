ffmpeg -f lavfi -i anullsrc=channel_layout=stereo:sample_rate=44100 -f v4l2 -i /dev/video0 -c:v libx264 -pix_fmt yuv420p -preset ultrafast -g 10 -b:v 2500k -bufsize 512k -acodec libmp3lame -ar 44100 -threads 2 -qscale 3 -b:a 96K -r 10 -s 960x540 -f flv rtmp://a.rtmp.youtube.com/live2/$STREAM_KEY

