from flask import Flask, render_template, request, send_file
import pyttsx3
import os

app = Flask(__name__)

# Define the directory to save audio files
AUDIO_FOLDER = os.path.join(os.getcwd(), 'static/audio')
if not os.path.exists(AUDIO_FOLDER):
    os.makedirs(AUDIO_FOLDER)

def text_to_speech(text, filename):
    engine = pyttsx3.init()
    engine.save_to_file(text, os.path.join(AUDIO_FOLDER, filename))
    engine.runAndWait()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/convert', methods=['POST'])
def convert():
    text = request.form['text']
    filename = 'output.mp3'
    text_to_speech(text, filename)
    return render_template('convert.html', audio_file=os.path.join('audio/', filename))
    return send_file(os.path.join(AUDIO_FOLDER, filename), as_attachment=True)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000,debug=True)






#if __name__ == '__main__':
#    app.run(host='0.0.0.0', port=5000, debug=True)












#from flask import Flask, render_template, request, send_file
#import pyttsx3
#import os

#app = Flask(__name__)

# Define the directory to save audio files
#AUDIO_FOLDER = os.path.join(os.getcwd(), 'static/audio')
#if not os.path.exists(AUDIO_FOLDER):
 #   os.makedirs(AUDIO_FOLDER)

#def text_to_speech(text, filename):
#   engine = pyttsx3.init()
#  engine.save_to_file(text, os.path.join(AUDIO_FOLDER, filename))  
# engine.runAndWait()

#@app.route('/')
#def index():
#    return render_template('index.html')

#@app.route('/convert', methods=['POST'])
#def convert():
#    text = request.form['text']
#    filename = 'output.mp3'
#    text_to_speech(text, filename)
#    filename = 'output.mp3'
#   return render_template('convert.html', audio_file=os.path.join('audio/', filename))
#   return send_file(os.path.join(AUDIO_FOLDER, filename), as_attachment=True) 

#@app.route('/convert')
#def play():
#    filename = 'output.mp3'
#    return render_template('convert.html', audio_file=os.path.join('audio/', filename))  

#if __name__ == '__main__':
#    app.run(host='0.0.0.0', port=5000,debug=True)









# from flask import Flask, render_template, request, send_file
# import pyttsx3
# import os

# app = Flask(__name__)

# def text_to_speech(text):
#     engine = pyttsx3.init()
#     engine.save_to_file(text, 'output.mp3')  # Save the speech as output.mp3
#     engine.runAndWait()

# @app.route('/')
# def index():
#     return render_template('index.html')

# @app.route('/convert', methods=['POST'])
# def convert():
#     text = request.form['text']
#     text_to_speech(text)
#     return send_file('output.mp3', as_attachment=True)  # Serve the audio file for download

# if __name__ == '__main__':
#     app.run(host='0.0.0.0', port=5000)






# from flask import Flask, render_template, request
# import pyttsx3

# app = Flask(__name__)

# def text_to_speech(text):
#     engine = pyttsx3.init()
#     engine.say(text)
#     engine.runAndWait()

# @app.route('/')
# def index():
#     return render_template('index.html')

# @app.route('/convert', methods=['POST'])
# def convert():
#     text = request.form['text']
#     text_to_speech(text)
#     return "Speech generated and played successfully!"

# if __name__ == '__main__':
#     app.run(debug=True)
