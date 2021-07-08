from flask import Flask, render_template, request, redirect
import speech_recognition as sr

webapp = Flask(__name__, template_folder="./templates/")

@webapp.route("/", methods=["GET", "POST"])
def index():
    transcript = ""
    if request.method == "POST":
        print('FORM DATA RECEIVED')

        if "file" not in request.files:
            return redirect(request.url)

        file = request.files["file"]
        if file.filename == "": 
            return redirect(request.url)

        if file:
            recognizer = sr.Recognizer()
            audiofile = sr.AudioFile(file)
            with audiofile as source:
                data = recognizer.record(source)
            transcript = recognizer.recognize_google(data, key=None)

    return render_template('index.html', transcript = transcript)

if __name__ == "__main__":
    webapp.run(debug=True, threaded=True)