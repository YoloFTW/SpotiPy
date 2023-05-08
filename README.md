# SpotiPy

SpotiPy is a Python application that uses the Spotify API to display the currently playing song on a local Flask server. SpotiPy is designed to be used by streamers who want to display the currently playing song on their stream. It can be easily integrated into streaming software like OBS using the browser capture feature.

<br/>

## Getting Started

Before you can use SpotiPy, you will need to register an application with the Spotify Developer Dashboard to obtain a client ID and client secret. Follow these steps to get started:

1. Run the `setup.py` file to install the required dependencies
2. Go to the [Spotify Developer Dashboard](https://developer.spotify.com/dashboard) and log in to your Spotify account (or create a new account if you don't have one).
3. Click the "Create An App" button and enter a name and description for your app.
4. Input http://(IP):8000/callback for the redirect URI. (IP) is the IP address of the machine running the SpotiPy server
</br> e.g. http://192.168.0.1:8000/callback</br>
you can find your ip address [here](https://api.ipify.org/)
5. Once your app is created, note the client ID and client secret that are provided.
6. Open the `.env` file in the SpotiPy directory and replace the `CLIENT_ID` and `CLIENT_SECRET` variables with the values from your Spotify app.

7. Start the Flask server by running the following command:
```shell
python main.py
```
8. access your flask server from [localhost:8000](http://localhost:8000)

9. follow the on screen instructions to authorise your app to access your Spotify account 

### Dependencies

* python 3.10
* pip installed to path

<br/>

## Authors

Contributors names
* [@YoloFTW](https://github.com/YoloFTW)

<br/>

## License

This project is licensed under the MIT License - see the [LICENSE](https://github.com/YoloFTW/SpotiPy/blob/main/LICENSE) file for details