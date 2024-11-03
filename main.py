from flask import Flask
import random

app = Flask(__name__)
facts_list = [
    "Elon Musk afirma que las redes sociales están diseñadas para mantenernos dentro de la plataforma, de modo que pasemos el mayor tiempo posible viendo contenidos.", 
    "Según un estudio realizado en 2018, más del 50% de las personas de entre 18 y 34 años se consideran dependientes de sus smartphones.", 
    "Las redes sociales tienen aspectos positivos y negativos, y debemos ser conscientes de ambos cuando utilicemos estas plataformas.", 
    "El estudio de la dependencia tecnológica es una de las áreas más relevantes de la investigación científica moderna."
]

@app.route("/")
def index():
    return '''
        <h1>Hola, en esta página puedes aprender un par de cosas interesantes sobre las dependencias tecnológicas.</h1>
        <a href="/random_fact">¡Ver un hecho al azar!</a><br>
        <a href="/RUTA">¡Ver generador de contraseñas!</a>
    '''

@app.route("/random_fact")
def facts():
    return f'<p>{random.choice(facts_list)}</p>'

@app.route("/RUTA")
def contraseña():
    caracteres = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890!@#$%^&*()"
    password = ''.join(random.choice(caracteres) for _ in range(10))
    return f'<h1>Contraseña generada: {password}</h1>'

if __name__ == "__main__":
    app.run(debug=True)
