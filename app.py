from flask import Flask, render_template, request
import requests

app = Flask(__name__)

def translate_text(text, source_lang, target_lang):
    url = "https://api.mymemory.translated.net/get"
    params = {
        'q': text,
        'langpair': f'{source_lang}|{target_lang}'
    }
    response = requests.get(url, params=params)
    data = response.json()
    return data['responseData']['translatedText']

@app.route("/", methods=["GET", "POST"])
def home():
    translated_text = ""
    if request.method == "POST":
        text = request.form["text"]
        source_lang = request.form["source_lang"]
        target_lang = request.form["target_lang"]
        translated_text = translate_text(text, source_lang, target_lang)
    return render_template("index.html", translated_text=translated_text)

if __name__ == "__main__":
    app.run(debug=True)
