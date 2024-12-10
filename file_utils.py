import os
from werkzeug.utils import secure_filename
from flask import current_app
from config import Config

def allowed_file(filename):
    """Vérifie si le fichier a une extension autorisée."""
    allowed_extensions = current_app.config['ALLOWED_EXTENSIONS']
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in allowed_extensions

def save_file(file):
    # Sécurisez le nom du fichier
    filename = secure_filename(file.filename)
    file_path = os.path.join(Config.UPLOAD_FOLDER, filename)

    # Sauvegarde du fichier
    file.save(file_path)
    return filename

