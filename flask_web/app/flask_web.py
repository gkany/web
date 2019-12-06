from flask import Flask
import os
import datetime

app = Flask(__name__)

@app.route("/")
def hello():
    hostname = 'localhost-test'
    if 'HOST_OPTS' in os.environ:
        hostname = os.environ['HOST_OPTS']
    now_time = datetime.datetime.utcnow().strftime('%Y-%m-%d %H:%M:%S')
    ret = '[{}][{}] hello flask web\n'.format(hostname, now_time)
    return ret

if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True, port=8041)


