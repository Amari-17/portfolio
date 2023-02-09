from flask import Flask,render_template,redirect,url_for
from flask_bootstrap import Bootstrap
from detail_collector import DetailCollector


app = Flask(__name__)
app.config['Secret_KEY'] = '83hs293C0926jcw2FJ893Bd3E'

Bootstrap(app)

detail = DetailCollector()

@app.route("/")
@app.route("/home")
def home():
    return render_template('index.html',details = detail)

if __name__ == "__main__":
    app.run()