from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    """
    Renderiza la página principal del mapa.
    """
    return render_template('index.html')

    # Se recomienda usar un puerto diferente al 5000 si es común en tu sistema.
#if __name__ == '__main__':
    #app.run(debug=True, port=5001)