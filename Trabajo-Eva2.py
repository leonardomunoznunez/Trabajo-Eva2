from flask import Flask

app = Flask(__name__)

@app.route('/hola')
def hola_mundo():
    return 'Hola Mundo programación de redes'

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=3000)

