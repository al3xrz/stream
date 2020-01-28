bash -c "exec -a ffmpeg_$1 ffmpeg  -rtsp_transport tcp -y -r 15 -f rtsp -i rtsp://91.205.130.102:554/live?id=$1 http://127.0.0.1:8090/camera_$1.ffm"





