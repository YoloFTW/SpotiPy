from flask import Flask, render_template, request, redirect, send_from_directory, make_response, current_app
from flask_socketio import SocketIO, emit
import logging
from dotenv import load_dotenv

import threading
import os

from utilities.GetIp import getIp
from utilities.UpdateEnv  import updateEnvVar
from utilities.GenerateAuthUrl  import GenerateAuthUrl
from utilities.UpdateSongClass  import Worker
from utilities.UpdateAccessToken import UpdateAccessToken

thread = None
thread_lock = threading.Lock()

# set logging level
log = logging.getLogger('werkzeug')
log.setLevel(logging.ERROR)

app = Flask(__name__)
socketio = SocketIO(app)

@app.route("/")
def index():

    # reloads .env file
    load_dotenv()

    # if access token is pressent
    if "AT" in os.environ:

        renderedTemplate = render_template("index.html", currentlyPlaying={})

        response = make_response(renderedTemplate)


    # if access token doesnt exist
    else:
        response = make_response(redirect("/auth-app"))
        

    return response
    


@app.route("/auth-app")
def authApp():

    # generate authentication url for spotify app
    authUrl = GenerateAuthUrl()

    # return auth page
    return render_template("authApp.html",authUrl=authUrl)




@app.route("/callback")
def callback():

    # reloads .env file
    load_dotenv()

    # Extract the authorization code from the callback URL
    authCode = request.args.get("code")

    # get users access token
    UpdateAccessToken(authCode, None)

    # redirect to main page
    response = make_response(redirect("/"))

    return response


# return favicon so cloudflare is happy
@app.route("/favicon.ico")
def favicon():
    return send_from_directory(os.path.join(app.root_path, "static/images"), "SpotiPy.ico", mimetype='image/vnd.microsoft.icon')


# initialise workers dictionary
@app.before_first_request
def initialize_app_variables():
    
    # reloads .env file
    load_dotenv()

    # if ip not set
    if not 'IP' in os.environ:

        # add ip to enviroment
        updateEnvVar("IP", getIp())

    current_app.config['workers'] = {}


# on websocket connection
@socketio.on('connect')
def test_connect(auth):
    emit('my response', {'data': 'Connected'})

# on websocket disconnection
@socketio.on('disconnect')
def test_disconnect():

    # get sid from socket
    sid = request.sid

    # stop background proccess
    if "workers" in current_app.config and sid in current_app.config['workers']:
        current_app.config['workers'][sid].stop()



# on websocket message
@socketio.on("message")
def handle_message(data):

    # get spocketId
    sid = request.sid

    # import class from 
    worker = Worker(socketio)

    # start backgrouund process
    socketio.start_background_task(worker.UpdateSong, current_app._get_current_object(), socketio)

    # add worker to enviroment
    if "workers" in current_app.config:
        current_app.config['workers'][sid] = worker



if __name__ == "__main__":

    app.run(host="0.0.0.0", port=8000)
    socketio.run(app)