from flask import Flask, render_template, url_for, jsonify, redirect, request, jsonify
import json
import requests
import urllib2
from pprint import pprint

# Setting up the web app using Flask
app = Flask(__name__)

# Homepage
@app.route("/")
def index():
    """Homepage."""

    return render_template('index.html')

@app.route('/repo_scan', methods=['GET'])
def repo_scan():
    repo_url = request.args.get('repo-url')
    # print '$$$$$$$$$$', repo_url
    foo = urllib2.urlopen(repo_url)
    response = foo.read()
    # print '*********', pprint(response)

    return jsonify(result=True)


if __name__ == "__main__":
    app.debug = True

    app.run(host="0.0.0.0")
