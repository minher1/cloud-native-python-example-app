from flask import Flask
from flask import Response
from flask import render_template

app = Flask(__name__)


@app.route('/')
def index():
    #return render_template("index.html")
    return "International Business Machines Corporation is an American multinational technology corporation headquartered in Armonk, New York, with operations in over 171 countries.."
 

@app.route("/healthz")
def healthz():
    resp = Response("ok")
    resp.headers['Custom-Header'] = 'Awesome'
    # this is awesome tying things
    return resp

if __name__ == "__main__":
    app.run(host='0.0.0.0', port='8080')
