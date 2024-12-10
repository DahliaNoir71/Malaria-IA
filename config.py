import os

class Config:
    # Configuration générale de l'application
    SECRET_KEY = os.environ.get('SECRET_KEY', 'votre_clé_secrète')  # Utilisation d'une variable d'environnement
    BASE_DIR = os.path.abspath(os.path.dirname(__file__))
    UPLOAD_FOLDER = os.path.join(BASE_DIR, 'static', 'uploads')
    ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg', 'gif'}
    MAX_CONTENT_LENGTH = 16 * 1024 * 1024  # Limite de taille de fichier : 16MB

    # Configuration pour le modèle de prédiction (si nécessaire)
    MODEL_PATH = 'model/model_cnn.keras'  # Chemin vers le modèle enregistré