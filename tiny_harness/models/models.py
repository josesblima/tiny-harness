from enum import Enum

class ModelManager():
    def __init__(self):
        self.current_model: Model = Model.QWEN38

    def switch_model(self, model: Model):
        current_model = model

class Model(Enum):
    QWEN38 = 'qwen3.8:27b'
    CODERNEXT = 'qwen3-coder-next'
