import tensorflow as tf
from tensorflow.keras.preprocessing import image
import numpy as np

# Charger le modèle préalablement sauvegardé
model = tf.keras.models.load_model('votre_modele.h5')

def predict_malaria(filename):
    """Effectue la prédiction sur l'image et retourne le résultat."""
    try:
        img_path = f'static/uploads/{filename}'
        img = image.load_img(img_path, target_size=(128, 128))  # Redimensionner l'image
        img_array = image.img_to_array(img) / 255.0  # Normaliser l'image
        img_array = np.expand_dims(img_array, axis=0)  # Ajouter une dimension pour le batch

        prediction = model.predict(img_array)
        result = 'Infectée' if prediction[0] > 0.5 else 'Non infectée'

        return result, None  # Pas d'erreur

    except Exception as e:
        return None, str(e)  # Retourne l'erreur si quelque chose se passe mal