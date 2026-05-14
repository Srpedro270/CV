from flask import Flask, render_template, request, redirect, url_for
import json
import smtplib
from email.mime.text import MIMEText
from secret import EMAIL_USER, EMAIL_PASS 

app = Flask(__name__)

@app.route("/")
def home():
    with open('data/CV.json', 'r', encoding='utf-8') as f:
        dados_cv = json.load(f)
    return render_template('index.html', cv=dados_cv)

@app.route("/send_request", methods=["POST"])
def send_request():
    name = request.form['name']
    email = request.form['email']
    message = request.form['message']
    
    print(f"Novo pedido de: {name} - {email}")
    
    corpo = f"Nome: {name}\nEmail: {email}\nMensagem: {message}"
    msg = MIMEText(corpo)
    msg['Subject'] = f'Novo contato do portfólio - {name}'
    msg['From'] = EMAIL_USER
    msg['To'] = EMAIL_USER

    try:
        with smtplib.SMTP('smtp.gmail.com', 587) as server:  # MUDOU AQUI
            server.starttls()
            server.login(EMAIL_USER, EMAIL_PASS)
            server.send_message(msg)
        print("EMAIL ENVIADO COM SUCESSO!")
    except Exception as e:
        print(f"ERRO AO ENVIAR EMAIL: {e}")
    
    return redirect(url_for('home'))

if __name__ == "__main__":
    app.run(debug=True)
