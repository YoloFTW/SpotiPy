
import os
from dotenv import load_dotenv
from .GetPlaying import getCurrentSong


class Worker(object):

    switch = False
    unit_of_work = 0

    def __init__(self, socketio):
        
        #initialise class variables
        self.socketio = socketio
        self.switch = True
        

    def UpdateSong(self, app, socketio):
        """
        Updates the currently playing song

        Args:
            app: (dict) - the current app object\n
            socketio: (socketio) - the socketio socket\n
        """
    
        with app.app_context():

            #reloads .env file
            load_dotenv()

            # if access token is pressent
            if "AT" in os.environ:

                #while socket still open
                while self.switch:

                    load_dotenv()

                    currentlyPlaying = getCurrentSong(os.getenv("AT"))

                    socketio.emit('updateSong', { 'data':  currentlyPlaying})

                    socketio.sleep(10)
    

    def stop(self):
        """
        stops the UpdateSong function

        """
    
        #stop the loop
        self.switch = False



