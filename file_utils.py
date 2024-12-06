import os
from werkzeug.utils import secure_filename
from flask import current_app

def allowed_file(filename):
    """Vérifie si le fichier a une extension autorisée."""
    allowed_extensions = current_app.config['ALLOWED_EXTENSIONS']
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in allowed_extensions

def save_file(file):
    """Sauvegarde le fichier téléchargé et retourne son nom de fichier."""
    upload_folder = current_app.config['UPLOAD_FOLDER']
    filename = secure_filename(file.filename)
    filepath = os.path.join('static/uploads', filename)
    file.save(filepath)
    return filename