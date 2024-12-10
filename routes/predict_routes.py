from flask import Blueprint, render_template
from model import predict_malaria
from config import Config
import os

predict_routes = Blueprint('predict_routes', __name__)

@predict_routes.route('/predict/<filename>', methods=['GET'])
def predict(filename):
    # Vérifier si le fichier existe
    # Construire correctement le chemin complet
    file_path = os.path.join(Config.UPLOAD_FOLDER, filename)
    if not os.path.exists(file_path):
        return render_template('index.html', error="Fichier non trouvé. Veuillez réessayer.")

    # Effectuer la prédiction
    result, error = predict_malaria(filename)

    if error:
        return render_template('index.html', error=error)

    # Passer le chemin de l'image et le résultat au template result.html
    uploaded_image = f"/uploaded_file/{filename}"
    return render_template('result.html', uploaded_image=uploaded_image, result=result)
