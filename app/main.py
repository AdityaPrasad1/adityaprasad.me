from flask import Flask, render_template
from flask_bootstrap import Bootstrap

app = Flask(__name__)
Bootstrap(app)

@app.before_request
def before_request() :
    if request.url.startswith('http://') :
        url = request.url.replace('http://', 'https://', 1)
        code = 301
        return redirect(url, code=code)

@app.route("/")
def index() :
    return render_template('index.html')

@app.route("/experience/")
def experience() :
    return render_template('experience.html')

@app.route("/projects/")
def projects() :
    return render_template('projects.html')

@app.route("/bio/")
def bio() :
    return render_template('bio.html')

if __name__ == "__main__" :
    app.run(host='0.0.0.0', port=443, ssl_context='adhoc')
