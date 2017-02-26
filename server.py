from flask import Flask, render_template, url_for, jsonify, redirect, request


# Setting up the web app using Flask
app = Flask(__name__)

# Homepage
@app.route("/")
def index():
    """Homepage."""

    return render_template('index.html')



if __name__ == "__main__":
    app.debug = True

    app.run(host="0.0.0.0")
