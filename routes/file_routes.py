import os

from flask import Blueprint, render_template, request, send_from_directory, redirect, url_for
from file_utils import allowed_file, save_file
from config import Config

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
        filename = save_file(file)  # Sauvegarde le fichier et retourne le nom
        uploaded_image_url = f"/uploaded_file/{filename}"  # URL pour afficher l'image

        return render_template('index.html',
                               success="Fichier téléchargé avec succès.",
                               uploaded_image=uploaded_image_url,
                               filename=filename)

    return render_template('index.html', error="Fichier invalide. Veuillez télécharger une image.")



@file_routes.route('/uploaded_file/<filename>')
def uploaded_file(filename):
    return send_from_directory(Config.UPLOAD_FOLDER, filename)

@file_routes.route('/delete_file/<filename>', methods=['POST'])
def delete_file(filename):
    # Construire le chemin complet de l'image
    file_path = os.path.join(Config.UPLOAD_FOLDER, filename)
    # Vérifier si le fichier existe, puis le supprimer
    if os.path.exists(file_path):
        os.remove(file_path)
    # Rediriger vers la page d'accueil
    return redirect(url_for('file_routes.index'))