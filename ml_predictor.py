import random


class DummyModelInstance(object):
    "dummy model instance"

    @staticmethod
    def predict():
        return random.random()


def load_model():
    "model loader"
    print("loading model")
    return DummyModelInstance()


class MonoState(object):
    _internal_state = {}

    def __new__(cls, *args, **kwargs):
        obj = super(MonoState, cls).__new__(cls, *args, **kwargs)
        obj.__dict__ = cls._internal_state
        return obj


class Predictor(MonoState):
    _internal_state = {'model': load_model()}

    def predict(self):
        forecast = self.model.predict()
        return forecast


if __name__ == '__main__':
    a = Predictor()
    print('object a       :', a)
    print('object a model :', a.model)
    print('forecast for a :', a.predict())
    b = Predictor()
    print('object b       :', b)
    print('object b model :', b.model)
    print('forecast for b :', b.predict())
