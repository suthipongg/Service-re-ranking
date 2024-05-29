from sentence_transformers.cross_encoder import CrossEncoder
import os

class CrossEncoderModel:
    def __init__(self):
        self.model = CrossEncoder(os.getenv('MODEL_PATH'))

    def predict(self, pairs_qa):
        return self.model.predict(pairs_qa)

if __name__ == "__main__":
    cros_encoder = CrossEncoderModel()
    result = cros_encoder.predict([["What is the capital of France?", "Paris"]])
    print(result)