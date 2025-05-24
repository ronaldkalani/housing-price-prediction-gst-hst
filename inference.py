import joblib
import os
import numpy as np

def model_fn(model_dir):
    model_path = os.path.join(model_dir, "model.joblib")
    return joblib.load(model_path)

def input_fn(request_body, request_content_type):
    if request_content_type == "text/csv":
        return np.array([float(x) for x in request_body.strip().split(',')]).reshape(1, -1)
    raise ValueError("Unsupported content type: {}".format(request_content_type))

def predict_fn(input_data, model):
    return model.predict(input_data)

def output_fn(prediction, content_type):
    return str(prediction[0])
