from flask import Flask
import os

app = Flask(__name__)

@app.route("/")
def hello():
    hostname = os.environ['HOST_OPTS']
    return '[{}] hello flask web\n'.format(hostname)

if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True, port=9999)


