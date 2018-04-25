from flask import Flask, render_template
from flask_bootstrap import Bootstrap

app = Flask(__name__)
Bootstrap(app)

@app.route("/")
def index() :
    return render_template('index.html')

@app.route("/credentials/")
def credentials() :
    return render_template('credentials.html')

@app.route("/projects/")
def projects() :
    return render_template('projects.html')

@app.route("/bio/")
def bio() :
    return render_template('bio.html')

if __name__ == "__main__" :
    app.run(host='0.0.0.0', debug=True, port=80)
