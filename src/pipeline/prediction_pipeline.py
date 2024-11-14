import numpy as np
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing import image 
import os

class PredictionPipeline:
    def __init__(self,file_name):
        self.filename=file_name

    def predict(self):
        model = load_model('artifacts/training/model.h5')

    # Load and preprocess the image
        test_image = image.load_img(self.filename, target_size=(224, 224))
        test_image = image.img_to_array(test_image) / 255.0 
        test_image = np.expand_dims(test_image, axis=0)

    # Get the raw prediction
        predictions = model.predict(test_image)
        print("Raw predictions:", predictions)

    # Get the predicted class index
        result = np.argmax(predictions, axis=1)
        print("Predicted class index:", result)

    # Return the result
        if result[0] == 1:
            prediction = 'Tumor'
        else:
            prediction = 'Normal'

        return [{"image": prediction}]