from flask import Flask
app = Flask(__name__)

@app.route("/about")
def about():
    return "Tady je Python backend: stránka About"
