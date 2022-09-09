# Importing flask module in the project is mandatory
# An object of Flask class is our WSGI application.

from flask import Flask, render_template, url_for, request, jsonify
from brain import runCommand
import time
import os
# Flask constructor takes the name of
# current module (__name__) as argument.
app = Flask(__name__)

# The route() function of the Flask class is a decorator,
# which tells the application which URL should call
# the associated function.


@app.route('/')
# ‘/’ URL is bound with hello_world() function.
def index():
    return render_template('index.html')

@app.route('/runCommand', methods=['POST'])
def runComm():
    if request.method == "POST":
        command = request.json['command']
        output = runCommand(command)
        print(output)
        if output=='cd success':
            return jsonify({"currentDir":os.getcwd()})
        else:
            return jsonify({"output":output})
    
@app.route('/setCurrentDir', methods=['POST'])
def setCurrentDir():
    if request.method == "POST":
        print(os.getcwd())
        os.chdir('C:\\Users\\LoneWolf')
        print(os.getcwd())
        return jsonify({"currentDir":os.getcwd()})

# main driver function
if __name__ == '__main__':

    # run() method of Flask class runs the application
    # on the local development server.
    app.run(debug=True, port=80)
