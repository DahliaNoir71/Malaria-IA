from flask import Blueprint, render_template, request
from file_utils import allowed_file, save_file

file_routes = Blueprint('file_routes', __name__)

@file_routes.route('/', methods=['GET'])
def index():
    return render_template('index.html')

@file_routes.route('/upload', methods=['POST'])
def upload_file():
    file = request.files.get('file')

    if not file:
        return render_template('index.html', error="Aucun fichier n'a été sélectionné")

    if file.filename == '':
        return render_template('index.html', error="Veuillez sélectionner un fichier")

    if allowed_file(file.filename):
        filename = save_file(file)
        return render_template('result.html', filename=filename)

    return render_template('index.html', error="Fichier invalide. Veuillez télécharger une image.")