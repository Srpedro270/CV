from flask import Flask, render_template
import json

app = Flask(__name__)

@app.route("/")
def homepage():
    # Carrega teus dados do JSON
    with open('data/cv.json', 'r', encoding='utf-8') as f:
        dados_cv = json.load(f)
        
    return render_template('index.html', cv=dados_cv)

if __name__ == "__main__":
    app.run(debug=True)