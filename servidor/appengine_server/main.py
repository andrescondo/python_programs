# -*- coding: utf-8 -*-

from flask import Flask,render_template
app = Flask(__name__)


@app.route('/')
def hola():
    return render_template('index.html')
    # la carpeta donde se manda, debe llamarse "templates", en caso de no poner el nombre correcto el programa no correra



if __name__ == '__main__':
    app.run()