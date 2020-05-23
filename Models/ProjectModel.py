import pickle


class ProjectModel:

    def __init__(self, filename='./Models/projectModel.sav'):
        self._filename = filename
        self._model = None
        self.loadModel()

    def loadModel(self):
        self._model = pickle.load(open(self._filename, 'rb'))

    def predict_proba(self, data):
        return self._model.predict_proba(data)[:, 1]

# data = [[259., 0., 173.60805556, 77.,
#                  5., 0., 0., 1.,
#                  0., 0., 0., 0.,
#                  0., 0., 0., 0.,
#                  0., 0., 0., 0.,
#                  0., 1., 0., 0.,
#                  0., 0., 0., 0.,
#                  0., 1., 0., 0.,
#                  0., 0.]]
# model = ProjectModel().predict_proba(data)
# print(model[0])