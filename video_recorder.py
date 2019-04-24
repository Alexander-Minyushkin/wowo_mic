import os
from subprocess import Popen

from flask import Flask
app = Flask(__name__)

ffmpeg_process = 0

@app.route('/')
def hello_world():
    return 'Hello, World!'
    
@app.route('/start')
def start():  
    
    global ffmpeg_process
    
    ffmpeg_process = Popen('ffmpeg -y -f alsa -i hw:0 -f x11grab -r 30 -video_size 1366x768 -i :0.0+0,0 -c:v libx264 -pix_fmt yuv420p -qp 0 ./tmp_1.avi'.split())
    return 'Started'
    
@app.route('/stop')
def stop():  
    
    global ffmpeg_process
    
    if ffmpeg_process != 0:
        ffmpeg_process.kill()
    
    return 'Stopped'

if __name__ == "__main__":
    app.run(debug=True,host='0.0.0.0',port=int(os.environ.get('PORT', 8080)))
    
# Ubuntu open port: $ sudo ufw allow 8080/tcp
# pip install pyopenssl // app.run(ssl_context='adhoc')
