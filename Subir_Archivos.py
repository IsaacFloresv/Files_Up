import os
from os import path
from pathlib import Path
from flask import Flask, render_template, request, send_file

app = Flask(__name__)
app.config['UPLOAD_FOLDER']="./Archivos PDF"

@app.route("/")
def upload_file():
    return render_template('formulario.html')

@app.route("/uploader", methods=['POST'])
def uploader():
    if request.method == "POST":
        #Get the name of the client
        usuario = request.form['usuario']
        #Get the name of the directory where the files will be saved
        folder = os.path.join(app.config['UPLOAD_FOLDER'],usuario)
        #It is confirmed if the directory exists, if it doesn't exist, the folder is created
        if (os.path.isdir(folder)== False):
            os.makedirs(folder)

        #Get the name of the file
        f = request.files['archivo']
        filename = f.filename
        ruta = os.path.join(folder,filename)
        #It is confirmed if the file exists in the directory, if it doesn't exist, the file is saved
        if os.path.isfile(ruta):
            return 'the file already exists.'
        else:
            #The file is saved
            f.save(ruta)
    return send_file(ruta)

if __name__ == '__main__':
    app.run(host='0.0.0.0',port=3000,debug=True) 