''' This is module docstring'''
class Perceptron:
    '''Class Perceptron'''

    def __init__(self, inputs):
        '''Initialization'''
        self.dummied_inputs = inputs
        self._weights = None

    def train(self, inputs, labels):
        '''Training on labeled data'''
        dummied_inputs = [observation + [-1] for observation in inputs]
        self._weights = [0.2] * len(dummied_inputs[0])
        for _ in range(5000):
            for value, label in zip(dummied_inputs, labels):
                label_delta = label - self.predict(inputs)
                self._weights[value] += .1 * value * label_delta


    def predict(self, new_data):
        '''Label new data'''
        if len(new_data) == 0:
            return None
        new_data = new_data + [-1]
        return int(0 < sum([x[0]*x[1] for x in zip(self._weights, new_data)])) # pylint: disable=R1728
