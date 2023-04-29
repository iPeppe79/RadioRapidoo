from flask import Flask, render_template
from flask_ask import Ask, statement, audio
import vlc

app = Flask(__name__)
ask = Ask(app, '/')

@app.route('/')
def homepage():
    return "Hello, world!"

@ask.launch
def start_skill():
    welcome_message = 'Ciao, benvenuto su Radio Rapidoo. Vuoi avviare lo streaming audio?'
    return question(welcome_message)

@ask.intent("YesIntent")
def play_radio():
    url = "https://nrf1.newradio.it:10456/SOLDOUT"
    player = vlc.MediaPlayer(url)
    player.play()
    return audio().play(url)

@ask.intent("AMAZON.PauseIntent")
def pause_radio():
    player.pause()
    return statement("La radio è stata messa in pausa")

@ask.intent("AMAZON.ResumeIntent")
def resume_radio():
    player.play()
    return audio().play(url)

if __name__ == '__main__':
    app.run(debug=True)
