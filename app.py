import os
from flask import Flask

app = Flask(__name__)

color = "red"

@app.route("/")
def main():
    print(f"Set new background color to {color} ")
    return render_template()
