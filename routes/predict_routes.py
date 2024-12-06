from flask import Blueprint, render_template
from model import predict_malaria

predict_routes = Blueprint('predict_routes', __name__)

@predict_routes.route('/predict/<filename>', methods=['GET'])
def predict(filename):
    result, error = predict_malaria(filename)

    if error:
        return render_template('index.html', error=error)

    return render_template('result.html', result=result, filename=filename)